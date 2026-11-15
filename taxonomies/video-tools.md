# Taxonomy of local AI video tools

Research of 15 November 2026, metadata and user feedback only. Companion of the other files in this folder.
"Covered by documented models?" tells whether the task is already covered by models with a record in [`../model-comparison.md`](../model-comparison.md#video): Wan 2.2 (T2V-A14B, I2V-A14B, TI2V-5B) and LTX 2.3; SeedVR2 upscaling is in the image section.
"Licence and format pitfalls" assume a strict policy: Apache 2.0 or MIT licences, safetensors or GGUF weights, no gated repository.
**Reddit could not be read**. Licences, gating, sizes and commits come from the Hugging Face API, read on 15.11.2026; commits are the first 12 characters.

## Reference resources

| Resource | Last update | What it covers | Strengths | Weaknesses |
|---|---|---|---|---|
| [VBench / VBench-2.0 leaderboard](https://huggingface.co/spaces/Vchitect/VBench_Leaderboard) | 01.04.2026 | Text-to-video and image-to-video on 16+ dimensions | Fine-grained, reproducible | Automatic metrics; no audio; newest models missing |
| Artificial Analysis video arena | Hugging Face mirror 20.06.2025 (stale); site not checked | Human-preference Elo | Includes closed models | Mostly API models |

## Taxonomy

| # | Category → sub-tasks | Typical uses | Covered by documented models? | Licence and format pitfalls |
|---|---|---|---|---|
| 1 | **Text-to-video** | Clips from prompts | **Yes** (Wan 2.2, LTX 2.3) | HunyuanVideo, SkyReels, CogVideoX 1.5, LTX and MiniMax use custom licences |
| 2 | **Image-to-video**, first and last frame | Animating stills | **Yes** (Wan 2.2 I2V, LTX 2.3) | Wan repositories also ship `.pth` VAE and text-encoder files |
| 3 | **Video with audio** | Clips with sound and speech | LTX 2.3 (custom licence) | Most 2026 models with audio are custom-licensed or too large |
| 4 | **Video editing and motion control** → restyling, character replacement, dance | Restyling, motion transfer | No | Large models do not fit unquantised |
| 5 | **Talking head, speech-to-video, lip sync** | Avatars, dubbing | No | LatentSync: OpenRAIL++ and `.pt`; dependency chains (a VAE under another licence) |
| 6 | **Frame interpolation** | Higher frame rate, slow motion | No | RIFE weights `.pkl`, FILM a TensorFlow SavedModel; **no safetensors build found** |
| 7 | **Video upscaling and restoration** | Upscaling to 1080p and above | Partly (SeedVR2 conversion) | Official SeedVR2 is `.pth` only |
| 8 | **Runtimes** | – | – | ComfyUI is GPL-3.0; many MPS bf16 NaN and black-frame bugs (see below) |

## Hacker News comments used

Algolia API, comments only. Window: since 13.05.2026.

- Local LTX 2.3 or Wan plus SeedVR2 upscaling is a workable pipeline ([vunderba, 15.05.2026](https://news.ycombinator.com/item?id=48155014)).
- MiniMax-H3's ~31B transformer is slow and heavy locally ([jiant, 07.11.2026](https://news.ycombinator.com/item?id=50405264)); runs on one 32 GB V100 for family use ([montroser, 02.11.2026](https://news.ycombinator.com/item?id=50342050)).
- Searches with no or thin results: Kandinsky 6, MAGI-2, HunyuanVideo 1.5, LongCat-Video.

## Candidates by category

"Main option" = the best candidate under the strict policy; "Alternative" = also usable; "Flag" = usable only after a check.

### 1–3. Text-to-video, image-to-video, video with audio

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`kandinskylab/Kandinsky-6.0-Lite-5s-Diffusers`** (3B) | MIT | 27.74 GB | `8ec017692475` | diffusers; MPS not checked | None found | **Main option** for video with audio (09.09.2026): text or image to 5 s video with sound and lip sync |
| `meituan-longcat/LongCat-Video` | MIT | 83.29 GB | `03b55529b1d1` | PyTorch; MPS not checked | None in window | Alternative: text-to-video, image-to-video, continuation |
| `zai-org/CogVideoX-2b` | Apache 2.0 | 13.77 GB | `1137dacfc2c9` | diffusers on MPS | None | Old (2024); a baseline |
| `genmo/mochi-1-preview` | Apache 2.0 | 133.45 GB (several precisions) | `cd1d0fe89aa8` | diffusers, ComfyUI | None | Old (2024) |

- Excluded: Kandinsky 6.0 Pro (gated), HunyuanVideo 1.5 (Tencent Hunyuan community licence; territorial restrictions not checked), LTX-2.5 (LTX-2 community licence, gated), MAGI-2 preview (Apache, but 302 GB, `.ckpt`/`.pth`, built for 8 data-centre GPUs), MAGI-1 (222 GB, `.bin`), MiniMax-H3 (custom licence, 498 GB), SkyReels V2/V3 (Skywork licence, `.pth`), CogVideoX 1.5 (licence "other"). Not checked: Ovi.

### 4. Editing and motion

| Repo | Licence | Size | Commit | Verdict |
|---|---|---|---|---|
| `Wan-AI/Wan2.2-Animate-2-14B` | Apache 2.0 | ≈ 82 GB (65.58 safetensors + 16.92 `.pth`) | `6e8f1973bf0a` | **Flag**: same `.pth` VAE and text-encoder pattern as Wan 2.2; no feedback |
| `Wan-AI/Wan-Dancer-14B` | Apache 2.0 | ≈ 86 GB (same pattern) | `85ce88dd8d02` | **Flag**: music-to-dance, niche |
| `ByteDance/Bernini-Diffusers-v2` | Apache 2.0 | 192.36 GB | `399cf6a18a4c` | Does not fit unquantised |

### 5. Talking head and speech-to-video

| Repo | Licence | Size | Commit | Feedback | Verdict |
|---|---|---|---|---|---|
| `meituan-longcat/LongCat-Video-Avatar-1.5` (1.6 released 13.11.2026) | MIT | ≈ 75 GB (59.37 safetensors, plus `.bin`, `.msgpack`, ONNX) | `92016c71d5d3` | A 3-minute music video on an RTX 5090 ([HF #9](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5/discussions/9), 29.10.2026); a strong rival to LTX 2.3 for one user ([HF #4](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5/discussions/4), 25.05.2026) | **Flag**: mixed formats; whether the `.bin` part can be skipped was not checked |
| `MeiGen-AI/InfiniteTalk` | Apache 2.0 | 168.55 GB (many variants; needs a Wan 2.1 base) | `d59847ebdacf` | None in window | Alternative: take a single variant |
| `kandinskylab/Kandinsky-S2V-1.0-Lite` | MIT | 4.54 GB (transformer only) | `9da9bc4c331e` | None | **Flag**: needs Qwen2.5-Omni-7B and the HunyuanVideo VAE (Tencent licence) |

- Excluded: LatentSync 1.6 (OpenRAIL++, `.pt`/`.pkl`).

### 6–7. Upscaling and interpolation

| Repo | Licence | Size | Commit | Verdict |
|---|---|---|---|---|
| `kandinskylab/Kandinsky-6.0-VSR-5s-Diffusers` | MIT | 17.45 GB | `f690411e3149` | Alternative: built for Kandinsky 6 output |
| `numz/SeedVR2_comfyUI` (third-party conversion of SeedVR2) | Apache 2.0 (matches) | 60.11 GB (several variants) | `09ced7102363` | Documented in the image section |
| `JunhaoZhuang/FlashVSR-v1.1` | Apache 2.0 | 6.95 GB (5.68 safetensors, plus `.ckpt`/`.pth`) | `2aa7e1f3ab50` | **Flag**: mixed formats |
| RIFE, FILM | MIT / Apache 2.0 (code) | small | – | **Flag on format**: no safetensors build found |

### 8. Runtimes on a Mac

| Runtime | Licence | Last activity | Notes |
|---|---|---|---|
| ComfyUI | GPL-3.0 | active | Known MPS issues: Wan 2.2 5B corrupt frames after the first ([#16644](https://github.com/Comfy-Org/ComfyUI/issues/16644), 29.09.2026); LTX 2.5 all black unless `--use-split-cross-attention` ([#15818](https://github.com/Comfy-Org/ComfyUI/issues/15818), 23.08.2026); random NaN attention with bf16 LTX-2.x ([#15804](https://github.com/Comfy-Org/ComfyUI/issues/15804), 22.08.2026); out of memory while dequantising INT8 on an M4 Pro ([#17264](https://github.com/Comfy-Org/ComfyUI/issues/17264), 21.10.2026). Fixes: Wan 2.2 VAE on MPS ([PR #17757](https://github.com/Comfy-Org/ComfyUI/pull/17757), 14.11.2026), fp16 VAEs on Apple GPUs ([PR #16996](https://github.com/Comfy-Org/ComfyUI/pull/16996), 13.10.2026) |
| diffusers | Apache 2.0 | active | MPS backend |
| ltx-2-mlx (dgrauet) | MIT | 01.11.2026 | LTX 2.3 and 2.5 on MLX |
| mlx-video (Blaizzy) | MIT | 13.05.2026 | Wan 2.1/2.2 and LTX-2; **stale** |

**Third-party conversions**: ComfyUI repacks and MLX ports are often published by individuals. Check them with the method in [`../research-method.md`](../research-method.md#third-party-conversions) before relying on them.
