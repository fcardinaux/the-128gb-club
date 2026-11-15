# Sources and method for researching models

Created on 13 November 2026. How the model records of this repository are researched, by a person or by an AI agent.

## Method

1. **Facts first, from the official source**: licence, size, formats, gated or not, publication date, commit (Hugging Face `model_info` API, Ollama library page). Metadata only, never weights.
2. **Then user feedback from the web**, read critically: comments from people who actually ran the model, not announcements.
3. **Recency window, depending on the model's age:**

   | Model age | Comments to read |
   |---|---|
   | Less than 3 months | All comments since the release |
   | 3 to 12 months | Comments from the last 6 months, plus the launch discussion |
   | More than 12 months | Comments from the last 6 months only (is it still used, has it been replaced?) |

4. **Record the comments in `models/<model>.json`**, one file per model (format: `tools/model.schema.json`): each comment **summarised in our own words** (no quotes), with its sentiment, link, author and date, (a comment without a source link is not recorded: `validate` refuses it, and leads seen only through a mirror or a summary site are not comments), and the overall summary in `appraisals.web`. Comments written in another language are summarised in English, keeping the link to the original. Add new comments to the existing file with the search date; put a one-line verdict in `appraisals.web.verdict`, then run `uv run tools/model_compare.py validate` and `render`.
5. **Report the evidence honestly**: link each comment used, give its date, and say so when there is little or no feedback. Vendor benchmarks and SEO "best LLM for X" pages are leads, not evidence.

## Memory target

Added on 15 November 2026. Every record is judged against **128 GB of unified memory** (fact `fits_128gb`):

- **true**: at least one usable build (official weights or a checked conversion, at a named quantisation) is **100 GB or less**. That leaves about 28 GB for the context (KV cache), the runtime and the operating system.
- **false**: every build is larger, or the model runs only by streaming weights from the SSD. The record says so in `runtimes` and in the note of `fits_128gb`.
- A build between 100 and about 115 GB is noted as **tight** in the note: it loads, with little context.
- A repository that holds several checkpoints or experts used one at a time (e.g. Wan 2.2 A14B, LTX 2.3) is judged on what is loaded at once, with a source.

On macOS the GPU may use only part of the memory by default (often quoted as about 75 %); `sysctl iogpu.wired_limit_mb` raises it, and the MLX documentation warns to keep it strictly below the total memory. Apple does not document the setting, so the default can change between macOS versions. On Strix Halo the GPU share is set in the BIOS (UMA allocation, see [AMD's ROCm notes](https://rocm.docs.amd.com/en/docs-7.2.0/how-to/system-optimization/strixhalo.html)); on DGX Spark the whole pool is shared.

## Third-party conversions

Added on 15 November 2026. Some official releases are only in pickle formats (`.pt`, `.pth`, `.ckpt`) or do not run on a Mac, and a third party (mlx-community, lmstudio-community, an individual) publishes a converted copy. A converted copy is trusted only after these checks, all done on metadata (nothing downloaded):

1. **Provenance**: who uploaded it and when (commit history), `base_model` in the card, the tool and the source revision used for the conversion (`conversion.json` or `provenance.json` when present).
2. **Same weights**: the safetensors header, read through the Hugging Face API, gives tensor names, dtypes and the parameter count. Compare with the official release: parameter count, file sizes (an fp16 copy is half of an fp32 original, plus or minus the pickle overhead), sha256 of the source files when the converter lists them.
3. **No code**: safetensors, GGUF and JSON only.
4. **Reviewed conversion code**: the runtime pull request that adds the model (mlx-vlm, mlx-audio…) was merged by a maintainer; an equivalence test against the reference implementation is reported.
5. **Feedback**: downloads, Hugging Face discussions of the copy, runtime issues.
6. **Licence**: a conversion does not change the licence; it is the original's. A copy whose card shows a different licence is flagged.
7. **After download**: compare the copy's output with the publisher's reference examples on a few inputs.

The result goes into the record, fact `provenance`: a short value (strong, consistent, weak) with what was compared, the source and the date.

## Sources

| Source | What to read | How | Notes |
|---|---|---|---|
| **Hacker News** | **Comments only**, not the linked articles | Algolia API: `https://hn.algolia.com/api/v1/search_by_date?query=<name>&tags=comment&typoTolerance=false&advancedSyntax=true&numericFilters=created_at_i><unix time>` | First-choice source: detailed, experienced discussions. Use exact matching, otherwise "EuroLLM" matches hundreds of unrelated comments |
| **r/LocalLLaMA** (Reddit) | Comment threads on releases and comparisons | Web search; Reddit pages are often hard to fetch | Many hands-on reports on Apple silicon and quantisations |
| **Hugging Face "Community" tab** of the model | Discussions and issues opened by users | `https://huggingface.co/<repo>/discussions` | Bugs, licence questions, broken files |
| **GitHub issues** of the runtimes | Ollama, llama.cpp, mlx-lm, mlx-audio, mflux | Search the model name in the issues | Shows whether the model actually runs on a Mac |
| **WMT findings** (translation only) | Human evaluation of the yearly shared task | Conference proceedings (WMT 2025, WMT 2026) | Independent, but lags behind new releases |
| **Papers and technical reports** | Per-language tables | arXiv | Authors' own claims; check the language pairs that matter (EN, FR, DE) |
| **Simon Willison's blog** | Hands-on notes on new local models | simonwillison.net | Short, practical, dated |

## Languages

The records focus on **English, French, German and Italian**. For language-related models (voice, speech recognition, translation, OCR), they note support for these four when known, and say when no user report was found (e.g. "FR/DE untested"). Other languages are listed when the model card names them.
