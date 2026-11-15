# Taxonomy of local AI speech and voice tools

Research of 15 November 2026, metadata and user feedback only. Companion of `image-tools.md` and `music-tools.md`.
"Covered by documented models?" tells whether the task is already covered by models with a record in [`../model-comparison.md`](../model-comparison.md): speech recognition (Qwen3-ASR, Qwen3-ForcedAligner, VibeVoice-ASR, Voxtral Mini Realtime, Whisper large-v3-turbo) and 19 speech synthesis models.
"Licence and format pitfalls" assume a strict policy: Apache 2.0 or MIT licences, safetensors or GGUF weights, no gated repository.
Language notes focus on English, French, German and Italian.
**Reddit could not be read**. Licences, gating, sizes and commits come from the Hugging Face API, read on 15.11.2026; commits are the first 12 characters.

## Reference resources

| Resource | Last update | What it covers | Strengths | Weaknesses |
|---|---|---|---|---|
| [Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard) ([code](https://github.com/huggingface/open_asr_leaderboard)) | 13.11.2026 | Word error rate: English short and long form, multilingual (FLEURS, MCV, MLS) | Reproducible; the multilingual tab covers fr, de, it; often cited on HN | Speed measured on an H200, says nothing about a Mac; no diarisation, VAD or streaming track |
| [TTS Arena V2](https://huggingface.co/spaces/TTS-AGI/TTS-Arena-V2) | 11.11.2026 | Blind A/B Elo ranking of TTS models | Human preference, open and closed models | Mostly English; no cloning or latency axis |
| [mlx-audio model table](https://github.com/Neywa-Labs/mlx-audio) (moved from Blaizzy/mlx-audio) | commit 14.11.2026 | TTS, STT, VAD, diarisation, enhancement and speech-to-speech models that run on MLX | The best "what runs on a Mac" list | No licence column; mixes non-commercial and open models |
| [Picovoice speech-to-text benchmark](https://github.com/Picovoice/speech-to-text-benchmark) | 14.11.2026 | WER and speed of on-device engines | Measures CPU and on-device speed | Run by a vendor |
| [awesome-diarization](https://github.com/wq2012/awesome-diarization) | 26.10.2026 | Diarisation papers, tools, datasets | Broad, maintained | No licence or format triage |
| [speech-trident](https://github.com/ga642381/speech-trident) | 10.07.2026 | Speech LLMs, codecs, representation models | Good map of speech-to-speech and omni models | Research-oriented |
| [open-tts-tracker](https://github.com/Vaibhavs10/open-tts-tracker) | 13.02.2025 | Open TTS models with licence columns | Licence columns | **Stale** |

## Taxonomy

| # | Category → sub-tasks | Typical uses | Covered by documented models? | Licence and format pitfalls |
|---|---|---|---|---|
| 1 | **Transcription (ASR)** → files, long audio, multilingual, punctuation | Meetings, interviews, voice notes, subtitles | **Yes** (Qwen3-ASR, Whisper, VibeVoice-ASR, Voxtral) | NVIDIA Parakeet and Canary: CC BY 4.0; Kyutai STT: CC BY 4.0; SenseVoice: custom licence and `.pt` |
| 2 | **Streaming and small on-device ASR** → live captions, dictation, low memory | Dictation, live captions | Partly (Voxtral Realtime) | Parakeet, the most praised dictation model, is CC BY 4.0; Moonshine tokenizer licence questioned |
| 3 | **Word timestamps and forced alignment** | Subtitles, karaoke, editing audio by text | **Yes** (Qwen3-ForcedAligner) | MMS aligner: CC BY-NC |
| 4 | **Speaker diarisation** → who spoke when, overlap | Meetings, podcasts, interviews | Partly (VibeVoice-ASR labels speakers) | pyannote: gated, `.bin`, community-1 is CC BY 4.0; Sortformer: CC BY 4.0 or NVIDIA licence; DiariZen: CC BY-NC. **No compliant standalone model found** |
| 5 | **Voice activity detection (VAD)** | Skip silence before ASR, voice assistants | No | TEN VAD: Apache 2.0 with extra conditions, ONNX; NVIDIA MarbleNet: NVIDIA licence |
| 6 | **Speech enhancement** → denoise, dereverberate, bandwidth restoration | Noisy recordings, old tapes, calls | No | Many originals are `.pt`/`.ckpt`; no compliant dedicated dereverberation model found |
| 7 | **Speech synthesis (TTS)** → preset voices, cloning, voice design, long form | Read-aloud, audiobooks, assistants | **Yes** (19 records) | Many strong models are non-commercial or custom (F5-TTS, Fish Audio S2, Higgs, IndexTTS, Spark-TTS, OmniVoice) |
| 8 | **Voice conversion** → change the voice of a recording | Dubbing your own voice, privacy | No | Seed-VC GPL-3.0; OpenVoice and RVC `.pth`; Vevo CC BY-NC. **Ethics**: never convert to a real person's voice without consent |
| 9 | **Speech-to-speech conversation** → full duplex, omni models | Voice assistants | No | Moshi weights CC BY 4.0; PersonaPlex NVIDIA licence; LFM audio models custom licence |
| 10 | **Speech translation** → speech in, translated text or speech out | Travel, meetings, subtitles in another language | No | SeamlessM4T: CC BY-NC and `.pt`; Hibiki: CC BY / CC BY-NC-SA |
| 11 | **Runtimes** | – | – | whisper.cpp models are legacy ggml `.bin` (not GGUF); WhisperKit and FluidAudio use CoreML; sherpa-onnx uses ONNX |

**Cross-cutting notes**:
- The strict policy removes the most praised dictation model (Parakeet, CC BY 4.0) and every standalone diarisation pipeline. Compliant routes exist, but they are newer and less tested.
- Several third-party conversions declare a licence different from the original (see "Third-party conversions" at the end). Check the upstream licence before relying on a conversion.
- Open full-duplex models are still far behind cascades (ASR → LLM → TTS) for most uses, according to HN comments (see below).

## Hacker News comments used

Algolia API, comments only. Window: since 13.05.2026.

- Live call transcription with Silero VAD, Qwen3-ASR-1.7B and pyannote community-1 ([navels, 05.11.2026](https://news.ycombinator.com/item?id=50373463)).
- pyannote community-1 performed much better than Sortformer ([zaptheimpaler, 19.07.2026](https://news.ycombinator.com/item?id=48964953)).
- The pyannote gate looks like an extra restriction on a CC BY 4.0 model ([3eb7988a1663, 13.06.2026](https://news.ycombinator.com/item?id=48520036)); WhisperX depends on pyannote, whose licensing complicates scripted installs ([dmayle, 07.07.2026](https://news.ycombinator.com/item?id=48822845)).
- Local models remain weak on multilingual diarisation, overlap and language switching ([cloaky233, 11.10.2026](https://news.ycombinator.com/item?id=50041609)).
- Senko plus Parakeet faster and more accurate than pyannote and Whisper on a MacBook ([dghlsakjg, 07.07.2026](https://news.ycombinator.com/item?id=48823023)).
- MOSS-Transcribe-Diarize better than Whisper, especially on multilingual and noisy audio ([wahnfrieden, 13.07.2026](https://news.ycombinator.com/item?id=48895623)); runs its MLX fork ([wahnfrieden, 13.07.2026](https://news.ycombinator.com/item?id=48898359)).
- A transcribe.cpp diarisation pull request uses Granite Speech 4.1 2B Plus and MOSS ([simonw, 19.07.2026](https://news.ycombinator.com/item?id=48964768)); MOSS-Transcribe-Diarize and the Open ASR Leaderboard suggested for local diarisation ([verdverm, 20.10.2026](https://news.ycombinator.com/item?id=50169159)).
- FireRedVAD beats TEN and Silero on benchmarks; used offline with Whisper ([wahnfrieden, 13.07.2026](https://news.ycombinator.com/item?id=48895771); [13.07.2026](https://news.ycombinator.com/item?id=48899230)).
- Silero VAD in front of whisper.cpp smoothed the experience ([PalmPilotProMax, 20.07.2026](https://news.ycombinator.com/item?id=48973247)); in front of an audio LLM to skip silence ([jakswa, 08.07.2026](https://news.ycombinator.com/item?id=48836659)); in a local voice pipeline with Kokoro and Parakeet ([cjus, 29.10.2026](https://news.ycombinator.com/item?id=50287289)).
- DeepFilterNet works locally, but a commercial cloud enhancer is better ([causality0, 13.07.2026](https://news.ycombinator.com/item?id=48888313)); converted to CoreML for the Neural Engine ([whstl, 13.10.2026](https://news.ycombinator.com/item?id=50072357)).
- Chatterbox mentioned for voice-to-voice transformation ([razster, 09.07.2026](https://news.ycombinator.com/item?id=48840436)).
- Switched from Parakeet v3 to Granite Speech 5.0 470M TurboCTC in mlx-audio ([rahimnathwani, 13.10.2026](https://news.ycombinator.com/item?id=50074285)).
- Parakeet v3 via parakeet-mlx is the best speed/accuracy trade-off for Mac dictation ([d4rkp4ttern, 11.10.2026](https://news.ycombinator.com/item?id=50049269)); extremely fast on an M1 Air ([saaaaaam, 13.10.2026](https://news.ycombinator.com/item?id=50071419)); preferred to Whisper almost always ([coder543, 13.07.2026](https://news.ycombinator.com/item?id=48895258)); Whisper turbo handles accents better ([AG342, 15.06.2026](https://news.ycombinator.com/item?id=48536021)).
- Neither Moonshine nor Whisper more accurate or faster than Parakeet ([betterproblems, 12.10.2026](https://news.ycombinator.com/item?id=50049758)).
- Voxtral good for transcription, no hallucination in silence ([arjie, 20.10.2026](https://news.ycombinator.com/item?id=50169301)); Granite "OK" for ASR ([greenavocado, 17.06.2026](https://news.ycombinator.com/item?id=48570224)).
- Cohere Transcribe called excellent ([sipjca, 19.07.2026](https://news.ycombinator.com/item?id=48965004)).
- Qwen3-Omni too weak in conversation; went back to a cascade with Kokoro ([_davide_, 26.07.2026](https://news.ycombinator.com/item?id=49061021)); no newer Qwen omni model since ([_ache_, 18.09.2026](https://news.ycombinator.com/item?id=49749708)).
- Open full-duplex models are far behind commercial voice modes; cascades still better for most uses ([karimf, 24.10.2026](https://news.ycombinator.com/item?id=50223011)); full-duplex models struggle with tool calling ([armcat, 24.10.2026](https://news.ycombinator.com/item?id=50218836)).
- Searches with no usable result: Seed-VC, OpenVoice, resemble-enhance, MiniCPM-o, Step-Audio, Haru-4B, SeamlessM4T, Hibiki, Sesame CSM, TEN VAD.

## Candidates by category

"Main option" = the best candidate under the strict policy; "Alternative" = also usable; "Flag" = usable only after a check. Already documented models are listed in [`../model-comparison.md`](../model-comparison.md) and not repeated here.

### 1–3. Transcription, streaming ASR and alignment

Documented: Qwen3-ASR-1.7B (main multilingual model), Qwen3-ForcedAligner-0.6B (word timestamps), VibeVoice-ASR (long audio with speakers), Voxtral Mini 4B Realtime (streaming), Whisper large-v3-turbo (widest runtime support).

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`ibm-granite/granite-speech-5.0-470m-turboctc`** | Apache 2.0 | 0.95 GB | `91dcb0605daf` | mlx-audio | One user switched to it from Parakeet v3 (HN 13.10.2026); IBM made it multilingual with punctuation in October ([HF #7](https://huggingface.co/ibm-granite/granite-speech-5.0-470m-turboctc/discussions/7), 09.10.2026) | **Main option** for small, fast ASR: en, fr, de, es, pt, it, ja. Weights changed recently: pin the commit |
| `microsoft/VibeVoice-ASR-Streaming-1.5B` / `-7B` | MIT | 5.65 / 17.36 GB | `4262d23d8a53` / `60d858b518b4` | mlx-audio | None found | Alternative: streaming variants of VibeVoice-ASR; 10 languages including fr, de, it |
| `moonshine-ai/moonshine-streaming-tiny` / `small` / `medium` | MIT | 0.18 / 0.56 / 1.07 GB | `f8e9dfd8c562` / `2c036506f23a` / `57b843633a8c` | mlx-audio, moonshine C++ library | Not better than Parakeet (HN 12.10.2026); wrong word timestamps with speculative decoding ([#247](https://github.com/moonshine-ai/moonshine/issues/247), 07.11.2026); tokenizer licence questioned ([#244](https://github.com/moonshine-ai/moonshine/issues/244), 07.11.2026) | Alternative: **English only**, very low memory |
| `distil-whisper/distil-large-v3.5` | MIT | 3.04 GB | `728a7691f3ff` | mlx-audio, whisper.cpp | None in window | Alternative: English only |

- Excluded: NVIDIA Parakeet TDT 0.6B v3 and its ports (CC BY 4.0; known issue: lowercase, unpunctuated output in mlx-audio and parakeet-mlx, [mlx-audio #1060](https://github.com/Neywa-Labs/mlx-audio/issues/1060), 23.10.2026), Canary (CC BY 4.0), Kyutai STT (CC BY 4.0), SenseVoiceSmall (custom licence, `.pt`), Fun-ASR-MLT-Nano (Apache but `.pt`), Cohere Transcribe (Apache but gated; an ungated GGUF mirror re-hosts it).

### 4. Speaker diarisation

No compliant standalone diarisation model was found. The compliant routes are models that transcribe and label speakers together.

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`OpenMOSS-Team/MOSS-Transcribe-Diarize`** (0.9B) | Apache 2.0 | 1.83 GB | `10304d926740` | mlx-audio; MLX and GGUF ports by individuals (Apache) | Better than Whisper on noisy audio (HN 13.07.2026). Quiet and overlapping speech dropped, quality falls past 30–60 s ([HF #19](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize/discussions/19), 22.07–01.09.2026); endless loop on music-only audio, fix promised ([HF #27](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize/discussions/27), 09.10.2026) | **Main option**. The card claims 50+ languages; its challenge results include fr, de, it |
| `ibm-granite/granite-speech-4.1-2b-plus` | Apache 2.0 | 4.23 GB | `e69efe37f97b` | mlx-audio | Used in a transcribe.cpp diarisation pull request (HN 19.07.2026); quality feedback thin | Alternative: speaker attribution and word timestamps; en, fr, de, es, pt (**no Italian**) |
| VibeVoice-ASR (documented) | MIT | – | – | mlx-audio | See its record | Alternative: long audio with speakers |
| `cstr/pyannote-v3-segmentation-GGUF` | MIT (matches upstream) | 0.01 GB | `2b2492e0c04f` | CrispASR | None found | **Flag**: re-hosts a gated upstream; segmentation only, still needs a speaker-embedding model and clustering |

- Excluded: pyannote speaker-diarization-community-1 (CC BY 4.0, gated, `.bin`; well liked on HN), pyannote 3.1 and segmentation-3.0 (MIT but gated, `.bin`; 3.1 also pulls community-1, [pyannote #2044](https://github.com/pyannote/pyannote-audio/issues/2044)), NVIDIA Sortformer (CC BY 4.0, NVIDIA licence or CC BY-NC depending on the version), NVIDIA Nemotron 3 Diarization (OpenMDW 1.1), DiariZen (CC BY-NC, `.bin`), Rev diarization (custom, gated), CoreML ports (format).
- Flagged: `aufklarer/WeSpeaker-ResNet34-LM-MLX` (speaker embedding) declares MIT, but the upstream model is CC BY 4.0.

### 5. Voice activity detection

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`mlx-community/silero-vad-v6`** (Silero VAD v6) | MIT (matches upstream) | < 0.01 GB | `2ebf4a5e1072` | mlx-audio | The usual VAD in local pipelines (HN 08.07, 20.07, 29.10 and 05.11.2026) | **Main option**. The repository also holds `.py` helper files: take only the weights |
| `handy-computer/silero-vad-v6.2-gguf` | MIT | < 0.01 GB | `a9b2d61c20ae` | transcribe.cpp | None specific | Alternative (GGUF) |
| `cstr/firered-vad-GGUF` (FireRedVAD) | Apache 2.0 (matches upstream) | 0.01 GB | `f965baa5daf1` | CrispASR | Beats TEN and Silero on benchmarks per one user (HN 13.07.2026); 100+ languages claimed | Alternative (GGUF only; the original is `.pth.tar`) |

- Excluded: TEN VAD (Apache 2.0 with extra conditions, ONNX), FireRedVAD original (`.pth.tar`), fsmn-vad (Apache but `.pt`; a GGUF port exists, zh/en oriented), NVIDIA MarbleNet (NVIDIA licence), SpeechBrain CRDNN (no licence, `.ckpt`).
- Flagged: `mlx-community/silero-vad` (no licence field; prefer `-v6`).

### 6. Speech enhancement

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`mlx-community/DeepFilterNet-mlx`** (v1–v3, 48 kHz, real time) | MIT (upstream code and weights MIT/Apache since [06.11.2026](https://github.com/Rikorose/DeepFilterNet/commit/7b14b895fe7fc42cab72b4a4c1e49c982bd6404b)) | 0.03 GB | `220d5dfb7266` | mlx-audio | Works locally but below a commercial cloud enhancer (HN 13.07.2026); NaN output after long digital silence ([#713](https://github.com/Rikorose/DeepFilterNet/issues/713), 28.10.2026) | **Main option** for noise. Contains a `.py` conversion script: take only the weights |
| `starkdmi/MossFormer2_SE_48K_MLX` | Apache 2.0 (matches upstream) | 0.57 GB (all precisions) | `ccd0ded00e26` | mlx-audio | None found | Alternative: heavier, higher-quality class |
| `studio409/Resemble-Enhance-GGUF` | MIT (matches upstream) | 0.71 GB | `8b7128716ab3` | Not checked | None found | **Flag**: denoise plus bandwidth restoration, but no confirmed runtime |

- Excluded: MossFormer2, MossFormerGAN and FRCRN originals (Apache but `.pt`), Resemble Enhance original (MIT but `.pt`), SpeechBrain SepFormer (Apache, `.ckpt`), SGMSE (MIT, `.ckpt`), dereverb BS-RoFormer (GPL-3.0, `.ckpt`), NVIDIA enhancement models (CC BY-NC-SA or NVIDIA licence), DialogueSidon (CC BY-NC), SAM-Audio (custom licence).

### 7. Speech synthesis

Documented in 19 records. Under the strict policy the main options are Qwen3-TTS (10 languages including fr, de, it), VoxCPM2 (voice design, 30 languages), Chatterbox Multilingual, MOSS-TTS v1.5 (quality, long form), ZONOS3-Mini (fast, very new) and Kokoro (small; no German). See [`../model-comparison.md`](../model-comparison.md#speech-synthesis).

### 8. Voice conversion

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| `ResembleAI/chatterbox`, voice conversion part | MIT | ≈ 1.1 GB needed (`s3gen.safetensors`, `ve.safetensors`; repo 13.9 GB) | `5bb1f6ee58e5` | PyTorch MPS | Voice-conversion feedback thin (HN 09.07.2026) | **Main option, with caveat**: the built-in default voice is a `.pt` file; supply your own target voice clip instead |
| `theoracleguy/Chatterbox-VoiceConversion-MLX-fp16` | declares Apache 2.0 | 0.43 GB | `84810069b3c4` | mlx-audio | None found | **Flag**: individual upload; declared licence differs from upstream MIT |

- Excluded: Seed-VC (GPL-3.0, `.pth`; its MLX port is GPL-3.0 too), OpenVoice V1/V2 (MIT but `.pth`), RVC (`.pth`, voice packs mostly cloned from real people), Vevo 1/1.5/2 (CC BY-NC), CosyVoice (Apache, mixed `.pt`/ONNX; voice conversion from the safetensors alone not checked).

### 9. Speech-to-speech conversation

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| `higurashi-ai/Haru-4B` (full duplex, voice cloning) | Apache 2.0 | 10.56 GB | `8d6e83bcd370` | mlx-audio; official MLX code and macOS app | Released 12.11.2026; 4-bit weights degraded the text stream in a Rust port ([HF #2](https://huggingface.co/higurashi-ai/Haru-4B/discussions/2), 14.11.2026). A pretrained base model "for research" | **Too early**. en, es, pt, de, fr, zh, ja, ru, ko; **no Italian** |
| `Qwen/Qwen3-Omni-30B-A3B-Instruct` | Apache 2.0 by name (tag "other", no LICENSE file) | 70.53 GB (mlx-community 8-bit: 38.8 GB) | `26291f793822` | MLX ports; speech output on a Mac not checked | Judged too weak in conversation (HN 26.07.2026) | Alternative: the only large omni model with speech output in fr, de, it |
| `openbmb/MiniCPM-o-4_5` (9B, vision and speech) | Apache 2.0 | 20.05 GB | `fb09628e98b1` | llama.cpp, Ollama (speech output on a Mac not checked) | TTS cut-off reported ([HF #17](https://huggingface.co/openbmb/MiniCPM-o-4_5/discussions/17), 22.03.2026) | **Flag**: also holds `.pt` and ONNX files; whether speech output needs them was not checked |
| `XiaomiMiMo/MiMo-Audio-7B-Instruct`, `inclusionAI/Ming-3.0-audio-tiny` | MIT | 16.05 / 20.78 GB | `2b8c0171dd10` / `401b1abc63de` | mlx-audio | None found | Alternatives: English and Chinese only |

- Excluded: Kyutai Moshi (weights CC BY 4.0; lag and heat in MLX on a 24 GB MacBook Pro, [moshi #421](https://github.com/kyutai-labs/moshi/issues/421), 29.07.2026), NVIDIA PersonaPlex (NVIDIA licence, gated), LiquidAI LFM audio models (custom licence), Kimi-Audio (MIT but `.pt`), Sesame CSM-1B (gated; ungated mirrors re-host it), MOSS-Speech (no licence), Step-Audio 2 mini and Fun-Audio-Chat (Apache; en/zh; `.pt` and ONNX parts or no Mac runtime checked).

### 10. Speech translation

| Repo | Licence | Size | Commit | Runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|
| **`ibm-granite/granite-speech-4.1-2b`** (ASR plus speech translation to text) | Apache 2.0 | 4.87 GB | `823ca793aa49` | mlx-audio | Thin (HN 17.06 and 22.10.2026) | **Main option** for speech to translated text: en, fr, de, es, pt, ja (**no Italian**). A Granite Speech 5.0 2B exists; not checked |
| Qwen3-Omni-30B-A3B-Instruct (see 9) | – | – | – | – | – | Alternative: speech-to-speech translation by prompting, fr, de, it in and out |
| `mistralai/Voxtral-Mini-3B-2507` | Apache 2.0 | 18.72 GB | `3060fe34b35b` | mlx-audio | Voxtral series good for transcription (HN 20.10.2026) | Alternative: translation by prompting (not a dedicated task); en, fr, de, es, it, pt, nl, hi |

- Excluded: SeamlessM4T v2 and Seamless Streaming (CC BY-NC, `.pt`), Kyutai Hibiki (CC BY 4.0) and Hibiki-Zero (CC BY-NC-SA), NVIDIA Canary (CC BY 4.0).

### 11. Runtimes on a Mac

| Runtime | Licence | Last activity | Notes |
|---|---|---|---|
| **mlx-audio** | MIT | 14.11.2026 | Widest model coverage on MLX: ASR, TTS, VAD, diarisation, enhancement, speech-to-speech |
| whisper.cpp | MIT | 13.11.2026 | Metal; its own models are legacy ggml `.bin`, not GGUF |
| transcribe.cpp | MIT | 14.11.2026 | GGUF builds of several ASR, VAD and diarisation models |
| parakeet-mlx | Apache 2.0 | 05.11.2026 | Parakeet only (CC BY 4.0 weights) |
| WhisperKit, FluidAudio | MIT, Apache 2.0 | 11.10.2026, 14.11.2026 | CoreML weights, outside the strict format policy |
| sherpa-onnx | Apache 2.0 | 13.11.2026 | ONNX only |

**Third-party conversions**: the `mlx-community`, `cstr`, `handy-computer`, `starkdmi`, `studio409` and `theoracleguy` repositories are conversions published by individuals or an open community organisation, not by the original authors. Two declare a licence that differs from the original (Chatterbox voice conversion MLX, WeSpeaker MLX), and some re-host gated models (pyannote segmentation, Sesame CSM, Cohere Transcribe). Check them with the method in [`../research-method.md`](../research-method.md#third-party-conversions) before relying on them.
