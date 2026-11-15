# /// script
# requires-python = ">=3.11"
# dependencies = ["jsonschema>=4.23,<5"]
# ///
"""The 128 GB Club comparison tool: one JSON file per model in models/, checked and rendered as a comparison table.

Commands (run from the repository root):
  uv run tools/model_compare.py validate              check every models/*.json against tools/model.schema.json
  uv run tools/model_compare.py refresh [ID ...]      update verifiable facts from the Hugging Face API (metadata only)
  uv run tools/model_compare.py render                write model-comparison.md (generated view, do not edit)
  uv run tools/model_compare.py show ID               print one model's facts and comments

Options, placed before the command:
  --private FILE     merge your own overlay (shortlist, decisions, pinned revisions) over the
                     public records; it is checked against FILE's sibling <name>.schema.json, and the
                     full view is written next to FILE instead of this repository
  --manifest FILE    with --private: also check consistency with a download manifest (Markdown file
                     with a "## Manifeste" TOML block)
  --output FILE      where `render` writes its Markdown file

Never downloads weights: `refresh` only reads https://huggingface.co/api/models/<repo>.
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import os
import re
import sys
import tomllib
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS = ROOT / "models"
SCHEMA = Path(__file__).resolve().parent / "model.schema.json"
TODAY = dt.date.today().isoformat()
WEIGHT_EXT = (".safetensors", ".gguf", ".bin", ".pt", ".pth", ".ckpt", ".pdiparams")

LICENCE_NAMES = {"apache-2.0": "Apache 2.0", "mit": "MIT", "agpl-3.0": "AGPL-3.0", "gpl-3.0": "GPL-3.0", "openrail": "OpenRAIL", "other": "other"}
STATUS_ORDER = ["selected", "candidate", "later", "excluded"]
STATUS_TITLE = {"selected": "Shortlisted", "candidate": "Candidates", "later": "Later", "excluded": "Excluded by a policy"}
CATEGORY_ORDER = ["llm", "code", "vision", "embeddings", "reranker", "guard", "ocr", "asr", "tts", "translation", "image", "video", "music", "chess", "timeseries"]
CATEGORY_TITLE = {"llm": "General language models", "code": "Code", "vision": "Image understanding", "embeddings": "Embeddings",
                  "reranker": "Rerankers", "guard": "Guard models", "ocr": "OCR", "asr": "Speech recognition", "tts": "Speech synthesis",
                  "translation": "Translation", "image": "Image generation and editing", "video": "Video", "music": "Music", "chess": "Chess",
                  "timeseries": "Time-series forecasting"}
PUBLIC_FACTS = ["licence", "gated", "publisher", "release_date", "parameters_total_b", "parameters_active_b",
                "size_gb", "formats", "languages", "runtimes", "fits_128gb", "provenance"]
PRIVATE_FACTS = ["added", "downloaded"]
PRIVATE_TOP = ["manifest_ids", "status", "decision", "exclusion_reason", "notes"]

OPTS: argparse.Namespace


# ---------------------------------------------------------------- data access
def load_public() -> dict[str, dict]:
    return {p.stem: json.loads(p.read_text()) for p in sorted(MODELS.glob("*.json"))}


def load_overlay() -> dict[str, dict]:
    return json.loads(Path(OPTS.private).read_text()) if OPTS.private else {}


def merge(pub: dict | None, ov: dict | None, mid: str) -> dict:
    """Public record plus its private overlay (if any)."""
    rec = copy.deepcopy(pub) if pub else {"id": mid, "name": ov.get("name", mid), "category": ov.get("category", "llm"),
                                          "sources": [], "facts": {}, "appraisals": {}, "comments": [], "private_only": True}
    if not pub and ov.get("usage"):
        rec["usage"] = ov["usage"]
    if not ov:
        return rec
    for k in PRIVATE_TOP:
        if k in ov:
            rec[k] = ov[k]
    for s in ov.get("sources", []):
        if s["index"] < len(rec["sources"]):
            rec["sources"][s["index"]].update({k: s[k] for k in ("revision", "files", "note") if k in s})
    rec["facts"].update(ov.get("facts", {}))
    if ov.get("appraisals", {}).get("speed"):
        rec["appraisals"]["speed"] = rec["appraisals"].get("speed", []) + ov["appraisals"]["speed"]
    return rec


def load_models() -> dict[str, dict]:
    pub, ov = load_public(), load_overlay()
    ids = sorted(set(pub) | set(ov))
    return {i: merge(pub.get(i), ov.get(i), i) for i in ids}


def save_public(rec: dict) -> None:
    """Write back only the public part of a (possibly merged) record."""
    path = MODELS / f"{rec['id']}.json"
    pub = json.loads(path.read_text())
    pub["facts"] = {k: rec["facts"][k] for k in PUBLIC_FACTS if k in rec["facts"]}
    path.write_text(json.dumps(pub, ensure_ascii=False, indent=2) + "\n")


def manifest() -> dict[str, dict]:
    m = re.search(r"## Manifeste.*?```toml\n(.*?)```", Path(OPTS.manifest).read_text(), re.S)
    return {x["id"]: x for x in tomllib.loads(m.group(1))["modele"]} if m else {}


# ---------------------------------------------------------------- validate
def schema_problems(validator, obj) -> list[str]:
    return [f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message}" for e in validator.iter_errors(obj)]


def cmd_validate(_args) -> int:
    from jsonschema import Draft202012Validator

    validator = Draft202012Validator(json.loads(SCHEMA.read_text()))
    errors = 0

    def report(name: str, problems: list[str]) -> None:
        nonlocal errors
        if problems:
            errors += len(problems)
            print(f"✗ {name}")
            for p in problems:
                print(f"    {p}")

    public = load_public()
    for fid, rec in public.items():
        problems = schema_problems(validator, rec)
        if rec.get("id") != fid:
            problems.append(f"id {rec.get('id')!r} differs from file name")
        for i, c in enumerate(rec.get("comments", [])):
            if not c.get("refs") and "](http" not in c.get("text", ""):
                problems.append(f"comments/{i}: no source link (refs or a link in the text)")
        report(fid, problems)

    if OPTS.private:
        ov_path = Path(OPTS.private)
        ov_schema = ov_path.with_name(ov_path.stem + ".schema.json")
        overlay = load_overlay()
        if ov_schema.exists():
            report(ov_path.name, schema_problems(Draft202012Validator(json.loads(ov_schema.read_text())), overlay))
        else:
            report(ov_path.name, [f"schema {ov_schema.name} not found"])
        for mid, ov in overlay.items():
            problems = []
            if mid not in public and not ov.get("name"):
                problems.append("no public record and no name (private-only records need name and category)")
            for s in ov.get("sources", []):
                src = public.get(mid, {}).get("sources", [])
                if s["index"] >= len(src):
                    problems.append(f"sources index {s['index']} out of range")
                elif any(s.get(k) != src[s["index"]].get(k) for k in ("kind", "repo", "tag") if k in s):
                    problems.append(f"sources index {s['index']} does not match the public source")
            report(f"{ov_path.name}: {mid}", problems)
        for mid in sorted(set(public) - set(overlay)):
            report(f"{ov_path.name}: {mid}", ["public record without private entry"])

    if OPTS.manifest:
        man = manifest()
        seen: dict[str, str] = {}
        for fid, rec in load_models().items():
            problems = []
            mids = rec.get("manifest_ids", [])
            if rec.get("status") == "selected" and not mids:
                problems.append("status 'selected' but no manifest_ids")
            for mid in mids:
                if mid in seen:
                    problems.append(f"manifest id {mid!r} also used by {seen[mid]}")
                seen[mid] = fid
                if mid not in man:
                    problems.append(f"manifest id {mid!r} not in the manifest")
                    continue
                entry = man[mid]
                ref = entry.get("ollama") or entry.get("hf")
                src = [s for s in rec.get("sources", []) if s.get("tag") == ref or s.get("repo") == ref]
                if not src:
                    problems.append(f"{mid}: manifest source {ref!r} missing from sources")
                elif entry.get("revision") and not any(s.get("revision") == entry["revision"] for s in src):
                    problems.append(f"{mid}: revision differs from the manifest")
            report(fid, problems)
        for mid in sorted(set(man) - set(seen)):
            report(f"manifest id {mid!r}", ["no model record"])

    n = len(public)
    scope = " + private overlay" if OPTS.private else ""
    scope += " + manifest" if OPTS.manifest else ""
    print(f"{n} public records{scope}: {errors} problem(s)" if errors else f"✓ {n} public records valid{scope}")
    return 1 if errors else 0


# ---------------------------------------------------------------- refresh (Hugging Face metadata only)
def hf_info(repo: str) -> dict:
    url = f"https://huggingface.co/api/models/{repo}?blobs=true"
    req = urllib.request.Request(url, headers={"User-Agent": "model-compare/1.0"})
    return json.load(urllib.request.urlopen(req, timeout=30))


def selected_size(info: dict, files: list[str] | None) -> float:
    total = 0
    for s in info.get("siblings", []):
        name = s["rfilename"]
        if files and not any(name == f or name.startswith(f.rstrip("/") + "/") for f in files):
            continue
        total += s.get("size") or 0
    return round(total / 1e9, 1)


def cmd_refresh(args) -> int:
    models = load_models()
    ids = args.ids or [i for i, r in models.items() if not r.get("private_only")]
    for fid in ids:
        rec = models.get(fid)
        if rec is None or rec.get("private_only"):
            print(f"✗ {fid}: no public record")
            continue
        hf = [s for s in rec["sources"] if s["kind"] == "huggingface"]
        if not hf:
            print(f"- {fid}: no Hugging Face source (Ollama facts are checked by hand)")
            continue
        facts = rec["facts"]
        infos = {}
        for s in hf:
            try:
                infos[s["repo"]] = hf_info(s["repo"])
            except Exception as e:  # noqa: BLE001
                print(f"✗ {fid}: {s['repo']}: {e}")
        if not infos:
            continue
        facts_src = [s for s in hf if s.get("role") == "facts"] or [s for s in hf if s.get("role", "download") == "download"] or hf
        main = facts_src[0]["repo"]
        if main not in infos:
            continue
        info = infos[main]
        src = f"https://huggingface.co/api/models/{main}"
        card = info.get("cardData") or {}
        facts["licence"] = {"value": LICENCE_NAMES.get(card.get("license"), card.get("license")), "source": src, "checked": TODAY}
        facts["gated"] = {"value": bool(info.get("gated")), "source": src, "checked": TODAY}
        facts["publisher"] = {"value": main.split("/")[0], "source": f"https://huggingface.co/{main}", "checked": TODAY}
        facts["release_date"] = {"value": (info.get("createdAt") or "")[:10] or None, "source": src, "checked": TODAY, "note": "createdAt of the repository"}
        total = (info.get("safetensors") or {}).get("total")
        if total:
            facts["parameters_total_b"] = {"value": round(total / 1e9, 1), "source": src, "checked": TODAY}
        downloads = [s for s in hf if s.get("role", "download") == "download"]
        sizes = {(s["repo"] + (" " + ",".join(s["files"]) if s.get("files") else "")): selected_size(infos[s["repo"]], s.get("files")) for s in downloads if s["repo"] in infos}
        if sizes:
            facts["size_gb"] = {"value": next(iter(sizes.values())) if len(sizes) == 1 else sizes, "source": "Hugging Face API, file sizes", "checked": TODAY}
        else:
            facts["size_gb"] = {"value": selected_size(info, None), "source": src, "checked": TODAY, "note": "whole official repository"}
        exts = sorted({Path(s["rfilename"]).suffix for s in info.get("siblings", []) if Path(s["rfilename"]).suffix in WEIGHT_EXT + (".py",)})
        facts["formats"] = {"value": ", ".join(exts), "source": src, "checked": TODAY}
        save_public(rec)
        print(f"✓ {fid}: {facts['licence']['value']}, {facts['size_gb']['value']} GB, {facts['release_date']['value']}")
    return 0


# ---------------------------------------------------------------- render
def fact(rec: dict, key: str) -> str:
    f = rec["facts"].get(key)
    if not f:
        return "—"
    v = f["value"]
    if isinstance(v, dict):
        return "; ".join(f"{k}: {x:g}" if isinstance(x, (int, float)) else f"{k}: {x}" for k, x in v.items())
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, float):
        return f"{v:g}"
    return str(v) if v is not None else "—"


def size_cell(rec: dict) -> str:
    s = fact(rec, "size_gb")
    if "official repository" in rec["facts"].get("size_gb", {}).get("note", ""):
        s += " (official repo)"
    return s


def size_total(rec: dict) -> float | None:
    f = rec["facts"].get("size_gb")
    if not f:
        return None
    v = f["value"]
    if isinstance(v, dict):
        return sum(x for x in v.values() if isinstance(x, (int, float)))
    return v if isinstance(v, (int, float)) else None


FACT_NAMES = {"licence", "gated", "publisher", "release_date", "parameters_total_b", "parameters_active_b", "size_gb",
              "formats", "languages", "runtimes", "fits_128gb", "provenance"}


def cell(s: str) -> str:
    return (s or "—").replace("|", "\\|").replace("\n", " ")


def source_cell(src: str) -> str:
    """A fact's source as Markdown: URLs become short links, a fact name points to that fact."""
    if not src:
        return "—"
    if src in FACT_NAMES:
        return f"see {src}"
    parts = []
    for piece in re.split(r",\s+(?=https?://)", src):
        m = re.match(r"(https?://[^\s,;)]+)(.*)", piece.strip())
        if m:
            url, rest = m.groups()
            label = re.sub(r"^https?://(www\.)?", "", url).rstrip("/")
            label = label if len(label) <= 45 else label[:42] + "…"
            parts.append(f"[{label}]({url}){rest}")
        else:
            parts.append(piece.strip())
    return cell(", ".join(parts))


