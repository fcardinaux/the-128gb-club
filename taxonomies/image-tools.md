# Taxonomy of local AI image tools

Research of 13 November 2026, metadata and user feedback only.
"Covered by general models?" tells whether general-purpose models already do the job: image generation and editing models (for example Z-Image-Turbo, FLUX.2 klein, Qwen-Image, Qwen-Image-Edit, Boogu-Image Edit), OCR models and image embeddings.
"Licence and format pitfalls" assume a strict policy: Apache 2.0 or MIT licences, safetensors or GGUF weights.
**Reddit could not be read** (blocked); HN feedback on first-hand local use is thin.

## Reference resources

| Resource | Last update | What it covers | Strengths | Weaknesses |
|---|---|---|---|---|
| [OpenModelDB](https://openmodeldb.info/) ([repo](https://github.com/OpenModelDB/open-model-database)) | commit 08.11.2026 | 672 upscaling and restoration models, tagged by purpose (denoise, deblur, JPEG, debanding, dehalftone, colourisation, inpainting…) and subject (realistic, faces, anime, text…) | Finest-grained, maintained; licence and hashes per model | Classic upscalers and restorers only; mostly `.pth`, community licences (often CC BY-NC-SA) |
| [Spandrel](https://github.com/chaiNNer-org/spandrel) (loader of chaiNNer and ComfyUI) | – | Architectures by task: super-resolution (~30), face restoration, inpainting, denoising, DeJPEG, colourisation, dehazing, low-light | Practical; restrictive architectures kept apart (`spandrel_extra_arches`: CodeFormer, MAT, DDColor, Restormer); loads `.safetensors` | Only what it can load |
| [chaiNNer](https://github.com/chaiNNer-org/chaiNNer) | v0.26.1, 27.10.2026 | Node GUI for upscaling, restoration, batch work | Apple Silicon via PyTorch MPS; good for batches | No category list; ONNX runs on CPU only on a Mac |
| [Hugging Face Tasks](https://huggingface.co/tasks) | – | Official pipeline tags: depth, segmentation, mask generation, image-to-image, detection, keypoints, image-to-3D… | Maps directly to Hub filters | Too coarse for restoration; no matting, quality assessment, vectorisation, culling |
| [Comfy "Complete AI Upscaling Handbook"](https://blog.comfy.org/p/upscaling-in-comfyui) | 06.02.2026 | Upscalers: conservative (SeedVR2, FlashVSR) vs creative (generative), image vs video | Current; the conservative/creative split matters for family photos | Mixes in API services; no licence or Mac notes |
| [IOPaint](https://github.com/Sanster/IOPaint) (formerly lama-cleaner) | archived 13.08.2025 | Erase (LaMa, MAT), diffusion inpainting/outpainting, plugins (SAM, RemoveBG, RealESRGAN, GFPGAN) | Useful practical grouping | Unmaintained: do not adopt as a tool |

Papers with Code shut down in July 2025 (now Hugging Face Trending Papers, without task leaderboards). The "awesome" lists are paper-oriented and mostly not useful for practical choices.

## Taxonomy

| # | Category → sub-tasks | Typical uses | Covered by general models? | Licence and format pitfalls |
|---|---|---|---|---|
| 1 | **Background removal / matting** → salient object, portrait, hair/fur alpha, illustration cut-out | Product and ID photos, stickers, collages | Partly: edit models give no clean alpha and change pixels | BiRefNet MIT (safetensors); RMBG-2.0 CC BY-NC and gated; fine-tunes may change licence; rembg models are ONNX. macOS Photos/Preview already lifts subjects |
| 2 | **Segmentation / object selection** → click/box prompt (SAM-type), text prompt, semantic, video tracking | Exact masks to feed into the edit models | No | SAM 2 Apache 2.0; **SAM 3: custom SAM licence, gated** |
| 3 | **Upscaling / super-resolution** → conservative (ESRGAN family, HAT, DAT, SPAN), creative/diffusion (SUPIR), one-step (SeedVR2, FlashVSR), domain-specific | Print old or small photos, crops | Partly: generation models upscale "creatively" and invent detail | Mostly `.pth` with community licences; Real-ESRGAN code BSD-3; SUPIR non-commercial; SeedVR2 Apache 2.0 |
| 4 | **Restoration** → denoise, deblur, DeJPEG, debanding, dehalftone (scanned prints), dehaze, low-light, scratches, all-in-one | Scanned family photos, phone night shots, old JPEGs | Partly: edit models change faces and content | Same `.pth` and licence issue; several research repos have no licence |
| 5 | **Face restoration** → blind face restoration, identity-preserving face upscaling | Old group photos | Partly, with identity drift | **CodeFormer: S-Lab (non-commercial)**; GFPGAN weights `.pth`, detectors (insightface) non-commercial; high hallucination risk |
| 6 | **Colourisation** → automatic, reference or hint-based | Family archive | Partly (washed-out colours, HN) | DDColor Apache 2.0 but no safetensors; DeOldify MIT but `.pth` |
| 7 | **Inpainting / object removal** → LaMa-type erase, prompt inpainting, watermark/text removal | Tourists, power lines, dust spots | **Mostly yes** (edit models); LaMa keeps the rest pixel-exact | LaMa Apache 2.0 but `.ckpt`/`.pt`; MAT restrictive |
| 8 | **Depth / normal estimation** | Lens blur after the fact, ControlNet, 3D photo effect | No | Depth Anything 3: Small/Base Apache 2.0, Large/Giant CC BY-NC; Apple Depth Pro custom licence |
| 9 | **Image quality assessment / aesthetic scoring** | Pick the best shot, clean the library | No | Many `.pth`, research licences |
| 10 | **Photo culling** (quality + near-duplicates + closed eyes) | Holidays, events | Partly (embeddings for grouping) | Workflow, relies on #9 and #15 |
| 11 | **Vectorisation (raster → SVG)** | Logos for printing, plotter, stickers | No | VTracer MIT (a tool, not a model); Potrace GPL |
| 12 | **Captioning / tagging / alt text** | Search the photo library | Probably yes (vision-language models such as Qwen3-VL) | Florence-2 MIT but `.bin` and custom code; WD taggers anime-oriented |
| 13 | **Outpainting / uncrop** | Change aspect ratio | **Yes** | – |
| 14 | **Style transfer** | Cards, gifts | **Yes** | – |
| 15 | **Relighting / shadow removal** | Harsh shadows, compositing | **Mostly yes** | IC-Light-type depend on SD licences (OpenRAIL) |
| 16 | **Deduplication / similarity** | Clean the library | **Yes** (embeddings) | – |
| 17 | **Face detection / recognition / clustering** | "People" view | No (Apple Photos, Immich) | Privacy-sensitive; InsightFace non-commercial |
| 18 | **Object / open-vocabulary detection** | "Find all bicycles", feed SAM | No | YOLO (Ultralytics) AGPL; Grounding-DINO Apache |
| 19 | **Pose / keypoints** | ControlNet pose | No | DWPose/RTMPose Apache but ONNX/`.pth`; OpenPose non-commercial |
| 20 | **HDR / exposure fusion**, **panorama** | Interiors, landscapes | No | Mostly classical tools (enfuse, Hugin, darktable): not a model search |
| 21 | **AI-image / watermark detection** | "Is this AI-made?" | No | Unreliable, quickly outdated |
| 22 | **OCR / documents** | Receipts, letters | **Yes** | – |
| 23 | **Image-to-3D** (mention) | 3D printing, curiosity | No | Mostly non-commercial licences |
| 24 | **Video: frame interpolation, video upscaling** (mention) | Old home videos, slow motion | No | licences not checked; heavy compute |

**Cross-cutting note**: a strict policy (Apache/MIT, safetensors/GGUF) excludes most of the OpenModelDB/Spandrel ecosystem (`.pth`, CC BY-NC-SA, S-Lab, research licences). Expect short candidate lists per category.

## Hacker News comments used

- Specialised denoising models beat general tools; SCUNet via chaiNNer works well most of the time ([meatmanek, 03.04.2025](https://news.ycombinator.com/item?id=43576101)).
- chaiNNer to run arbitrary models, openmodeldb.info as a good source ([cheald, 03.12.2025](https://news.ycombinator.com/item?id=46140330)).
- rembg CLI for background removal; birefnet for photos, toonout for illustrations ([vunderba, 24.08.2026](https://news.ycombinator.com/item?id=49427056)).
- BiRefNet v2 removes background between parts of the outline better than a newer competitor ([Benjamin_Dobell, 20.11.2025](https://news.ycombinator.com/item?id=45989592)).
- Licence pitfall: a model built on MIT BiRefNet weights released as CC BY-NC, later changed back to MIT ([woadwarrior01, 27.07.2026](https://news.ycombinator.com/item?id=49074829); [not_lain, 28.07.2026](https://news.ycombinator.com/item?id=49080626)).
- Instruction-edit "restoration" (Flux Kontext) reframed the image, invented content and distorted details ([chrismorgan, 11.07.2025](https://news.ycombinator.com/item?id=44531020)).
- General image models colourise only with washed-out, tinted colours ([istjohn, 11.09.2025](https://news.ycombinator.com/item?id=45216680)).
- Uses AI to colourise old black-and-white pictures for a history blog ([strenholme, 06.09.2026](https://news.ycombinator.com/item?id=49586100)).
- VTracer for raster to SVG; its author says it performs badly on some examples ([darvid, 08.02.2026](https://news.ycombinator.com/item?id=46939705); [chris-tsang, 06.04.2025](https://news.ycombinator.com/item?id=43603078)).
- Remacri, a favourite upscaler for photographs, run locally ([enlyth, 06.11.2022](https://news.ycombinator.com/item?id=33492128)); old comment, kept for context.

## Candidates by category

Research of 13 November 2026 (Hugging Face API, HN comments, HF discussions, GitHub issues; Reddit blocked). "Main option" = the best candidate under the strict policy above; "Alternative" = also usable. Commits are the first 12 characters read that day; re-read the full commit when pinning a version.

### 1. Background removal / matting

| Model | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| **`Comfy-Org/BiRefNet`** (BiRefNet general + Lucida v7) | MIT | 1.33 GB, safetensors only | `884af709e9b7` | ComfyUI native "Remove Background" node (since 04.2026) | **Main option.** Reference open model; the author confirms MIT for the weights (HF #23, 04.11.2026). Lucida: illustrations, logos; single developer, regressions reverted |
| `feyninc/FeyNobg` | Apache 2.0 (CC BY-NC until 28.07.2026) | 1.05 GB | `c1fd67fbefe3` | `pip install nobg` | Alternative. Blind test prefers RMBG-2.0; weak hair reported |
| `finegrain/finegrain-box-segmenter` (MVANet) | MIT | 0.19 GB | `9884de4a1db9` | `refiners` library | Alternative. Object inside a drawn box |
| `hustvl/vitmatte-small-composition-1k` | Apache 2.0 | 0.10 GB | `6a58ad764640` | transformers | Alternative. Edge refiner after SAM (needs a trimap) |

- The official `ZhengPeng7/BiRefNet*` repos need `.py` files (trust_remote_code): the Comfy-Org copy avoids them.
- Excluded: RMBG-2.0 / 1.4 (Bria licences, gated), Sapiens2 (own licence), MatAnyone (S-Lab), SDMatte (OpenRAIL), InSPyReNet, S3OD, PDFNet, toonout (MIT but `.pth`/`.pt` only), BEN2 (`.py`, `.pth`, ONNX mixed), feyninc/multimatte (labelled Apache but derived from SAM 3, SAM licence).

### 2. Segmentation / object selection

| Model | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| **`facebook/sam2.1-hiera-large`** | Apache 2.0 | 0.90 GB safetensors (+ `.pt` to leave out) | `665f8e2ad61c` | transformers `Sam2Model` on MPS; ComfyUI via kijai's node (`Kijai/sam2-safetensors`) | **Main option.** Click/box selection; widely used as a main tool (HN 23.06.2026). Upstream Meta has no MPS support (community fork) |
| `facebook/sam2.1-hiera-base-plus` | Apache 2.0 | 0.32 GB | `b7320756a133` | same | Alternative (lighter option) |
| `IDEA-Research/grounding-dino-base` | Apache 2.0 | 0.93 GB | `12bdfa3120f3` | transformers | Alternative. Text → box, then SAM 2.1 for the mask |
| `florence-community/Florence-2-large` | MIT | 1.55 GB | `4271c66b88cd` | transformers, no remote code | Alternative. Text-prompted detection, captions, OCR |
| `yonigozlan/EdgeTAM-hf` | Apache 2.0 | 0.06 GB | `c266ce53b3fc` | transformers | Alternative. Very light |
| `tencent/WeVisOne-VL-4B` | Apache 2.0 | 9.66 GB + `mask_decoder.pt` | `6b44a45873b4` | own package | Too early: text segmentation and matting; `.pt` file, 3 weeks old |

- Excluded: SAM 3 and 3.1 (SAM licence, gated; mirrors keep the licence), SAM3-LiteText (keeps the SAM 3 encoder). ComfyUI's native segmentation node supports only SAM 3: SAM 2.1 needs the custom node.

### 3. Upscaling / super-resolution

| Model | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| **SeedVR2 3B + 7B**, `numz/SeedVR2_comfyUI` (safetensors repack of ByteDance's `.pth`) | Apache 2.0 | 3B fp16 6.78 GB + 7B fp16 16.48 GB + VAE 0.5 GB ≈ 23.8 GB if only these files are taken (repo 60.1 GB in all) | `09ced7102363` | **mflux** (`mflux-upscale-seedvr2`, MLX, native on the Mac); ComfyUI native node (`Comfy-Org/SeedVR2`) | **Main option.** One-step diffusion, no prompt, also restores real-world degradations; community default. MPS bugs in the numz ComfyUI node on an M5 Max 128 GB (issue #600): prefer mflux. 7B-sharp optional (+16.5 GB) |
| `fal/AuraSR-v2` | weights Apache 2.0, pip code CC BY-SA 4.0 | 2.47 GB (+ `.ckpt` to leave out) | `ff452185a7c8` | pip `aura-sr`, ComfyUI node | Alternative. GAN 4x, MPS not verified |
| `caidas/swin2SR-*` | Apache 2.0 | 0.05 GB | `c69ef3e2d2ac` | transformers | Alternative. 2022, soft results |

- The official `ByteDance-Seed/SeedVR2-*` repos are `.pth` only.
- Excluded: Real-ESRGAN (BSD-3-Clause), 4x-UltraSharp (CC BY-NC-SA), OpenModelDB community models (CC BY), HAT/SwinIR/DRCT (`.pth` outside HF), SUPIR (non-commercial), HYPIR (HF says Apache, GitHub says non-commercial), InvSR, DiT4SR, LucidFlux, SD x4 upscaler (licences).

### 4. Restoration (denoise, deblur, damage)

| Model | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| SeedVR2 (see 3) | Apache 2.0 | – | – | mflux | **Main option** (general real-world degradations) |
| **`mlx-community/NAFNet-SIDD-width64`** (denoise) and **`-GoPro-width64`** (deblur) | MIT | 0.46 + 0.27 GB | `3ca8b8711b2f` / `09d01a2c6357` | MLX (`nafnet-mlx` port: no licence, immature) | **Main option.** Niche; no feedback |
| General edit models (Qwen-Image-Edit-2511, Boogu, FLUX.2 klein) | – | – | – | prompt "restore" | Scratches and damage; they may change faces and content (HN 11.07.2025) |

- Excluded or flagged: RealRestorer (HF says Apache, weights reported non-commercial, 41.8 GB), DiffBIR v2 (Apache but `.pth`/`.ckpt`), Bringing-Old-Photos-Back-to-Life (MIT but `.pt`, archived), InstructIR (MIT but `.pt`).

### 5. Face restoration

| Model | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| **`ohayonguy/PMRF_blind_face_image_restoration`** | MIT | 0.92 GB safetensors | `67e0aa382ab4` | PMRF GitHub code (MIT); ComfyUI-PMRF node is **AGPL** | **Main option.** ICLR 2025; MPS not verified; no feedback |
| **`mlx-community/RestoreFormerPlusPlus-fp32`** | Apache 2.0 | 0.29 GB | `9870c2e38502` | Swift `mlx-restoreformer-swift` only | **Main option.** Apple-native; niche |

- Excluded: CodeFormer (S-Lab, non-commercial; an "MIT" mirror is mislabelled), GFPGAN (weights `.pth` on GitHub, no safetensors on HF; detectors non-commercial).
- Risk for every face model: identity drift on old family photos.

### 6. Colourisation

| Model | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| **`prithivMLmods/QIE-2511-BW2TrueColor`** (LoRA for Qwen-Image-Edit-2511) | Apache 2.0 | 0.24 GB needed (`QIE-2511-BW2TrueColor-3000.safetensors`; repo 1.18 GB with training checkpoints) | `f5bc5dca0422` | ComfyUI (MPS), diffusers; mflux compatibility unverified | **Main option.** Trigger "Transform Black and White into True Colors". Untested by the community. Regenerates the whole image: keep only its colours and recombine with the original lightness (Lab) so faces and details stay intact |
| Edit models by prompt (Qwen-Image-Edit-2511, Boogu, FLUX.2 klein) | – | – | – | – | Fallback; washed-out, tinted colours (HN 11.09.2025) |

- Excluded: DDColor (Apache but `.bin`/`.pth`/ONNX/CoreML only, no safetensors anywhere), DeOldify (`.pth`, archived), KoalaNation and AlekseyCalvin colourisers (FLUX.1 Kontext dev, non-commercial), FLUX.2 klein **9B** colourisation LoRAs (klein 9B non-commercial, gated), ColorizeNet (`.ckpt`, OpenRAIL), LTX IC-LoRAs (video, own licence).

### 7. Pixel-exact object removal

| Model | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| **`michaelgold/big-lama`** | tag MIT, upstream LaMa Apache 2.0 (both allowed; relabel unexplained) | 0.20 GB | `98ab7cface89` | Spandrel (MIT), comfyui-inpaint-nodes (GPL), chaiNNer; key compatibility untested | **Main option.** Only licensed safetensors conversion of Big-LaMa; mask in, rest of the image identical; still the lightweight reference but a few years old |
| **`prithivMLmods/Qwen-Image-Edit-2511-Object-Remover`** (LoRA) | Apache 2.0 | 0.24 GB | `3d92218a37c0` | ComfyUI, diffusers | **Main option.** Better realism, 4 steps; regenerates the whole image, so composite back with the mask. Liked at launch |
| `slopshop/erase-v1` (FLUX.2 klein 4B LoRA) | Apache 2.0 | 0.20 GB | `0bb45298a0f4` | custom pipeline | Alternative. Mask-based, removes shadows and reflections; no ComfyUI/mflux recipe, no feedback |
| `prithivMLmods/QIE-2511-Object-Remover-v2`, `-Bbox-v3` | Apache 2.0 | 0.24 GB needed | `f3782a831cd5`, `a02272161eac` | ComfyUI | Alternative. Bbox-v3 weak with many boxes |

- Not recommended: Moebius (hustvl, ECCV 2026, 0.22B): `.bin` only, 512 px, mostly negative real-world feedback (HN 22.06.2026, HF #3).
- Excluded: LaMa originals (`.ckpt`/`.pt`), LaMa ONNX/CoreML copies, unlicensed safetensors copies, fal and xocialize klein object-remove LoRAs (file reported corrupt), MI-GAN (no safetensors), MAT (restrictive), Flux Fill removal LoRAs (FLUX.1 dev non-commercial), Qwen-Image-2.1 remover (qwen-research base).
- HN (22.06.2026): for local inpainting, FLUX.2 klein and Qwen-Edit are good, Boogu very good.

### 9. Image quality assessment / aesthetic scoring

Only VLM-based models pass; a 7B VLM takes a few seconds per image (fine for bursts, slow for a whole library).

| Model | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| **`TianheWu/VisualQuality-R1-7B`** | HF MIT, GitHub Apache 2.0 | 16.6 GB (+ `training_args.bin`, a pickle file, not needed) | `12852ce5718d` | mlx-vlm (mlx-community 4/6/8-bit), llama.cpp GGUF | **Main option.** NeurIPS 2025 spotlight; most mature; no user reports |
| **`ByteDance/EvoQuality`** | Apache 2.0 | 16.6 GB | `ea11986a5d93` | transformers MPS; MLX 8-bit (usermma), GGUF | **Main option.** ICLR 2026; 1–5 score and pairwise comparison; no user reports |
| **`ByteDance/Q-Insight`** | Apache 2.0 | 16.6 GB (`score_degradation/` only; repo 86 GB with `.pt`/`.pkl`/`.bin`) | `8dc8e4c3c119` | transformers MPS | **Main option.** Also explains degradations; take only `score_degradation/`; no user reports |
| `mlx-community/SigLIP2-NR-IQA-KonIQ` | Apache 2.0 | 5 MB + 4.5 GB backbone | `8349820ad6cf` | MLX, package unclear | Alternative. Fast first pass, unofficial reproduction |

- Excluded: pyiqa (PolyForm Noncommercial code, CC BY-NC-SA `.pth` weights: MUSIQ, MANIQA, TOPIQ, CLIP-IQA+, NIMA), Q-Align (S-Lab on GitHub), DeQA-Score (custom code, Llama-2 base), QualiCLIP (CC BY-NC), LAION and improved aesthetic predictors (`.pth` only), aesthetic-predictor-v2.5 (AGPL), anime aesthetic models, UniPercept (gated).
- HN (21.05.2026): a user culled 4,487 photos with NIMA + LAION + MUSIQ; it spared the bottom 80 %, but the models disagreed strongly on some shots.

### 11. Vectorisation (raster → SVG)

No AI model passes the strict policy; the useful options are ordinary tools.

| Tool | Licence | Install | Verdict |
|---|---|---|---|
| **VTracer** | MIT | `pip install vtracer` or `cargo install vtracer-cli` (not in Homebrew) | **Main option.** Colour images, logos, illustrations; the practical standard on HN; reduce colours first, finish by hand |
| Potrace | GPL-2.0+ | `brew install potrace` | Alternative. Black-and-white line art only (Inkscape Trace) |

- Excluded models: StarVector (custom code, StarCoder OpenRAIL base, 1B gated), OmniSVG (`.bin` only, 4B on a qwen-research base, brittle per HF users), dots.mocr-svg (extra licence agreement, custom code), LLM4SVG (no weights).

**Third-party conversions**: SeedVR2 (`numz`), NAFNet ×2 and RestoreFormer++ (`mlx-community`) and big-lama (`michaelgold`) are conversions published by individuals or an open community organisation, not by the original authors; their checks are in each model record (`provenance`), see [`../research-method.md`](../research-method.md#third-party-conversions).
