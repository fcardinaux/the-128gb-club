# Model records

One JSON file per model, valid against [`../tools/model.schema.json`](../tools/model.schema.json). The comparison table [`../model-comparison.md`](../model-comparison.md) is generated from these files; do not edit it by hand.

## Contents of a record

- **Identity**: `id` (same as the file name), `name`, `category`, `usage`.
- **Sources**: Hugging Face repositories, Ollama tags or GitHub projects. `role`: `download` (default, the files that run the model), `facts` (official repository used for facts only), `info` (related, for information).
- **Facts** (verifiable): licence, gated or not, publisher, release date, parameters (total and active), size, formats, languages, runtimes, whether it fits in 128 GB of unified memory (definition in [`../research-method.md`](../research-method.md#memory-target)). Each value carries its `source` and the date it was `checked`.
- **Appraisals**: `web` (one-line verdict, summary, search date, scope of the search, amount of feedback: none, thin, moderate or rich) and `speed`.
- **Comments**: user feedback from the web, `positive`, `negative` or `neutral`, summarised in our own words in English, with `refs` (link, author, date, site). The method is in [`../research-method.md`](../research-method.md).

## Commands

From the repository root:

```bash
uv run tools/model_compare.py validate          # check every record against the schema
uv run tools/model_compare.py refresh [ID ...]  # update facts from the Hugging Face API (metadata only, never weights)
uv run tools/model_compare.py render            # regenerate model-comparison.md
uv run tools/model_compare.py show ID           # one model in readable form
```

After any change to a record: `validate`, then `render`, then commit both.

## Notes on the research of 13.11.2026

- **Reddit could not be read** by automated tools; summaries of Reddit threads published by other sites were not used as evidence. The `scope` of each record says which sources were read.
- **Sources by family**:
  - language models: Hacker News comments, Hugging Face discussions, issues of Ollama, llama.cpp and mlx-lm;
  - OCR and voice: Hacker News comments, Hugging Face discussions, issues of Ollama, QwenLM, resemble-ai/chatterbox and mlx-audio (now `Neywa-Labs/mlx-audio`);
  - image and video: Hacker News comments, Hugging Face discussions, issues of mflux, ComfyUI, mlx-video and ComfyUI-WanVideoWrapper.
- **Successors with less open terms**: Qwen-Image-2.1 (14.09.2026) has a non-commercial research licence; FLUX.3 Klein (13.10.2026) has the licence "other" and is gated; Wan 2.5 and later have no published weights (Wan 3.0 is API only). On that date, Qwen-Image-2512, Qwen-Image-Edit-2511, FLUX.2 Klein 4B and Wan 2.2 were still the latest Apache 2.0 versions of their families.
- **Wan 2.2 Diffusers repositories**: with transformers 5.0 to 5.2 the text encoder loads with `embed_tokens MISSING` and the video ignores the prompt. Fixed by transformers PR #43880 (merged 19.02.2026, probably in 5.3); with an older 5.x, pin `transformers==4.57.1`.
- **mlx-video and Wan 2.2** (checked 14.11.2026): its converter reads the original Wan-AI checkpoints, including `.pth` text-encoder and VAE files, not the Diffusers repositories.
- **French and German accents** rendered in images: no user report found for any image model.
