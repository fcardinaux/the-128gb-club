# Taxonomy of local AI document tools

Research of 15 November 2026, metadata and user feedback only. Companion of `image-tools.md`, `music-tools.md` and `speech-tools.md`.
"Covered by documented models?" tells whether the task is already covered by models with a record in [`../model-comparison.md`](../model-comparison.md#ocr): Chandra OCR 2, DeepSeek-OCR 2, dots.ocr, GLM-OCR, Granite-Docling, Infinity-Parser2-Flash, MinerU-4 pipeline models, MinerU2.5-Pro, olmOCR-2, PaddleOCR-VL, PP-DocLayoutV3, Qianfan-OCR and Unlimited-OCR-2.
"Licence and format pitfalls" assume a strict policy: Apache 2.0 or MIT licences, safetensors or GGUF weights, no gated repository.
Language notes focus on English, French, German and Italian.
**Reddit could not be read**. Licences, gating, sizes and commits come from the Hugging Face API, read on 15.11.2026; sizes are the whole repository (several quantisations may be included); commits are the first 12 characters.

## Reference resources

| Resource | Last update | What it covers | Strengths | Weaknesses |
|---|---|---|---|---|
| [OmniDocBench](https://github.com/opendatalab/OmniDocBench) | v1.7 on 30.04.2026; repo 12.11.2026 | 1,651 PDF pages, 10 document types (handwritten notes included); text, formulas, tables, reading order | The most cited parsing benchmark; scores per component | English and Chinese only; versions not comparable; run by the MinerU team; top scores near saturation |
| [olmOCR-Bench](https://huggingface.co/datasets/allenai/olmOCR-bench) | 19.02.2026 | Pass/fail unit tests: text, order, tables, math, old scans, headers | Model-agnostic; community scores per model on Hugging Face | Mostly English; some vendors dismiss it ([HN](https://news.ycombinator.com/item?id=48647449), themanmaran, 23.06.2026) |
| [OCRBench v2](https://github.com/Yuliang-Liu/MultimodalOCR) | 09.11.2026 | OCR tasks for multimodal LLMs: spotting, key-information extraction, VQA | Wide task coverage | Aimed at general VLMs, not page-to-Markdown |
| [ParseBench](https://github.com/run-llama/ParseBench) | v2 on 29.10.2026; repo 15.11.2026 | 4,317 cases in six dimensions, including forms and charts | Weights errors by severity (changed number, flipped negation) | Run by LlamaIndex, whose own parser ranks first; mostly English business documents |
| [OmniParseBench](https://huggingface.co/datasets/datalab-to/omni_parse_bench) | 04.11.2026 | Parsing, with handwriting tests | Recent | Run by Datalab, which sells Surya, marker and Chandra |
| OCR Arena (ocrarena.ai) | not checked | Pairwise human votes | Human preference | Lags behind new models ([HN](https://news.ycombinator.com/item?id=49336738), my002, 17.08.2026) |
| [davanstrien/ocr-bench](https://github.com/davanstrien/ocr-bench) | 11.11.2026 | Leaderboards per collection, judged by a VLM; old scans | Historical material; transparent | One person's project; VLM judge |
| [CATMuS medieval](https://huggingface.co/datasets/CATMuS/medieval) | 11.03.2025 | Medieval Latin-script handwriting, several languages | De facto test set for medieval HTR | Medieval only |
| [HTR-United](https://github.com/HTR-United/htr-united) | 08.11.2026 | Catalogue of handwriting ground-truth datasets, many in French | Best entry point for FR/DE/IT historical data | A catalogue, not a leaderboard |
| [AWESOME-OCR-LLM](https://github.com/Yuliang-Liu/AWESOME-OCR-LLM) | 11.11.2026 | Links on LLM-era OCR | Current | A link list; older awesome lists are stale |

## Taxonomy

| # | Category → sub-tasks | Typical uses | Covered by documented models? | Licence and format pitfalls |
|---|---|---|---|---|
| 1 | **Page OCR and parsing** → PDF or image to Markdown, reading order | Searchable archives, feeding documents to an LLM | **Yes** (13 records) | Surya, marker and Chandra weights: OpenRAIL; several VLM OCR models build on a research-licence base |
| 2 | **Handwriting recognition (HTR)** → modern, historical (Kurrent, medieval), line or page level | Letters, archives, family records | Partly (VLM OCR records claim handwriting) | Most historical models are `.ckpt` (PyLaia), `.mlmodel` (kraken) or `.bin`; the best page-level Kurrent model is CC BY-SA |
| 3 | **Table structure recognition** | Spreadsheets from PDFs, invoices | Partly (page VLMs output HTML tables) | Surya table model CC BY-NC-SA; NVIDIA table model `.pth`; TableFormer V1 licence unclear |
| 4 | **Formula recognition (LaTeX OCR)** | Scientific papers, course notes | Partly (page VLMs) | UniMERNet `.pth`; texify CC BY-SA or CC BY-NC-SA; pix2tex `.pth`; handwritten math models non-commercial |
| 5 | **Layout analysis** → regions, reading order, line segmentation | First stage of pipelines; HTR line finding | **Yes** (PP-DocLayoutV3) | DocLayout-YOLO: AGPL code and `.pt`; LayoutLMv3 CC BY-NC-SA; kraken segmenter `.mlmodel` |
| 6 | **Key-information extraction and document Q&A** → fields to JSON, forms, charts | Invoices, bank statements, receipts | No | Donut and Pix2Struct `.bin`; LayoutLM CC BY-NC-SA; some fine-tunes declare MIT on a research-licence base |
| 7 | **Pipelines and classical OCR** | Batch conversion, searchable PDFs | Partly (MinerU) | Pipeline code is often permissive while its default models are not (marker, MinerU) |

**Cross-cutting notes**:
- **Line segmentation is a gap** under the strict format policy: the line-level HTR models need a segmenter, and the only dedicated one (kraken) uses `.mlmodel`. Page-level VLMs avoid the problem.
- No independent character error rate was found for French, German or Italian handwriting with the new general models; only the historical models' cards give numbers. No dedicated Italian handwriting model was found.
- On a Mac, Apple's built-in Vision OCR is a strong, free baseline for printed text ([HN](https://news.ycombinator.com/item?id=49953995), postalcoder, 04.10.2026; [HN](https://news.ycombinator.com/item?id=49999502), treetalker, 07.10.2026).

## Hacker News comments used

Algolia API, comments only. Window: since 13.05.2026.

- Docling converted a rulebook with wild graphic design very well ([Schlagbohrer, 20.07.2026](https://news.ycombinator.com/item?id=48976812)); Docling gave "garbage", possibly misused, marker with `--force-ocr` was best ([ljouhet, 23.06.2026](https://news.ycombinator.com/item?id=48644377)).
- NuExtract much better than Tesseract or a generic VLM for bank statements ([ad_fontes, 13.08.2026](https://news.ycombinator.com/item?id=49290410)).
- Good experiences with MinerU and PaddleOCR-VL ([dcan, 14.08.2026](https://news.ycombinator.com/item?id=49298968)); MinerU too heavy for consumer PCs ([nick_jonas, 14.05.2026](https://news.ycombinator.com/item?id=48133090)).
- PaddleOCR in production offline on CPU ([\_\_rito\_\_, 23.06.2026](https://news.ycombinator.com/item?id=48648011)); about 95 % on single lines ([darepublic, 04.10.2026](https://news.ycombinator.com/item?id=49956215)); PaddleOCR-VL 8-bit MLX on a Mac ([dandaka, 21.08.2026](https://news.ycombinator.com/item?id=49387167)); an unverified claim that some Paddle models derive from non-commercial models, "a few years outdated" in the commenter's words ([Phemist, 04.09.2026](https://news.ycombinator.com/item?id=49567246)).
- Tesseract much worse than PaddleOCR or Surya/marker ([v3ss0n, 14.08.2026](https://news.ycombinator.com/item?id=49293634)); OCRmyPDF is the right tool for searchable text only ([Null3351, 04.11.2026](https://news.ycombinator.com/item?id=50365700)).
- Chandra most accurate in one test, GLM-OCR close; PaddleOCR, dots.ocr and DeepSeek-OCR worse ([phenomen, 24.08.2026](https://news.ycombinator.com/item?id=49421088)).
- GLM-OCR good on difficult handwriting ([vinaigrette, 01.07.2026](https://news.ycombinator.com/item?id=48750605)); vision LLMs handle cursive and old handwriting well ([wongarsu, 23.06.2026](https://news.ycombinator.com/item?id=48644188)); accurate OCR of bad handwriting not yet practical locally ([jiggawatts, 02.10.2026](https://news.ycombinator.com/item?id=49933305)); a top hosted model reads 19th-century gothic handwriting but is expensive ([vintermann, 29.10.2026](https://news.ycombinator.com/item?id=50288674)).
- Transkribus (proprietary, hosted) recommended for old letters ([thadt, 23.06.2026](https://news.ycombinator.com/item?id=48648355); [forinti, 27.08.2026](https://news.ycombinator.com/item?id=49468190)) and old Swedish records ([jnurmine, 04.07.2026](https://news.ycombinator.com/item?id=48783460)).
- No single benchmark settles the choice ([aliljet, 23.06.2026](https://news.ycombinator.com/item?id=48646583)).
- granite-vision-4.1-4B cited as a small local model ([adrian_b, 17.06.2026](https://news.ycombinator.com/item?id=48568714)).
- Searches with no usable result: LightOnOCR, MiniCPM-OCR, TrOCR, kraken, eScriptorium, TableFormer, Table Transformer, LaTeX OCR tools.

## Candidates by category

"Main option" = the best candidate under the strict policy; "Alternative" = also usable; "Flag" = usable only after a check. Already documented models are in [`../model-comparison.md`](../model-comparison.md#ocr) and not repeated here.

### 1. Page OCR and parsing: new general models

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`lightonai/LightOnOCR-3-4B`** (also 1B and 0.8B) | Apache 2.0 | 9.11 GB (1B: 2.02 GB) | `b71010f095dc` (1B: `23d544085c88`) | Transformers (MPS); GGUF by a third party (Apache, matches); 1B: mlx-community 4- and 8-bit | Best for regional languages per one user ([HF #1](https://huggingface.co/lightonai/LightOnOCR-3-4B/discussions/1), 09.10.2026); 1B checkpoint flagged "corrupted" by Transformers, `key_mapping` workaround ([HF #1](https://huggingface.co/lightonai/LightOnOCR-3-1B/discussions/1), 27–28.10.2026); garbled output on Apple Metal fixed in llama.cpp on 20.08.2026 ([#25652](https://github.com/ggml-org/llama.cpp/issues/25652)); code regions lose content in Docling ([#5221](https://github.com/docling-project/docling/issues/5221), 06.11.2026) | **Main option** (released 06–07.10.2026). Card claims handwriting, forms, receipts. Use a llama.cpp build after 20.08.2026. mlx-vlm support not checked |
| `openbmb/MiniCPM-OCR-1.0` (1.3B) | Apache 2.0 | 2.62 GB (official GGUF 8.23 GB) | `883ca368d173` | llama.cpp, Ollama; full parsing via an SDK that adds PP-DocLayoutV3 | Only integration requests so far; **thin** | Alternative (released 21.10.2026); main languages Chinese and English |
| PP-OCRv6 (PaddleOCR) | Apache 2.0 | – | – | PaddleOCR; official `_safetensors` variants | See PaddleOCR in section 7 | Alternative: classical detection and recognition, fast on CPU |

- Excluded: Surya OCR 2.5 and Indra OCR (OpenRAIL-M), Nanonets-OCR2-3B (no licence; research-licence base).
- Not checked: OXR, TeleOCR, HunyuanOCR-1.5 (seen in the [PicoDocs #80](https://github.com/PicoMLX/PicoDocs/issues/80) plan, 24.10.2026, which compares October 2026 OCR models with Apple Vision).

### 2. Handwriting recognition

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **LightOnOCR-3-4B, MiniCPM-OCR-1.0** (see 1) | Apache 2.0 | – | – | – | No CER for FR/DE/IT handwriting found | **Main option** for modern hands, page level. MiniCPM-OCR ships a tutorial for fine-tuning on French handwritten lines |
| `dh-unibe/trocr-kurrent` (TrOCR base) | MIT | 1.34 GB safetensors (repo 2.68 GB) | `2882072ac68f` | Transformers (MPS); needs line segmentation | None in window | Alternative: German Kurrent, 19th c.; card CER 2.66 %. Take only the safetensors file |
| `dh-unibe/trocr-german-kurrent-xvi-xix-from-kurrent-v2` | MIT | 1.34 GB | `bd1d96b67225` | Same | None found | Alternative: German, 16th–19th c. Not reviewed in detail |
| `dh-unibe/qwen3.5-4b-german-xix-v2` (LoRA on Qwen3.5-4B) | MIT | 0.36 GB | `a08ce348a063` | Merge into the base first; MLX or GGUF after merging not checked | None | **Flag**: line level, adapter. Card CER 6.80 % on 19th-century Swiss Federal Council minutes, against 11.18 % for a kraken model |
| `magistermilitum/tridis_v2_HTR_historical_manuscripts` (TrOCR large) | MIT | 2.30 GB safetensors (repo 6.82 GB) | `a9893de9921c` | Transformers (MPS); line level | None in window | Alternative: Latin, Old French, Old Spanish, 11th–16th c. Take only the safetensors file |
| `LaMOP/TrOCR_Manicule_2026_Latin_Medieval` | MIT | 1.34 GB | `08e146d2dbf4` | Transformers | None found | Possible: medieval Latin. Not reviewed |
| `microsoft/trocr-base-handwritten` | MIT | 2.67 GB | `eaacaf452b06` | Transformers | Trained on English only | Baseline for modern English |

- Excluded: `b-straub/LightOnOCR-3-1B-Historic-German-Handwriting` (CC BY-SA 4.0; otherwise the most relevant page-level Kurrent model, about 30 s per page with llama.cpp on an M3), kraken models (MIT but `.mlmodel`), Teklia PyLaia models (MIT but `.ckpt`), TrOCR German handwritten (AFL-3.0), French TrOCR large (MIT but `.bin`), Finnish/Swedish multicentury model (Apache but `.bin`), Qwen3-VL-8B CATMuS fine-tune (no licence), Qwen3.8-Flash-Next HTR fine-tune (Qwen community licence, 530 GB).
- Passes the policy but out of the language focus: Riksarkivet TrOCR (Swedish).

### 3. Table structure recognition

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`PaddlePaddle/SLANeXt_wired_safetensors`** (wireless variant also) | Apache 2.0 | 0.18 GB | `d97b77b50789` | Transformers `AutoModelForTableRecognition`; MPS not checked | None found | **Main option** (standalone) |
| `docling-project/TableFormerV2` | Apache 2.0 | 0.21 GB | `e41ba5da7ef6` | Docling (MPS) | "Preview"; duplicates multi-page tables where V1 stays clean ([#3553](https://github.com/docling-project/docling/issues/3553), 05.06.2026); card and licence added only after a request ([HF #3](https://huggingface.co/docling-project/TableFormerV2/discussions/3), 20.08.2026) | Alternative (preview) |
| `PaddlePaddle/SLANet_plus_safetensors` | Apache 2.0 | 0.007 GB | `e44d12b3fe69` | PaddleOCR or Transformers (not checked) | None found | Alternative: lightweight |
| `microsoft/table-transformer-structure-recognition-v1.1-all` | MIT | 0.12 GB | `7587a7ef111d` | Transformers (MPS) | Code repository archived | Alternative: older baseline |
| `docling-project/docling-models` (TableFormer V1) | CDLA-Permissive-2.0 and Apache 2.0 both listed | 0.36 GB | `2199320848bb` | Docling | Degenerate output and dropped rows reported as a regression ([#4255](https://github.com/docling-project/docling/issues/4255), 17.09.2026) | **Flag**: which licence applies is unclear |

- Excluded: Surya table model (CC BY-NC-SA 4.0), NVIDIA Nemotron table structure (NVIDIA licence, `.pth`). Not reviewed: pix2text table model (MIT, safetensors).
- Page-level VLMs (section 1 and the documented OCR records) output HTML tables directly.

### 4. Formula recognition

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`PaddlePaddle/PP-FormulaNet_plus-L_safetensors`** | Apache 2.0 | 0.73 GB | `6cc004a8e91e` | PaddleOCR or Transformers; card nearly empty, runtime not checked | None found | **Main option** (standalone) |
| `MixTex/ZhEn-Latex-OCR` | Apache 2.0 | 0.42 GB | `37da0497956a` | Transformers (not checked) | None found | Possible: old, not reviewed |
| LightOnOCR-3, MiniCPM-OCR-1.0, NuExtract3 | Apache 2.0 | – | – | – | No formula-specific feedback | Page-level alternatives |

- Excluded: UniMERNet (Apache but `.pth`; used inside MinerU), texify (CC BY-SA or CC BY-NC-SA), pix2text formula models (MIT but ONNX), pix2tex (`.pth`), Docling CodeFormulaV2 (CDLA-Permissive-2.0, not in the strict list), FormulaNet by alephpi (AGPL-3.0), handwritten math models (CC BY-NC-SA, AFL-3.0).

### 5. Layout analysis

Documented: PP-DocLayoutV3.

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`docling-project/docling-layout-heron`** (RT-DETRv2) | Apache 2.0 | 0.17 GB | `8f39ad3c0b4c` | Docling (MPS); MLX bf16 by mlx-community (Apache, matches) | Discussions from 2025 only; indirect via Docling comments | **Main option** (Docling default) |
| `docling-project/docling-layout-heron-101`, `-egret-xlarge` | Apache 2.0 | 0.31 / 0.25 GB | `2e4993cf6bb2` / `23857d16596e` | Docling | None found | Alternatives |
| `PaddlePaddle/PP-DocLayout_plus-L_safetensors` | Apache 2.0 | 0.13 GB | `325ea4e609e2` | Transformers | None found | Alternative |
| `Aryn/deformable-detr-DocLayNet` | Apache 2.0 | 0.17 GB | `d5503a90ae08` | Transformers | None found | Possible: older |

- Excluded: DocLayout-YOLO (AGPL code, `.pt` weights, one repo with no licence), Surya layout (OpenRAIL, `.pth`), LayoutLMv3 (CC BY-NC-SA). Flagged: kraken line segmenter (Apache, `.mlmodel`).

### 6. Key-information extraction and document Q&A

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`numind/NuExtract3`** (4B, on Qwen3.5-4B) | Apache 2.0 | 9.34 GB (official GGUF 19.08 GB) | `c99dc8f5641b` | llama.cpp (official GGUF); the mlx-community bf16 copy declares no licence | Better than Tesseract or a generic VLM on bank statements (HN 13.08.2026); leads the "present" sub-score on olmOCR-Bench old scans ([HF #3](https://huggingface.co/numind/NuExtract3/discussions/3), 29.06.2026) | **Main option**: JSON template in, JSON out; also Markdown |
| `ibm-granite/granite-vision-4.1-4b` | Apache 2.0 | 8.01 GB (official GGUF 18.92 GB) | `37d591f06319` | llama.cpp | Cited as a small local model (HN 17.06.2026); task tags fail with a non-standard image placeholder ([HF #7](https://huggingface.co/ibm-granite/granite-vision-4.1-4b/discussions/7), 15.11.2026); **thin** | Alternative: forms, charts, document Q&A |
| `ibm-granite/granite-vision-3.3-2b-chart2csv-preview` | Apache 2.0 | 6.16 GB | `298ed4d87126` | Transformers; IBM GGUF | None found | Niche: chart to CSV |
| `numind/NuExtract-2.0-8B` | MIT | 16.60 GB | `a470f0b5dd0b` | Transformers; numind GGUF | None in window | Superseded by NuExtract3 |

- Excluded: NuExtract-2.0-4B (declares MIT, but its base Qwen2.5-VL-3B has a research licence), Donut and Pix2Struct (`.bin`, 2022), LayoutLM invoices and LayoutLMv3 (CC BY-NC-SA), Florence-2 DocVQA (no licence), Datalab lift (OpenRAIL).

### 7. Pipelines and classical OCR

| Tool | Licence (code / default models) | Mac support | Feedback | Verdict |
|---|---|---|---|---|
| **Docling** 2.150.1 (14.11.2026) | MIT / heron and TableFormerV2 Apache 2.0; TableFormer V1 unclear; CodeFormulaV2 CDLA-P-2.0 | macOS arm64; OCR through Apple Vision (ocrmac); MLX engine requested ([#4932](https://github.com/docling-project/docling/issues/4932)) | Mixed (HN 20.07 and 23.06.2026); table regressions [#5136](https://github.com/docling-project/docling/issues/5136), [#5237](https://github.com/docling-project/docling/issues/5237) (November 2026); on macOS, ocrmac text intermittently missing with no warning ([#5207](https://github.com/docling-project/docling/issues/5207), 06.11.2026) | **Main option**. Pin the version; check the models it loads |
| PaddleOCR 3.7.0 (11.06.2026) | Apache 2.0 / Apache 2.0, with official `_safetensors` variants | CPU on macOS; README cites a 6.1× speed-up on M4 for PP-OCRv6 tiny | Positive in production (HN, see above) | Alternative: use the safetensors variants |
| Tesseract 5.5.4 and OCRmyPDF 17.14.1 | Apache 2.0, MPL-2.0 | Homebrew; an OCRmyPDF plugin uses Apple Vision | The right tool for searchable PDFs (HN 04.11.2026) | **Classical baseline** |
| kraken 7.1, with eScriptorium | Apache 2.0 / models of various licences, `.mlmodel` | Linux and macOS | None found on HN | Tool fine; models flagged for format |
| MinerU 4.2.2 (13.11.2026) | Apache 2.0 with extra terms (commercial licence above a size threshold; attribution for online services) | Apple silicon tier (PyTorch MPS plus llama.cpp) | Text detection forced to CPU on MPS, about 12× slower ([#5632](https://github.com/opendatalab/MinerU/issues/5632), closed); swaps chemical symbols in formulas ([#5646](https://github.com/opendatalab/MinerU/issues/5646), 16.10.2026) | **Flag**: not plain Apache 2.0; some pipeline models are `.pth` |
| marker 2.2.0 and Surya | Apache 2.0 / OpenRAIL-M weights (free below a revenue threshold) | llama.cpp on Apple silicon; MLX experimental | Best for long complex documents (HN 23.06.2026); balanced mode invented 58 words on a bleed-through page ([#1081](https://github.com/datalab-to/marker/issues/1081), 16.08.2026) | Excluded by the weights licence |
| olmOCR toolkit 0.4.27 | Apache 2.0 | Needs an NVIDIA GPU (vLLM); no Mac path documented | – | Not for a Mac (the olmOCR-2 model itself is documented) |

**Third-party conversions**: the mlx-community, prithivMLmods and atkinschang repositories are conversions published by individuals or an open community organisation, not by the original authors. Some declare no licence (mlx-community NuExtract3, atkinschang TableFormerV2-MLX), and one 8-bit MLX copy of LightOnOCR-3-1B reports a size larger than the bf16 original (7.14 GB), unexplained. Check them with the method in [`../research-method.md`](../research-method.md#third-party-conversions) before relying on them.
