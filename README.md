# The 128 GB Club

Open-weight AI models for the lucky owners of **128 GB of unified memory**: what fits, what runs, and what the people who actually use them say.

Members only, in a friendly way: every model is judged against the same 128 GB, so "fits" and "too large" mean something. Language, vision, OCR, image, video, speech, music, translation, time-series and more.

## Who it is for

Machines whose CPU and GPU share 128 GB of memory:

- **Apple silicon** Macs with 128 GB (Mac Studio, MacBook Pro). Runtimes are checked here first: MLX, llama.cpp, Ollama.
- **AMD Ryzen AI Max+ (Strix Halo)** and **NVIDIA DGX Spark** machines with 128 GB: the size limits apply the same way; llama.cpp and Ollama run there; MLX is mainly for Apple silicon. Runtime notes for these machines are not checked.

What "fits" means is defined in [`research-method.md`](research-method.md#memory-target).

**Languages**: the language notes focus on **English, French, German and Italian** ("FR/DE untested" means no user report was found for French or German). Other languages are listed when the model card names them.

## What is here

| Part | Content | Status |
|---|---|---|
| **Model attic** | One record per model: licence, size, formats, publisher, release date, runtimes, plus short summaries of user feedback with links (Hacker News, Hugging Face discussions, runtime GitHub issues; Reddit when it can be read). A small tool checks the records and renders [`model-comparison.md`](model-comparison.md). | 107 models |
| **[Glossary](glossary.md)** | Terms, software and organisations met along the way, with French, German and Italian translations. | ≈ 190 terms |
| **Taxonomies** | Overviews of [image](taxonomies/image-tools.md), [music](taxonomies/music-tools.md), [speech and voice](taxonomies/speech-tools.md), [document](taxonomies/document-tools.md), [vision and 3D](taxonomies/vision-3d-tools.md), [retrieval and RAG](taxonomies/retrieval-tools.md), [code](taxonomies/code-tools.md), [video](taxonomies/video-tools.md) and [time-series](taxonomies/time-series-tools.md) tools: what each kind of model does, and the main open candidates. | 9 |
| **[Research method](research-method.md)** | How facts and user feedback are gathered: sources, recency window, rules for summaries. | – |

## Using the tool

Requires [uv](https://docs.astral.sh/uv/). From the repository root:

```bash
uv run tools/model_compare.py validate        # check every models/*.json against tools/model.schema.json
uv run tools/model_compare.py render          # regenerate model-comparison.md
uv run tools/model_compare.py show qwen3.8-27b
uv run tools/model_compare.py refresh ID      # update facts from the Hugging Face API (metadata only)
```

`--private FILE` merges your own overlay (selection, decisions, pinned revisions) over the public records and writes the full view next to that file; see `uv run tools/model_compare.py --help`.

## Principles

- **Facts from the official source** (model card, Hugging Face API, licence file), dated.
- **Feedback from people who ran the model**, not from announcements; summarised in our own words, always with the link and the date: a comment without a source is not recorded. Thin feedback is said to be thin.
- **Open licences and safe formats first**: the records show the licence and whether the weights are in safetensors or GGUF.
- **Third-party conversions checked**: an MLX or GGUF copy made by someone other than the publisher is checked against the original (uploader, tensor headers and sizes, no code, reviewed conversion, licence); the result, strong, consistent or weak, is in the record's `provenance` fact. See [`research-method.md`](research-method.md#third-party-conversions).
- Metadata only: this repository contains no model weights.

## Licence

- **Code** (`tools/`): MIT, see [`LICENSE`](LICENSE).
- **Content** (model records, glossary, taxonomies, generated tables, documentation): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), see [`LICENSE-content`](LICENSE-content). Reuse freely, with credit.
- The linked sources belong to their authors; this repository summarises them in its own words.
