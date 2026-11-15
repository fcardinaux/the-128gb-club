# Taxonomy of local AI vision and 3D tools

Research of 15 November 2026, metadata and user feedback only. Companion of the other files in this folder; image editing, upscaling and background removal are in [`image-tools.md`](image-tools.md).
"Covered by documented models?" tells whether the task is already covered by models with a record in [`../model-comparison.md`](../model-comparison.md#image-understanding): Qwen3-VL-30B-A3B, Qwen3.6 and Qwen3.8-27B (built-in vision), Gemma 4, Falcon Perception, SAM 2.1, MoGe-3, MapAnything (Apache variant) and SenseNova-SI-1.3.
"Licence and format pitfalls" assume a strict policy: Apache 2.0 or MIT licences, safetensors or GGUF weights, no gated repository.
**Reddit could not be read**. Licences, gating, sizes and commits come from the Hugging Face API, read on 15.11.2026; commits are the first 12 characters. Mac runtime support is as documented or reported, not tested.

## Reference resources

| Resource | Last update | What it covers | Strengths | Weaknesses |
|---|---|---|---|---|
| [OpenCompass Open VLM Leaderboard](https://huggingface.co/spaces/opencompass/open_vlm_leaderboard) | Space code 11.03.2026; data refresh not checked | Image VLMs on many benchmarks | Broadest open-VLM table; reproducible | May lag 2026 releases; no Mac speed or memory |
| [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) | 13.11.2026 | The toolkit behind that leaderboard | Very active; run your own evaluations | A tool, not a ranking |
| [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) | 15.11.2026 | Image, video and audio evaluation | Strong on video | Licence not checked |
| [OpenCompass video leaderboard](https://huggingface.co/spaces/opencompass/openvlm_video_leaderboard) | 21.11.2024 | Video VLMs | The only open video-VLM table | **Stale** |
| [3D Arena](https://huggingface.co/spaces/dylanebert/3d-arena) | 26.10.2026 | Human votes on image-to-3D generators | The only arena for 3D generation | Vote counts not checked |
| [awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) | 04.10.2026 | Splatting papers and tools | Comprehensive, curated | Research-centred |
| [vismatch](https://github.com/gmberton/vismatch) | 12.11.2026 | One wrapper for about 50 feature matchers | One API | Each weight keeps its own licence (SuperPoint is non-commercial) |

No maintained depth-estimation leaderboard was found.

## Taxonomy

| # | Category → sub-tasks | Typical uses | Covered by documented models? | Licence and format pitfalls |
|---|---|---|---|---|
| 1 | **Vision-language models** → captioning, visual Q&A, charts, screenshots, multi-image, video understanding | Photo captions and search, accessibility descriptions, UI agents, video summaries | **Yes** (Qwen3-VL, Qwen3.6, Qwen3.8, Gemma 4) | Gemma 3: Gemma licence, gated (Gemma 4 is Apache); LFM2.5-VL: LFM licence; Moondream 3: "other"; many repositories ship custom Python code |
| 2 | **Detection** → closed-set real-time, open-vocabulary (text to boxes), grounding, pointing and counting | Inventory counts, wildlife camera triage, data labelling | Partly (Falcon Perception) | Ultralytics YOLO: AGPL-3.0 and `.pt`; RF-DETR XL, 2XL and NAS: PML 1.0 (Nano to Large are Apache) |
| 3 | **Segmentation** → semantic, instance, panoptic; promptable; text-prompted; video object tracking | Cut-outs, land-use maps, microscopy pre-labelling, video rotoscoping | **Yes** (SAM 2.1, Falcon Perception) | SAM 3 and 3.1: gated, SAM licence; DINOv3: gated; Mask2Former "other" and `.bin`; SegFormer NVIDIA licence |
| 4 | **Depth estimation** → relative, metric, video-consistent, LiDAR-prompted | Photo refocus, AR occlusion, 3D photos, measuring | **Yes** (MoGe-3) | Licence varies by size: Depth Anything V2 Base/Large and DA3 Large/Giant are CC BY-NC; Depth Pro: Apple licence; UniDepth CC BY-NC; Marigold v1-1 OpenRAIL++ |
| 5 | **Surface normals and intrinsic decomposition** (albedo, shading) | Relighting, material capture, VFX | Partly (MoGe-3 normals) | DSINE: custom licence; Marigold v1-1 normals and IID: OpenRAIL++ |
| 6 | **Multi-view reconstruction, cameras, matching** → feed-forward point maps, SfM/MVS | Photogrammetry, drone mapping, camera tracking | **Yes** (MapAnything) | DUSt3R, MASt3R, CUT3R: CC BY-NC-SA; VGGT: CC BY-NC or gated; Pi3: BSD-2 (not in the strict list); Fast3R: FAIR non-commercial |
| 7 | **Gaussian splatting and NeRF** (tools) | Virtual tours, heritage capture, scene capture | No | Original INRIA 3DGS non-commercial; OpenSplat AGPL; gsplat CUDA only |
| 8 | **Image-to-3D generation** → shape, texture, parts, scenes | Game assets, 3D-print prototypes, product previews | No | Hunyuan3D excludes the EU, UK and South Korea; Stability 3D models gated; hidden gated dependencies (DINOv3, RMBG-2.0); mostly CUDA |
| 9 | **Pose and point tracking** → 2D keypoints, 3D body mesh, 6-DoF object pose, point tracking | Sports analysis, ergonomics, motion capture, VFX | No | SMPL and MANO body models: registration, non-commercial; Sapiens custom licence; CoTracker3 CC BY-NC; TAPNet `.npy`/`.pt`/`.ckpt` |
| 10 | **Spatial VLMs and point-cloud models** | Distance and direction questions, embodied planning, room layout from scans | **Yes** (SenseNova-SI) | Many fine-tunes of Qwen2.5-VL-3B (research licence) carry a misleading MIT or Apache label; SpatialLM and Sonata CC BY-NC |

**Cross-cutting notes**:
- **Custom code**: Molmo2, InternVL3.5, Sa2VA, the original Florence-2 and moondream2 ship Python files run with `trust_remote_code`. Qwen3-VL, Gemma 4, Qwen3.8, MiniCPM-V 4.7, SmolVLM2, the community Florence-2, Depth Anything 3, TRELLIS.2, TripoSG, RF-DETR and EoMT do not.
- **Hidden dependencies**: a pipeline can pass on its own weights and still pull a gated or non-commercial model (TRELLIS.2 and Pixal3D load DINOv3 and RMBG-2.0).
- On a Mac, most 3D generators and splatting trainers are CUDA-first; Mac use relies on community ports.

## Hacker News comments used

Algolia API, comments only. Window: since 13.05.2026.

- A 128 GB headless llama.cpp box captions NAS photos into EXIF with Qwen3-VL 30B, in daily use ([vunderba, 14.05.2026](https://news.ycombinator.com/item?id=48141957); [06.08.2026](https://news.ycombinator.com/item?id=49204201)).
- Qwen3-VL 8B as a small utility vision model, often better than a much larger model ([barrkel, 14.11.2026](https://news.ycombinator.com/item?id=50496049)), 100–200 tokens/s for short captions ([barrkel, 14.11.2026](https://news.ycombinator.com/item?id=50498683)); Qwen VL models best for visual comprehension ([Grimblewald, 21.07.2026](https://news.ycombinator.com/item?id=48990462)).
- Gemma 4 12B at 4 bits for image sorting and description ([SwellJoe, 14.08.2026](https://news.ycombinator.com/item?id=49304989)); Gemma 4 12B QAT image analysis praised ([dofm, 15.10.2026](https://news.ycombinator.com/item?id=50104808)); Gemma 4 26B-A4B for private image processing ([deniska, 09.10.2026](https://news.ycombinator.com/item?id=50023492)); 53 % on a coin-classification test ([dgacmu, 02.10.2026](https://news.ycombinator.com/item?id=49933256)).
- mlx-vlm sampler support weak compared with llama.cpp ([Der_Einzige, 21.07.2026](https://news.ycombinator.com/item?id=48990705)).
- RF-DETR's larger variants use PML 1.0, not Apache ([MrGLaDOS, 23.06.2026](https://news.ycombinator.com/item?id=48644088); confirmed by a Roboflow co-founder, [yeldarb, 24.06.2026](https://news.ycombinator.com/item?id=48663168)); RF-DETR beats YOLO26 ([steinvakt2, 23.06.2026](https://news.ycombinator.com/item?id=48641995)); D-FINE-seg presented by its author ([argo_cve, 20.07.2026](https://news.ycombinator.com/item?id=48984985)).
- Grounding DINO for text to box, SAM 2 for clicks ([geuis, 23.06.2026](https://news.ycombinator.com/item?id=48642418)); both useful to curate training data ([IanCal, 09.06.2026](https://news.ycombinator.com/item?id=48458256)).
- Phone, ffmpeg, COLMAP and OpenSplat on an M4 MacBook Air gave a good splat ([ImaCake, 24.05.2026](https://news.ycombinator.com/item?id=48256292)); Brush and LichtFeld Studio named as open trainers ([slimbuck, 26.07.2026](https://news.ycombinator.com/item?id=49063061)); splats do not give clean game meshes ([jfrei, 10.11.2026](https://news.ycombinator.com/item?id=50443041)).
- Local 3D generators under 96 GB give meshes fit only for prototypes ([embedding-shape, 03.09.2026](https://news.ycombinator.com/item?id=49549264)); a local Flux plus Hunyuan3D pipeline, fun but "junky" ([wincy, 02.06.2026](https://news.ycombinator.com/item?id=48374315)); TRELLIS 2 among useful local tools ([potsandpans, 21.05.2026](https://news.ycombinator.com/item?id=48225567)).
- ViTPose+ Large for dance sync and running gait ([dr_blueberry, 14.09.2026](https://news.ycombinator.com/item?id=49702489)).
- Searches with no usable result: MiniCPM-V, Molmo2, InternVL, SmolVLM, Florence-2, Marigold, COLMAP, CoTracker, Pixal3D, MapAnything.

## Candidates by category

"Main option" = the best candidate under the strict policy; "Alternative" = also usable; "Flag" = usable only after a check. Already documented models are not repeated here.

### 1. Vision-language models

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`google/gemma-4-31B-it`** (also 26B-A4B, 12B; documented) | Apache 2.0 | 62.6 / 51.6 / 23.9 GB (official QAT Q4_0 GGUF 18.9 / 15.6 / 7.2 GB) | `842da3794eaa` | llama.cpp, Ollama, mlx-vlm | See the [Gemma 4 record](../model-comparison.md) | **Main option**; no custom code |
| `openbmb/MiniCPM-V-4.7-35B-A3B` | Apache 2.0 | 70.4 GB (official GGUF Q4_K_M 21.2 + 1.1 GB projector) | `98e79ba972b5` | llama.cpp, Ollama | About 10× faster than Qwen models on a 58 MP photo, fewer image tokens ([mlx-vlm #2546](https://github.com/Neywa-Labs/mlx-vlm/issues/2546), 17.10.2026); bounding boxes placed too low, acknowledged ([llama.cpp #30508](https://github.com/ggml-org/llama.cpp/issues/30508), 14.10.2026) | Alternative: fast on large photos |
| `Qwen/Qwen3-VL-32B-Instruct` | Apache 2.0 | 66.7 GB (MLX 4-bit 19.6 GB) | `0cfaf48183f5` | mlx-vlm, llama.cpp, Ollama | See the Qwen3-VL record | Alternative: dense sibling of the documented 30B-A3B |
| `Qwen/Qwen3-VL-235B-A22B-Instruct` | Apache 2.0 | 471 GB; GGUF UD-Q2_K_XL 88.0, UD-IQ3_XXS 94.6 GB | `710c13861be6` | llama.cpp | None found | Fits only at 2–3 bits |
| `allenai/Molmo2-8B` (also 4B) | Apache 2.0 | 34.7 GB fp32 (MLX 4-bit 6.4 GB) | `e28fa28597e5` | mlx-vlm; llama.cpp not confirmed | Thin | **Flag**: custom code; strong at pointing |
| Small: `HuggingFaceTB/SmolVLM2-2.2B-Instruct`, `florence-community/Florence-2-large` | Apache 2.0, MIT | 9.0, 1.55 GB | – | Transformers | None | Alternatives: small; Florence-2 also detects and grounds. Prefer the community Florence-2 to Microsoft's (custom code, `.bin`) |

Also Apache or MIT and within 128 GB: InternVL3.5-38B (custom code), Ministral 3 14B, Kimi-VL-A3B-Thinking; older video models LLaVA-Video-7B and VideoChat-Flash-7B.

- Excluded: Gemma 3 and 3n (Gemma licence, gated), Qwen3.8-Flash-Next (Qwen community licence, 360 GB), LFM2.5-VL (LFM licence), Moondream 3 (licence "other", `.pt`; praised for pointing and counting, [brianjking, 19.06.2026](https://news.ycombinator.com/item?id=48594235)). Not checked: quantised sizes of GLM-4.6V (MIT, 215 GB bf16) and Mistral Small 4 (Apache, 242 GB); Llama 4.

### 2. Detection and grounding

| Repo | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| **`Roboflow/rf-detr-base`** (also nano, medium, large) | Apache 2.0 | 0.13 GB | `7b95b089788e` | Transformers, PyTorch MPS (not checked) | **Main option** for real-time detection; Nano to Large only |
| **`openmmlab-community/mm_grounding_dino_large_all`** | Apache 2.0 | 1.38 GB | `0445d0a0ae5f` | Transformers | **Main option** for text-to-box detection |
| `ustc-community/dfine-xlarge-obj365` | Apache 2.0 | 0.25 GB | `a99923ec2727` | Transformers | Alternative |
| `google/owlv2-large-patch14-ensemble` | Apache 2.0 | 1.75 GB | `95e26936e865` | Transformers | Alternative: also detects by example image |
| `PekingU/rtdetr_v2_r50vd`, `IDEA-Research/grounding-dino-base`, LLMDet, OmDet-Turbo | Apache 2.0 | small | – | Transformers | Alternatives |

- Excluded: Ultralytics YOLO11, YOLOv8, YOLO26 and YOLOE (AGPL-3.0, `.pt`), DEIMv2 (custom licence), Rex-Omni (licence "other"), RF-DETR XL, 2XL and NAS (PML 1.0).

### 3. Segmentation

Documented: SAM 2.1 (promptable, video), Falcon Perception (text-prompted).

| Repo | Licence | Size | Commit | Verdict |
|---|---|---|---|---|
| **`tue-mps/coco_panoptic_eomt_large_640`** (EoMT; also semantic and instance variants) | MIT | 1.27 GB | `dcd130bed9b1` | **Main option** for panoptic, semantic and instance segmentation; Transformers |
| `tue-mps/eomt-dinov3-ade-semantic-large-512` | MIT | 1.26 GB | `1d1f172700ab` | **Flag**: whether DINOv3 terms carry over was not checked |
| `yonigozlan/EdgeTAM-hf` (conversion of Meta EdgeTAM) | Apache 2.0 | 0.06 GB | `c266ce53b3fc` | Alternative: light video tracking; upstream licence not checked |
| `ByteDance/Sa2VA-Qwen3-VL-4B` | Apache 2.0 | 20.2 GB | `fa5f0ed5d0b0` | **Flag**: custom code; the card names an InternVL3 base |
| `CIDAS/clipseg-rd64-refined` | Apache 2.0 | 0.6 GB | – | Alternative: quick, coarse text-prompted masks |

- Excluded: SAM 3 and 3.1 (gated, SAM licence; an MLX copy declares no licence), Mask2Former, OneFormer (`.pth`/`.bin`), SegFormer (NVIDIA licence), DINOv3 backbones (gated).

### 4. Depth estimation

Documented: MoGe-3 (MLX port).

| Repo | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| **`depth-anything/DA3METRIC-LARGE`** (also DA3MONO-LARGE, DA3-BASE, DA3-SMALL) | Apache 2.0 | 1.34 GB | `4010e39f3634` | PyTorch, MPS pointers in the GitHub issues | **Main option**; feedback thin. DA3-LARGE, GIANT and NESTED are CC BY-NC |
| `depth-anything/Depth-Anything-V2-Small-hf` | Apache 2.0 | 0.10 GB | `5426e4f0f365` | Transformers | Alternative: small (Base and Large are CC BY-NC) |
| `depth-anything/prompt-depth-anything-vitl-hf` | Apache 2.0 | 1.36 GB | `abfaa0958bbe` | Transformers | Alternative: metric depth guided by LiDAR |
| `prs-eth/marigold-depth-v1-0` | Apache 2.0 | 7.74 GB | `f4fc453d7d21` | diffusers (MPS) | Alternative (v1-1 is OpenRAIL++) |
| `jingheya/lotus-depth-g-v2-1` | Apache 2.0 | 4.3 GB | – | diffusers | Alternative |

- Excluded: Depth Pro (Apple licence), UniDepth (CC BY-NC), Metric3D (`.pth`), Pixel-Perfect-Depth and FlashDepth (`.pth`), DepthCrafter (licence "other"), RollingDepth (OpenRAIL).
- Flagged: Video Depth Anything Small (Apache but `.pth`; its MLX copy declares CC BY-NC, unlike the original).

### 5. Normals and intrinsic decomposition

| Repo | Licence | Size | Commit | Verdict |
|---|---|---|---|---|
| `jingheya/lotus-normal-g-v1-1` | Apache 2.0 | 4.32 GB | `92b42fd7f5c3` | Alternative |
| `Stable-X/stable-normal-v0-1` | Apache 2.0 | 4.06 GB | `4362d11c636e` | Alternative |
| `Yanrui95/NormalCrafter` (video) | Apache 2.0 | 4.51 GB | `7e24d68d86ae` | **Flag**: base-model licence not checked |

No feedback found. Excluded: DSINE (custom licence), Marigold v1-1 normals and IID (OpenRAIL++).

### 6. Multi-view reconstruction and matching

Documented: MapAnything (Apache variant).

| Repo or tool | Licence | Size | Commit | Verdict |
|---|---|---|---|---|
| **COLMAP** (GLOMAP now merged into it) | BSD-3 | tool | – | **Main option** for classical SfM; native macOS builds |
| `depth-anything/DA3-BASE` | Apache 2.0 | 0.54 GB | `f4a6c9b3c95e` | Alternative: feed-forward geometry and camera poses from any number of views |
| `ETH-CVG/lightglue_disk` | Apache 2.0 | 0.05 GB | `2df49cd2b07e` | Alternative: matching (the SuperPoint version is "other") |
| `zju-community/matchanything_eloftr` | Apache 2.0 | 0.06 GB | `7bd52a4d5e2c` | Alternative: cross-modality matching |

- Excluded: DUSt3R, MASt3R, CUT3R (CC BY-NC-SA), VGGT (CC BY-NC; commercial variant gated), MapAnything non-Apache variant (CC BY-NC), Pi3 (BSD-2, outside the strict list), Pi3X (CC BY-NC), STream3R (licence "other"), Fast3R (FAIR non-commercial), HunyuanWorld-Mirror (Tencent licence).

### 7. Gaussian splatting and NeRF tools

| Tool | Licence | Last activity | Apple silicon | Verdict |
|---|---|---|---|---|
| **Brush** | Apache 2.0 | 03.10.2026 | Yes (Rust and wgpu, Metal) | **Main option**; a Mac regression fixed the same day ([#533](https://github.com/ArthurBrussee/brush/issues/533), 09.09.2026) |
| OpenSplat | AGPL-3.0 | 29.10.2026 | Yes (MPS) | Works on a Mac (HN 24.05.2026); copyleft |
| MetalSplatter | MIT | 02.09.2026 | Native Metal | Viewer only |
| LichtFeld Studio | GPL-3.0 | 14.11.2026 | Not checked | Copyleft |
| nerfstudio | Apache 2.0 | 29.07.2025 | Partial (splatfacto failed) | Slowing |
| gsplat | Apache 2.0 | 19.09.2026 | **No** (CUDA only) | Not for a Mac |

Blender 5.3 added Gaussian-splat support (November 2026). Excluded: INRIA gaussian-splatting (non-commercial).

### 8. Image-to-3D generation

| Repo | Licence | Size | Commit | Mac runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| `VAST-AI/TripoSG` | MIT | 7.95 GB | `2c1c516d22d5` | PyTorch; MPS not checked | None | Alternative: no hidden dependency found |
| `microsoft/TRELLIS.2-4B` | MIT | 16.2 GB | `af44b45f2e35` | CUDA officially; community MPS port (about 5 min 40 s on an M4 Pro) | Hangs on macOS 27 on an M3 Air ([HF #19](https://huggingface.co/microsoft/TRELLIS.2-4B/discussions/19), 16.09.2026) | **Flag**: the pipeline loads DINOv3 (gated) and RMBG-2.0 (gated, non-commercial) |
| `TencentARC/Pixal3D` | MIT (since about 01.06.2026) | 46.1 GB | `b0cb2e1b794c` | CUDA; a ggml port takes about 34 min per image on an M2 16 GB; 169–420 s on a DGX Spark ([HF #11](https://huggingface.co/TencentARC/Pixal3D/discussions/11), 12.10.2026) | RMBG can be swapped for BiRefNet ([HF #3](https://huggingface.co/TencentARC/Pixal3D/discussions/3), 29.07.2026) | **Flag**: same DINOv3 and RMBG dependencies; the card carries an EU restriction flag |
| `stepfun-ai/Step1X-3D`, `wgsxm/PartCrafter` | Apache 2.0, MIT | 19.6, 4.0 GB | `bf7084495b3a` / – | Probably CUDA (not checked) | None | Alternatives |

- Excluded: Hunyuan3D 2, 2.1, 2mini (Tencent licence, not valid in the EU, UK or South Korea; `.ckpt`/`.bin`), Stable Fast 3D and SPAR3D (gated), TripoSR (`.ckpt`), InstantMesh (`.ckpt`/`.bin`), SAM 3D Objects (gated), Apple Sharp (Apple licence, `.pt`), Direct3D-S2 (`.ckpt`), Lyra 2.0 (no licence), HunyuanWorld 1 (Tencent licence). A TRELLIS.2 GGUF copy declares "other", unlike the MIT original.

### 9. Pose and point tracking

| Repo | Licence | Size | Commit | Verdict |
|---|---|---|---|---|
| **`usyd-community/vitpose-plus-huge`** (also base-simple, 0.34 GB) | Apache 2.0 | 3.60 GB | `9f36d7aec180` | **Main option** for 2D body keypoints; Transformers |
| `akore/rtmw-l-256x192` (conversion of mmpose RTMW) | Apache 2.0 (matches) | 0.23 GB | `fd7df05e28ce` | Alternative: whole body (body, hands, face); loader not checked |

- **Point tracking**: nothing passes (TAPIR and TAPNext `.npy`/`.pt`/`.ckpt`, AllTracker `.pth`, CoTracker3 CC BY-NC).
- **6-DoF object pose**: FoundationPose excluded (NVIDIA licence, ONNX, TensorRT).
- **3D body mesh**: every SMPL-based model needs registration-only, non-commercial body files; SAM 3D Body gated; Sapiens and Sapiens2 custom licences.

### 10. Spatial VLMs and point clouds

Documented: SenseNova-SI-1.3.

| Repo | Licence | Size | Commit | Verdict |
|---|---|---|---|---|
| `BAAI/RoboBrain2.5-4B` (Qwen3-VL architecture) | Apache 2.0 | 9.65 GB | `ec4b3bf5e969` | Alternative |
| `remyxai/SpaceQwen3-VL-2B-Thinking` | Apache 2.0 | 4.26 GB | `405a1c95bd0c` | Alternative: small |
| `nyu-visionx/Cambrian-S-7B` (spatial video) | Apache 2.0 | 32.1 GB | `556e72fded09` | Alternative; mlx-vlm support not checked |
| `allenai/Molmo2-ER` (embodied reasoning) | Apache 2.0 | 19.4 GB | `dab22564403d` | **Flag**: custom code |

No feedback found. Excluded: SpaceQwen2.5-VL, SpaceThinker, SpaceOm and Spatial-MLLM (research-licence Qwen2.5-VL base, whatever their own label), SpatialRGPT and ViLaSR (no licence), Cosmos-Reason (NVIDIA licence), SpatialLM (CC BY-NC); point clouds: PointTransformerV3 (`.pth`), Sonata (CC BY-NC).

**Third-party conversions**: several mlx-community, community and individual copies declare a licence that differs from the original (Video Depth Anything MLX, SAM 3.1 MLX, a TRELLIS.2 GGUF). Check them with the method in [`../research-method.md`](../research-method.md#third-party-conversions) before relying on them.
