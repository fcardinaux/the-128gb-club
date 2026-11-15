# Taxonomy of local AI coding tools

Research of 15 November 2026, metadata and user feedback only. Companion of the other files in this folder.
"Covered by documented models?" tells whether the task is already covered by models with a record in [`../model-comparison.md`](../model-comparison.md#code): Laguna XS 2.1 and XS.2, Mellum2-12B-A2.5B-Base, Qwen2.5-Coder base, Qwen3-Coder-Next, Qwen3.8-27B, sweep-next-edit, Zeta 2/2.1, plus the general models (GLM-5.3-Flash, DeepSeek V4-Flash, gpt-oss-120b, Qwen3.6-35B-A3B).
"Licence and format pitfalls" assume a strict policy: Apache 2.0 or MIT licences, safetensors or GGUF weights, no gated repository.
**Reddit could not be read**. Licences, gating, sizes and commits come from the Hugging Face API, read on 15.11.2026; commits are the first 12 characters.

## Reference resources

| Resource | Last update | What it covers | Strengths | Weaknesses |
|---|---|---|---|---|
| [SWE-bench](https://www.swebench.com/) (Verified, Bash-only, Multilingual, Multimodal) | not checked | Fixing real GitHub issues | The standard agentic benchmark; Bash-only compares models under one scaffold | Saturated or contaminated at the top; scaffold-dependent |
| SWE-bench Pro, Terminal-Bench 2.1 | not checked | Harder agentic tasks | Less saturated | Few open-model entries |
| [LiveCodeBench](https://livecodebench.github.io/) | Hugging Face Space 07.06.2024; site not checked | Competitive programming in time windows | Limits contamination | Not agentic |
| [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) | 20.11.2025 | Code editing in 6 languages | Measures diff-format edits | **Stale**: no 2026 models |

## Taxonomy

| # | Category → sub-tasks | Typical uses | Covered by documented models? | Licence and format pitfalls |
|---|---|---|---|---|
| 1 | **Autocomplete (fill-in-the-middle)** | Inline completion in an editor (llama-vscode, Continue, Zed) | **Yes** (Qwen2.5-Coder base, Mellum2 base) | Use base models, not instruct; Codestral: MNPL (non-production) |
| 2 | **Next-edit prediction** | Predicting the next edit from recent changes | **Yes** (sweep-next-edit, Zeta) | – |
| 3 | **Agentic coding** → tool use, multi-file changes | opencode, aider, Goose, Continue agent | **Yes** (several records) | Many large coders use custom licences: OpenMDW, modified MIT, Qwen community |
| 4 | **Reasoning code models** | Algorithms, tests | Partly | – |
| 5 | **Code review** | Pull-request review, security audit | Through general models only; no dedicated open review model found | Hallucinated findings |
| 6 | **Speculative-decoding drafts** (DFlash, MTP, small same-family models) | Speeding up a large coder | No | A draft is tied to its target model and runtime; DFlash support in llama.cpp and MLX not checked |

## Hacker News comments used

Algolia API, comments only. Window: since 13.05.2026.

- On a 128 GB Mac, Laguna 2.1 codes very fast at roughly Sonnet 4.5 level (enthusiastic, unverified) ([rogerkirkness, 11.11.2026](https://news.ycombinator.com/item?id=50448768)).
- On a Mac, MoE models (Laguna XS 2.1 6-bit, Qwen3.8-Flash-Next) preferred, because a dense 27B is slow ([mark_l_watson, 11.11.2026](https://news.ycombinator.com/item?id=50454127)).
- Laguna S 2.1 weights had problems at launch, fixed later; template bugs at launch are common ([embedding-shape, 04.11.2026](https://news.ycombinator.com/item?id=50361406)); Laguna S 2.1 already overtaken by newer open models ([walrus01, 06.11.2026](https://news.ycombinator.com/item?id=50388260)).
- Qwen3-Coder-30B-A3B is an old non-reasoning model, far behind Qwen3.8-27B ([lukewarm707, 21.10.2026](https://news.ycombinator.com/item?id=50181243)); snappier and more accurate than Qwen3.6 in one user's tests ([trey-jones, 30.06.2026](https://news.ycombinator.com/item?id=48727517)); hallucinated tool calls with an MCP tool ([victor_pudeyev, 02.10.2026](https://news.ycombinator.com/item?id=49936051)).
- Recent Mistral models, Devstral included, weak compared with their claims ([segmondy, 06.10.2026](https://news.ycombinator.com/item?id=49979079)); Devstral 2 an acceptable compromise ([ywvcbk, 08.09.2026](https://news.ycombinator.com/item?id=49606979)); Devstral Small 2 follows style examples well when writing docs ([badsectoracula, 05.06.2026](https://news.ycombinator.com/item?id=48411059)).
- Searches with no usable result: Mellum 2.1, Seed-Coder, DFlash drafts, llama-vscode.

## Candidates by category

"Main option" = the best candidate under the strict policy; "Alternative" = also usable; "Flag" = usable only after a check. Already documented models are not repeated here.

### 3–4. Agentic and general coding

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`JetBrains/Mellum2.1-12B-A2.5B-Thinking`** (official GGUF, Apache 2.0) | Apache 2.0 | 24.30 GB (GGUF repo, 11 quantisations: 130.4 GB) | `92ddae9fc766` (GGUF `4159d684ffdb`) | llama.cpp, Ollama; MTP repositories by JetBrains | Not running on AMD GPUs with Vulkan or ROCm ([HF #3](https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking/discussions/3), 21.10.2026); no HN feedback | **Main option** for a small fast model (20.09.2026); self-reported SWE-bench Verified 47.0, LiveCodeBench v6 82.0 |
| `mistralai/Devstral-Small-2-24B-Instruct-2512` | Apache 2.0 | 51.59 GB (mlx-community 8-bit: 26.55 GB) | `55c5b41e98c2` | MLX, GGUF | Mixed on HN (see above); instruction injection through third-party docs measured ([HF #31](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512/discussions/31), 26.08.2026); chat-template fix for tool turns ([HF #30](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512/discussions/30), 02.07.2026) | Alternative. The unsloth GGUF declares licence "other", unlike the original |
| `Qwen/Qwen3-Coder-30B-A3B-Instruct` | Apache 2.0 | 61.07 GB (MLX 8-bit 32.44 GB) | `b2cff646eb4b` | MLX, llama.cpp, Ollama | Mixed and ageing (see above) | Alternative: fast, non-reasoning; superseded by Qwen3-Coder-Next and Qwen3.8-27B |
| `JetBrains/Qwen3.8-3.6-27B-blend` | Apache 2.0 | 59.41 GB | `172ea6ea91b8` | MLX 4-bit and GGUF builds | None found | Alternative: a merge of two documented Qwen models (15.09.2026) |
| `moonshotai/Kimi-Dev-72B` | MIT | 145.41 GB bf16; Q4 and Q8 GGUF should fit (per-quantisation sizes not checked) | `8791d7981945` | llama.cpp | None in window | Old (06.2025) |

- Excluded: Laguna S 2.1 (OpenMDW 1.1; its NVFP4 MLX build, 71.9 GB, would fit), Kimi K2.7 Code (modified MIT, 595 GB), Devstral 2 123B (licence "other"), Codestral 22B (MNPL), Leanstral 1.5 (Apache, but 120.9 GB bf16 and specific to Lean proofs).

### 1. Autocomplete (fill-in-the-middle)

| Repo | Licence | Size | Commit | Verdict |
|---|---|---|---|---|
| `ByteDance-Seed/Seed-Coder-8B-Base` | MIT | 16.50 GB | `049f843238b4` | Alternative; fill-in-the-middle support not checked; no feedback in window |
| `ByteDance-Seed/Stable-DiffCoder-8B-Instruct` | MIT | 16.50 GB | `10cdaf9b486f` | Experimental: a diffusion code model; Mac runtime not checked |

### 6. Speculative-decoding drafts

| Repo | Licence | Size | Commit | Target |
|---|---|---|---|---|
| `z-lab/Qwen3-Coder-30B-A3B-DFlash` | MIT | 0.95 GB | `98ca0e3e2e6a` | Qwen3-Coder-30B-A3B |
| `JetBrains/Qwen3.8-3.6-27B-blend-DFlash2` | Apache 2.0 | 3.85 GB | `bd647bdeffa4` | The JetBrains blend |
| `ggml-org/Qwen2.5-Coder-1.5B-Q8_0-GGUF` | Apache 2.0 | 1.65 GB | `8be1b8a895a8` | Classic llama.cpp draft for Qwen2.5-Coder; also used for llama-vscode completion |

- Excluded: Laguna XS 2.1 DFlash (OpenMDW 1.1), Laguna S 2.1 DFlash (licence "other").

**Third-party conversions**: MLX and GGUF builds by mlx-community, unsloth and others are not published by the original authors; one declares a licence that differs from the original (Devstral Small 2 GGUF by unsloth). Check them with the method in [`../research-method.md`](../research-method.md#third-party-conversions) before relying on them.