def comment_text(c: dict) -> str:
    """Comment text, followed by its sources when the text has no link of its own."""
    text = c["text"]
    if "](http" in text or not c.get("refs"):
        return text
    refs = "; ".join(f"[{', '.join(x for x in (ref.get('label'), ref.get('date')) if x) or 'source'}]({ref['url']})"
                     for ref in c["refs"])
    return f"{text} ({refs})"


def anchor(name: str) -> str:
    return re.sub(r"[^a-z0-9 -]", "", name.lower()).replace(" ", "-")


def sort_key(r: dict):
    return (CATEGORY_ORDER.index(r["category"]) if r["category"] in CATEGORY_ORDER else 99, r["name"].lower())


def output_path() -> Path:
    if OPTS.output:
        return Path(OPTS.output).resolve()
    if OPTS.private:
        return Path(OPTS.private).resolve().parent / "model-comparison.md"
    return ROOT / "model-comparison.md"


def cmd_render(_args) -> int:
    out_file = output_path()
    models_rel = os.path.relpath(MODELS, out_file.parent)
    models = load_models()
    private = bool(OPTS.private)
    head = [
        "# Model comparison" if private else "# The 128 GB Club: model comparison",
        "",
        f"Generated by `tools/model_compare.py render` on {TODAY} from `models/*.json`"
        + (" and the private overlay" if private else "")
        + ". **Do not edit by hand**: change the JSON files, then run the command again.",
        "",
        "Facts are verifiable: each one has its source and the date it was checked, in the model's section. "
        "\"Fits 128 GB\" follows the definition in `research-method.md` (Memory target). Appraisals summarise web feedback in our own words, with links. "
        "\"Positive\" and \"Negative\" count the web comments of each kind; each count links to the model's section, "
        "where every comment is listed with its source link and date.",
        "",
    ]
    out = list(head)
    columns = ["Model", "Usage", "Licence", "Size (GB)", "Fits 128 GB", "Released"] + (["Downloaded"] if private else []) + \
              ["Web verdict", "Feedback", "Positive", "Negative"] + (["Decision"] if private else [])

    def row(r: dict) -> str:
        web = r["appraisals"].get("web", {})
        pos = sum(c["sentiment"] == "positive" for c in r["comments"])
        neg = sum(c["sentiment"] == "negative" for c in r["comments"])
        name = f"[{r['name']}](#{anchor(r['name'])})"
        if private and r.get("manifest_ids"):
            name += "<br>" + ", ".join(f"`{m}`" for m in r["manifest_ids"])
        cells = [name, cell(r.get("usage", "")), fact(r, "licence"), size_cell(r), fact(r, "fits_128gb"), fact(r, "release_date")]
        if private:
            down = r["facts"].get("downloaded", {}).get("value")
            cells.append(down if isinstance(down, str) else "—")
        link = f"](#{anchor(r['name'])})"
        cells += [cell(web.get("verdict", "")), web.get("feedback", "—"),
                  f"[{pos}{link}" if pos else "0", f"[{neg}{link}" if neg else "0"]
        if private:
            cells.append(cell(r.get("decision") or r.get("exclusion_reason", "")))
        return "| " + " | ".join(cells) + " |"

    table_head = ["| " + " | ".join(columns) + " |", "|" + "---|" * len(columns)]
    if private:
        groups = [(STATUS_TITLE[s], [r for r in models.values() if r.get("status") == s]) for s in STATUS_ORDER]
    else:
        groups = [(CATEGORY_TITLE.get(c, c), [r for r in models.values() if r["category"] == c]) for c in CATEGORY_ORDER]
    order = []
    for title, recs in groups:
        if not recs:
            continue
        recs.sort(key=sort_key)
        order += recs
        line = f"{len(recs)} model{'s' if len(recs) != 1 else ''}."
        if private and title in (STATUS_TITLE["selected"], STATUS_TITLE["candidate"]):
            done = sum(size_total(r) or 0 for r in recs if isinstance(r["facts"].get("downloaded", {}).get("value"), str))
            line = f"{len(recs)} models, ≈ {sum(size_total(r) or 0 for r in recs):,.0f} GB in total, of which ≈ {done:,.0f} GB downloaded."
        out += [f"## {title}", "", line, ""] + table_head + [row(r) for r in recs] + [""]
    out += ["## Details", ""]
    for r in order:
        out += details(r, models_rel, private)
    out_file.write_text("\n".join(out).rstrip() + "\n")
    print(f"✓ {out_file} written ({len(order)} models)")
    return 0


