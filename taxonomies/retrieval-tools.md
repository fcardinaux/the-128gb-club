# Taxonomy of local AI retrieval and RAG tools

Research of 15 November 2026, metadata and user feedback only. Companion of the other files in this folder.
"Covered by documented models?" tells whether the task is already covered by models with a record in [`../model-comparison.md`](../model-comparison.md): Qwen3-Embedding, Qwen3-VL-Embedding, bge-reranker-v2-m3, Qwen3-Reranker, Qwen3-VL-Reranker and four guard models.
"Licence and format pitfalls" assume a strict policy: Apache 2.0 or MIT licences, safetensors or GGUF weights, no gated repository.
Language notes focus on English, French, German and Italian.
**Reddit could not be read**. Licences, gating, sizes and commits come from the Hugging Face API, read on 15.11.2026; commits are the first 12 characters.

## Reference resources

| Resource | Last update | What it covers | Strengths | Weaknesses |
|---|---|---|---|---|
| [MTEB / MMTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) | 14.11.2026 | Embedding models on many tasks and languages: retrieval, reranking, STS | The common reference; filters by language and task | Scores quoted in model cards are self-reported; training-data contamination not controlled |
| [ViDoRe](https://huggingface.co/vidore) | not checked | Retrieval over document images (ColPali family) | The standard for PDF and image retrieval | Mostly English and French |

## Taxonomy

| # | Category → sub-tasks | Typical uses | Covered by documented models? | Licence and format pitfalls |
|---|---|---|---|---|
| 1 | **Dense text embeddings** → multilingual, long context, Matryoshka dimensions | Semantic search, RAG | **Yes** (Qwen3-Embedding) | EmbeddingGemma v1: Gemma licence, gated; Jina v3/v4/v5: CC BY-NC or Qwen research licence |
| 2 | **Multimodal embeddings** → text and image, documents, audio, video | Searching PDFs, photos, video | **Yes** (Qwen3-VL-Embedding) | ColQwen2.5 builds on a research-licence base |
| 3 | **Late interaction (ColBERT, ColPali)** → text multi-vector, document images | Precise retrieval over tables, scans, slides | No | Adapter repositories: the base model's licence decides |
| 4 | **Sparse learned retrieval (SPLADE type)** | Hybrid search with BM25 | No | SPLADE-v3: CC BY-NC-SA, gated, `.bin`; BGE-M3: MIT but no safetensors |
| 5 | **Rerankers** → cross-encoders, LLM rerankers | Second stage of RAG | **Yes** (3 records) | All Jina rerankers CC BY-NC; bge-reranker-v2-gemma builds on Gemma |
| 6 | **Guard stage** → screening retrieved text for prompt injection, filtering output | Between retriever and generator, and on the output | **Yes** (4 guard records) | – |
| 7 | **Runtimes** | – | – | mlx-embeddings code is GPL-3.0; no llama.cpp or MLX support found for EmbeddingGemma 2; Ollama reranking not checked |

## Hacker News comments used

Algolia API, comments only. Window: since 13.05.2026.

- All of Hacker News (49 M items) embedded with EmbeddingGemma 2 on a laptop iGPU at about 200 documents per second ([dmonterocrespo, 29.10.2026](https://news.ycombinator.com/item?id=50290768)).
- Very impressed by EmbeddingGemma 2 ([bbor, 22.10.2026](https://news.ycombinator.com/item?id=50199218)); under-appreciated ([xnx, 13.10.2026](https://news.ycombinator.com/item?id=50071960)); its Apache 2.0 licence noted ([cstever, 13.10.2026](https://news.ycombinator.com/item?id=50070403)).
- The shared audio and text space used for speech-to-text, with caveats on accuracy ([Shershah1024, 13.10.2026](https://news.ycombinator.com/item?id=50071209)).
- Searches with no usable result: Harrier, Granite embedding R2, the small rerankers, ColPali-type models.

## Candidates by category

"Main option" = the best candidate under the strict policy; "Alternative" = also usable; "Flag" = usable only after a check.

### 1. Dense multilingual embeddings

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`google/embeddinggemma-2`** (740M; text, image, audio, video) | Apache 2.0 | 1.49 GB | `f9972ac22e69` | Transformers / sentence-transformers on MPS; llama.cpp and MLX support not found | Positive on HN (see above); context length question ([HF #15](https://huggingface.co/google/embeddinggemma-2/discussions/15), 17.10.2026) | **Main option** (14.09.2026); 100+ languages. Unlike v1, Apache and not gated |
| `microsoft/harrier-oss-v1-0.6b` (also 270m, 27b) | MIT | 1.19 GB (0.54 / 54.02 GB) | `f9b9dc8d367d` | sentence-transformers on MPS | 27b not loadable with sentence-transformers v5 ([HF #3](https://huggingface.co/microsoft/harrier-oss-v1-27b/discussions/3), 06.07.2026) | Alternative; self-reported MTEB v2 multilingual 66.5 / 69.0 / 74.3; 94 languages including fr, de, it |
| `ibm-granite/granite-embedding-311m-multilingual-r2` (also 97m) | Apache 2.0 | 0.62 GB (0.19 GB) | `443995599303` | sentence-transformers; MLX not checked | None | Alternative: small; take only the safetensors (ONNX and `.bin` duplicates) |
| `Snowflake/snowflake-arctic-embed-l-v2.0` | Apache 2.0 | 2.27 GB | `ac6544c8a46e` | sentence-transformers | None in window | Alternative: older multilingual baseline |

Also passing, not detailed: `intfloat/multilingual-e5-large-instruct` (MIT), `nomic-ai/nomic-embed-text-v2-moe` (Apache 2.0), `Octen/Octen-Embedding-8B` (Apache 2.0; base model not checked).

- Excluded: EmbeddingGemma 300m (Gemma licence, gated), Jina embeddings v3 and v5 (CC BY-NC 4.0), Jina v4 (Qwen research licence), BGE-M3 (MIT but `.bin`, `.pt`, ONNX only).

### 2–3. Late interaction and document-image retrieval

| Repo | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| **`nomic-ai/colnomic-embed-multimodal-7b`** | Apache 2.0 (base Qwen2.5-VL-7B: Apache 2.0) | 0.32 GB adapter + 16.58 GB base | `09dbc9502b66` | colpali-engine on MPS (not checked) | **Main option**: licence chain clean |
| `lightonai/GTE-ModernColBERT-v1` | Apache 2.0 | 0.60 GB | `25f6f7bb8237` | PyLate on MPS | Alternative: text, English-focused |
| `vidore/colSmol-500M` | MIT | 0.07 GB adapter | `0aaa9726104c` | PyTorch | Possible: base SmolVLM licence not checked |
| `vidore/colqwen2.5-v0.2` | MIT (adapter) | 0.24 GB | `dcbe8d9cede5` | mlx-embeddings example | **Flag**: its base declares Apache but derives from Qwen2.5-VL-3B (research licence) |

No feedback found in the window for any of these. Excluded: ColNomic 3B (research-licence base), Jina ColBERT v2 (CC BY-NC).

### 4. Sparse retrieval

| Repo | Licence | Size | Commit | Verdict |
|---|---|---|---|---|
| **`opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1`** | Apache 2.0 | 0.67 GB | `1e0f096c2b51` | **Main option**: the only multilingual sparse model found that passes. No feedback |

- Excluded: SPLADE-v3 (CC BY-NC-SA, gated, `.bin`), Splade_PP_en_v2 (`.bin` and ONNX only).

### 5. Small rerankers

Documented: bge-reranker-v2-m3, Qwen3-Reranker, Qwen3-VL-Reranker.

| Repo | Licence | Size | Commit | Feedback | Verdict |
|---|---|---|---|---|---|
| `mixedbread-ai/mxbai-rerank-base-v2` / `-large-v2` | Apache 2.0 | 0.99 / 3.09 GB | `3ea9d4dffa7d` / `ca7e1ee484c3` | sentence-transformers integration merged ([HF #12](https://huggingface.co/mixedbread-ai/mxbai-rerank-large-v2/discussions/12), 08.04.2026) | Alternative: multilingual, Qwen2.5-based |
| `Alibaba-NLP/gte-multilingual-reranker-base` | Apache 2.0 | 0.61 GB | `8215cf04918b` | None | Alternative: multilingual |
| `Alibaba-NLP/gte-reranker-modernbert-base`, `ibm-granite/granite-embedding-reranker-english-r2` | Apache 2.0 | 0.60 GB each | `f7481e605550` / `d09d3d6971b6` | None | English only |

- Excluded: Jina rerankers v2, v3 and m0 (CC BY-NC 4.0), bge-reranker-v2-gemma (Gemma base).

### 7. Runtimes

| Runtime | Licence | Notes |
|---|---|---|
| llama.cpp (`llama-server`) | MIT | Embedding and rerank endpoints with GGUF models |
| Ollama | MIT | `/api/embed`; reranking not checked |
| sentence-transformers | Apache 2.0 | Runs on MPS; the broadest model support |
| mlx-embeddings | GPL-3.0 | Examples for XLM-R, BERT, ModernBERT, Qwen3, Qwen3-VL, ColQwen2.5; not Gemma |

**Third-party conversions**: MLX and GGUF copies of these models are often published by individuals or by an open community organisation. Check them with the method in [`../research-method.md`](../research-method.md#third-party-conversions) before relying on them.