def details(r: dict, models_rel: str = "models", private: bool = False) -> list[str]:
    web = r["appraisals"].get("web", {})
    head = f"File: [`models/{r['id']}.json`]({models_rel}/{r['id']}.json)." if not r.get("private_only") else "Private record only."
    if private and r.get("status"):
        head += f" Status: {r['status']}."
    lines = [f"### {r['name']}", "", head]
    srcs = []
    for s in r["sources"]:
        ref = s.get("repo") or s.get("tag") or ""
        t = f"{s['kind']} `{ref}`" if ref else s["kind"]
        if s.get("files"):
            t += " (" + ", ".join(f"`{f}`" for f in s["files"]) + ")"
        if s.get("revision"):
            t += f", revision `{s['revision'][:12]}`"
        if s.get("role") in ("facts", "info"):
            t += f" [{s['role']}]"
        if s.get("note"):
            t += f" – {s['note']}"
        srcs.append(t)
    if srcs:
        lines += ["", "Sources: " + "; ".join(srcs) + "."]
    if r["facts"]:
        lines += ["", "| Fact | Value | Source | Checked |", "|---|---|---|---|"]
        for k, f in r["facts"].items():
            val = fact(r, k) + (f" ({f['note']})" if f.get("note") else "")
            lines.append(f"| {k} | {cell(val)} | {source_cell(f.get('source', ''))} | {f.get('checked', '—')} |")
    if web.get("summary"):
        lines += ["", f"**Web summary** (searched {web.get('searched', '—')}, feedback {web.get('feedback', '—')}): {web['summary']}"]
    for sent, title in (("negative", "Negative"), ("positive", "Positive"), ("neutral", "Neutral")):
        cs = [c for c in r["comments"] if c["sentiment"] == sent]
        if cs:
            lines += ["", f"**{title}**", ""] + [f"- {comment_text(c)}" for c in cs]
    for n in r.get("notes", []):
        lines += ["", f"_Note:_ {n}"]
    return lines + [""]


# ---------------------------------------------------------------- show
def cmd_show(args) -> int:
    rec = load_models().get(args.id)
    if rec is None:
        print(f"✗ no such model: {args.id}")
        return 1
    print("\n".join(details(rec, private=bool(OPTS.private))))
    return 0


def main() -> int:
    global OPTS
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--private", metavar="FILE", help="private overlay JSON merged over the public records")
    p.add_argument("--manifest", metavar="FILE", help="download manifest to check against (needs --private)")
    p.add_argument("--output", metavar="FILE", help="output file of render")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate").set_defaults(func=cmd_validate)
    r = sub.add_parser("refresh")
    r.add_argument("ids", nargs="*")
    r.set_defaults(func=cmd_refresh)
    sub.add_parser("render").set_defaults(func=cmd_render)
    s = sub.add_parser("show")
    s.add_argument("id")
    s.set_defaults(func=cmd_show)
    OPTS = p.parse_args()
    if OPTS.manifest and not OPTS.private:
        p.error("--manifest needs --private")
    return OPTS.func(OPTS)


if __name__ == "__main__":
    sys.exit(main())
