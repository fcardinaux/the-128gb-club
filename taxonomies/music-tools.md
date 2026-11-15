# Taxonomy of local AI music tools

Research of 13 November 2026, metadata and user feedback only. Companion of `image-tools.md`.
"Covered by general models?" tells whether general-purpose models already do the job: speech recognition (for example Qwen3-ASR, Whisper, VibeVoice-ASR, Voxtral), TTS and voice cloning (for example Qwen3-TTS, Chatterbox, Fish Audio S2) and LLMs.
Licence and format remarks assume a strict policy: Apache 2.0 or MIT licences, safetensors or GGUF weights.
**Reddit was not read** in this pass. HN feedback on hands-on local use is moderate for song generation and stem separation, and thin for everything else.
Licences, gating, file lists, sizes and commits come from the Hugging Face API (`/api/models/<repo>?blobs=true`), read on 13.11.2026. Claims marked "not checked" were not verified against a source.

## Reference resources

| Resource | Last update | What it covers | Strengths | Weaknesses |
|---|---|---|---|---|
| [Hugging Face Tasks](https://huggingface.co/tasks) (`text-to-audio`, `audio-to-audio`, `audio-classification`, `audio-text-to-text`) | – | Official pipeline tags | Maps directly to Hub filters; sorting by trending shows new releases | No symbolic/MIDI task; separation, transcription and SVS are scattered across tags |
| [mlx-audio](https://github.com/Blaizzy/mlx-audio) model tables | commit 13.11.2026 | TTS, STT, STS, **music generation** (MiniMax Music 3, Stable Audio 3), music understanding (MOSS-Music), SAM-Audio separation | Shows what runs natively on Apple silicon | Lists models whatever their licence (several fail the strict policy) |
| [CrispASR](https://github.com/CrispStrobe/CrispASR) README / feature matrix | commit 13.11.2026 | GGUF + Metal runtime: piano and multi-instrument transcription (MT3, Onsets & Frames, hFT, Basic Pitch), beats (Beat This), chords (BTC), separation (Mel-RoFormer, SCNet) | The licence is stated for each backend; single binary, no PyTorch | Many ports by one developer; new backends are marked "candidate" |
| [ComfyUI audio](https://docs.comfy.org/tutorials/audio/ace-step/ace-step-v1) + Comfy-Org repos | Comfy-Org repos updated 09–10.2026 | Native nodes for ACE-Step 1.5, MiniMax Music 3, Stable Audio 3, YuE2 | Safetensors-only repacks; MPS backend | **Repack licence tags may be wrong** (Comfy-Org MiniMax-Music-3 says Apache 2.0, upstream is a custom licence) |
| [python-audio-separator](https://github.com/nomadkaraoke/python-audio-separator) / [UVR](https://github.com/Anjok07/ultimatevocalremovergui) model lists | 29.10.2026 / 06.10.2026 | Every community separation model (MDX-Net, VR, Demucs, BS/Mel-RoFormer, SCNet) | Practical, complete | Weights are `.ckpt`/`.pth`/ONNX, mostly unlicensed or CC BY-NC |
| [ZFTurbo Music-Source-Separation-Training](https://github.com/ZFTurbo/Music-Source-Separation-Training) + MVSEP quality tables | 12.11.2026 | Separation architectures, SDR tables | Reference for RoFormer quality | Weights hosted as GitHub release `.ckpt` |
| [Nuo Stems "separation quality" page](https://docs.nuo-stems.com/docs/stems-separation-quality) | – | Comparison of stem models (recommended on HN, 29.08.2026) | Readable, listening-oriented | Vendor page |
| [SongEval](https://github.com/ASLP-lab/SongEval) | 08.04.2026 | Song aesthetic scoring toolkit (Apache 2.0 code) | Used as a benchmark by song models | Weights not checked; benchmark, not a user tool |
| [wildminder/awesome-ai-voice](https://github.com/wildminder/awesome-ai-voice) | 04.11.2026 | TTS, voice cloning, music generation | Current | Light on symbolic music and analysis |
| [Curated-Awesome-Lists/awesome-ai-music-generation](https://github.com/Curated-Awesome-Lists/awesome-ai-music-generation) | 04.09.2026 | General list | Broad | Mixes services and papers; not licence-aware |

## Taxonomy

| # | Category → sub-tasks | Typical uses | Covered by general models? | Licence and format pitfalls |
|---|---|---|---|---|
| 1 | **Full song generation with vocals and lyrics** → text + lyrics to song, cover, repaint, style LoRA | Songs from your own lyrics; occasion songs; demos of a melody | No | **Most strong models fail**: MiniMax Music 3 (custom community licence), YuE2 (CC BY-NC), SongGeneration/LeVo 2 (no licence, `.pt`), SongBloom (CC BY-NC-SA), DiffRhythm 2 (needs MuQ-MuLan, CC BY-NC). ACE-Step 1.5 (MIT) and HeartMuLa (Apache 2.0) pass |
| 2 | **Instrumental text-to-music** → loops, backing tracks, styles | Backing tracks to practise with, video soundtracks | No | MusicGen, MAGNeT, JASCO: CC BY-NC; Stable Audio Open/3: Stability licence, gated; Magenta RealTime 2: CC BY 4.0 (not Apache or MIT; a community copy relabels it Apache) |
| 3 | **Symbolic composition / MIDI generation / sheet music** → continuation, infilling, accompaniment to a melody, text-to-MIDI, ABC/MusicXML scores | Develop a theme, harmonise a melody, get editable notes rather than audio | Partly (LLMs can write ABC/LilyPond, with limited success) | NotaGen MIT but `.pth` only; text2midi `.bin` only; MIDI-LLM Llama 3.2 licence; ChatMusician on LLaMA-2; MIDI-GPT CC BY-NC, gated; Moonbeam `.pt`; Orpheus `.pth`/pickle |
| 4 | **Accompaniment / arrangement / continuation / stem generation** → add a track to a recording, extend a song, extract and regenerate stems | Add drums or bass to a home recording, extend a sketch | No | Same as #1 and #3 |
| 5 | **Source separation** → vocals/instrumental, 4–6 stems, karaoke, de-reverb | Learn parts, karaoke, remix, clean a vocal before transcription | No | Community RoFormer fine-tunes have no licence and are `.ckpt`; UVR packs mix `.ckpt`/`.pth`/ONNX; SAM-Audio has the SAM licence and is gated; becruily "deux" CC BY-NC; anvuew GPL-3.0 |
| 6 | **Transcription audio → MIDI** → piano, multi-instrument, guitar tab | Get notes from a recording or from humming; feed #3 | No | YourMT3 `.ckpt` (code GPL-3.0); Transkun MIT but `.pt` in the pip package; TabCNN CC BY 4.0 |
| 7 | **Music understanding / tagging / captioning / embeddings** → describe, tag, search a library, Q&A on a track | Catalogue a music collection; caption songs to train a LoRA | Partly (speech models only) | MERT, MuQ: CC BY-NC; Music/Audio Flamingo: NVIDIA licence; Qwen3-Omni Captioner tagged "other"; CLAP v1 music `.bin` only |
| 8 | **Chord / beat / key / tempo detection** | Lead sheets, practice, DJ | No | BTC chords CC BY-NC-SA; madmom and Essentia model licences not checked |
| 9 | **Lyrics alignment and lyrics transcription** | Karaoke files (LRC), check the lyrics of generated songs | Partly (Whisper, Qwen3-ASR on separated vocals) | MMS forced aligner CC BY-NC |
| 10 | **Singing voice synthesis / conversion** → MIDI + lyrics → singing, change the singer | Hear a written vocal line sung | No | YingMusic CC BY-NC / CC BY 4.0; Vevo2 CC BY-NC-ND; Seed-VC GPL-3.0; RVC voice packs are mostly unlicensed clones of real singers. **Ethics**: never clone a real person's voice without consent |
| 11 | **Sound effects / foley** | Videos, games | No | MMAudio CC BY-NC (a "MIT" safetensors copy is mislabelled); Stable Audio 3 SFX gated; TangoFlux no licence tag; ThinkSound/PrismAudio `.ckpt`; Woosh CC BY-NC; HunyuanVideo-Foley own licence; MOSS-SoundEffect Apache 2.0 but its VAE is `.pth` |
| 12 | **Restoration / super-resolution / mastering** → bandwidth extension, declip, reference mastering | Old recordings, MP3s, mastering a song | No | Apollo CC BY-SA; FlashSR `.pth`; AudioSR MLX ports CC BY-NC; matchering is GPL-3.0 (a tool, no model) |
| 13 | **Notation, engraving and MIDI rendering** (tools, not models) | Print scores, play back MIDI | No | MuseScore, LilyPond GPL (tools, fine); General MIDI SoundFont licences vary |
| 14 | **Lyrics writing** | Songwriting | **Yes** (LLMs) | – |
| 15 | **AI-music detection, plagiarism and similarity checks** | "Is this too close to an existing song?" | No | Immature, research-only |
| 16 | **Real-time jamming** (live MIDI → audio) | Play with an AI band | No | Magenta RealTime 2 CC BY 4.0; Aria real-time demo (piano, MLX) passes |

**Cross-cutting notes**:
- A strict policy (Apache/MIT, safetensors/GGUF) excludes most of the separation and transcription ecosystem (`.ckpt`/`.pth`, no licence) and several of the best song models (MiniMax Music 3, YuE2, LeVo 2). Community repacks and GGUF conversions solve the format problem (Comfy-Org, mlx-community, cstr/CrispASR). **Check every repack's licence against the upstream**: some relabel CC BY-NC or custom weights as MIT/Apache.
- **Languages**: ACE-Step 1.5 claims 50+ lyric languages (FR and DE included). HeartMuLa, HeartTranscriptor and MOSS-Music cover zh/en (plus ja/ko/es for HeartMuLa): **no FR/DE**.

## Hacker News comments used

Algolia API, comments only, exact matching. Window: since 13.11.2025 for 2026 models (launch discussions included), since 13.05.2026 for older models and tools.

- ACE-Step 1.5 praised as great and, at 1.5B parameters, very easy to run locally ([falloon, 17.02.2026](https://news.ycombinator.com/item?id=47051106)).
- ACE-Step 1.5 musicality far below commercial services; a big gap to Suno ([Rochus, 09.02.2026](https://news.ycombinator.com/item?id=46952916)).
- HeartMuLa: first results judged more promising than ACE-Step 1.5 ([popalchemist, 10.02.2026](https://news.ycombinator.com/item?id=46956303)).
- Uses ACE-Step via ComfyUI on a Mac; renders mean 5–10 min of heat ([vorticalbox, 16.04.2026](https://news.ycombinator.com/item?id=47791107)).
- M4 Max: an 8 s ACE-Step clip in 15 s ([sawfwair, 30.07.2026](https://news.ycombinator.com/item?id=49112047)).
- AceStep XL said to be trained on an open dataset (a user's claim, not verified) ([dahrkael, 28.05.2026](https://news.ycombinator.com/item?id=48305231)).
- YuE2 (CC BY-NC) sounds cleaner than MiniMax Music 3, but its songs are very bland and do not develop ([halyconWays, 11.09.2026](https://news.ycombinator.com/item?id=49654504)). Also described as a much stronger Band-in-a-Box, making melodically accurate covers of old MIDI tracks ([vunderba, 17.09.2026](https://news.ycombinator.com/item?id=49734955)). Takes sheet music as ABC notation, and ran on a Mac M1 ([vunderba, 11.09.2026](https://news.ycombinator.com/item?id=49653194)).
- The Anticipatory Music Transformer from Stanford recommended with enthusiasm ([bravura, 20.08.2026](https://news.ycombinator.com/item?id=49377302)).
- Piano autocomplete with a small MIDI LM: results no better, or worse, than a Markov model; suggests working on a harmonic/melodic layer instead ([rajivayyangar, 20.08.2026](https://news.ycombinator.com/item?id=49377995)).
- Advanced LLMs know LilyPond and music theory and can check counterpoint errors, but had limited success expanding jazz lead sheets ([tunesmith, 14.07.2026](https://news.ycombinator.com/item?id=48902741)).
- Asked to OCR sheet music to MusicXML/LilyPond, Opus produces nonsense ([indiv0, 23.06.2026](https://news.ycombinator.com/item?id=48645552)). Optical music recognition and AI reading of scores are very poor ([peatmoss, 23.06.2026](https://news.ycombinator.com/item?id=48644574)).
- Prefers MuseScore's autoplay and instant feedback over LilyPond ([quacked, 14.07.2026](https://news.ycombinator.com/item?id=48905377)).
- Magenta RealTime 2 with live MIDI input is fun to play with ([speedgoose, 20.08.2026](https://news.ycombinator.com/item?id=49374837)).
- mel_band_roformer and bs_roformer are excellent stem separation models, the best one user has heard ([Stitch4223, 29.08.2026](https://news.ycombinator.com/item?id=49490247)).
- htdemucs and the UVR models are good but not great, with many artifacts ([pdntspa, 29.08.2026](https://news.ycombinator.com/item?id=49492133)). The UVR community lives on Discord and spreadsheets and is not user-friendly ([adzm, 29.08.2026](https://news.ycombinator.com/item?id=49488167)).
- StemDeck: local 6-stem Demucs with Apple silicon MPS ([thclpr, 29.08.2026](https://news.ycombinator.com/item?id=49486082)). Separating overlapping instruments is still the hard part ([0n0n0m0uz, 31.08.2026](https://news.ycombinator.com/item?id=49514057)).
- Demucs converted to CoreML on the Neural Engine: 60 s → 10 s ([whstl, 13.10.2026](https://news.ycombinator.com/item?id=50072357)). A desktop app with Whisper + Demucs runs fully offline ([fatihserhattura, 26.10.2026](https://news.ycombinator.com/item?id=50242339)).
- Basic Pitch / NeuralNote: building the standalone Mac app was easy ([abhikul0, 25.05.2026](https://news.ycombinator.com/item?id=48263994)).
- MOSS-Audio (same backbone as MOSS-Music) feels good, but does not give useful feedback for music practice out of the box ([sbrother, 11.08.2026](https://news.ycombinator.com/item?id=49251874); [16.09.2026](https://news.ycombinator.com/item?id=49721981)).
- Nothing found on HN for NotaGen, text2midi, MIDI-LLM, MOSS-Music, SoulX-Singer, MMAudio, AudioSR, matchering, Transkun or MT3 within the window.

## Candidates by category

Commits are the first 12 characters read on 13.11.2026; re-read the full commit when pinning. Sizes are those of the useful files. "Formats" is what the repo contains.

### 1. Full song generation with vocals and lyrics

| Repo | Licence (HF API) | Gated | Formats | Size | Date / lastModified | Commit | Mac runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **`Comfy-Org/ACE-Step-1.5`** (repack of ACE-Step 1.5 + XL) | apache-2.0 (upstream MIT; both allowed) | no | safetensors only | XL-sft bf16 9.97 + XL-base bf16 9.97 + LM 4B 8.38 + Qwen 0.6B 1.19 + VAE 0.34 = **29.85 GB** if only these files are taken (repo 63.1 GB); or turbo AIO 10.03 GB alone | 03.02.2026 / 28.10.2026 | `371bb1680f8c` | ComfyUI native (MPS) | See ACE-Step feedback below | **Recommended.** Safetensors only. XL-base is needed for lego/extract/complete (#4) |
| `ACE-Step/Ace-Step1.5` + `acestep-v15-xl-sft` + `acestep-v15-xl-base` + `acestep-5Hz-lm-4B` (official) | mit | no | safetensors + `.py` + `silence_latent.pt` (3.8 MB) | 10.03 + 19.95 + 19.95 + 8.38 = 58.3 GB (XL in fp32, HF #11) | 23.01.2026 / XL 07.04.2026 | `19671f406d60`, `d06de46b4622`, `220c1166efbd`, `0a3ec94b557a` | Official app: **native MLX on macOS** (`start_gradio_ui_macos.sh`), also MPS; acestep.cpp (MIT) | GitHub #1114 (19.04.2026): vocals correct but lifeless, weak dynamics; a comment of 04.08.2026 reproduces it on an M4 Max (MPS) and traces it to the `shift` setting. HF #31 (03.10.2026): blind test vs Stable Audio 3, ACE-Step preferred 4 times out of 5 (one tie). HF XL-turbo #12 (09.06.2026, in Chinese): many Chinese words mispronounced, long fixes with REPAINT. GitHub #1280 (29.07.2026): project seen as abandoned, many UI bugs; reply (07.08.2026): ComfyUI gives better quality. HF #27 (09.11.2026): maintainer will add an MIT LICENSE file to the weights repo, commercial use allowed | **Note**: the native MLX app also needs `silence_latent.pt` (pickle) and Python code |
| **`HeartMuLa/HeartMuLa-RL-oss-3B-20260123`** + `HeartMuLa/HeartCodec-oss-20260123` | apache-2.0 | no | safetensors only | 15.75 + 6.64 = **22.4 GB** | 23.01.2026 | `fc0eff19a204`, `f889dab0532c` | heartlib (Apache 2.0) on **MPS is buggy** (#56 22.01.2026; #85 needs triton; MPS PR #23 still open). Community MLX port `uplg/mulan` (no licence) works well and fast on an M1 Max (#118, 20.06.2026) | HN 10.02.2026: more promising than ACE-Step 1.5. HF #3 (26.01.2026): same kind of music regardless of tags. RL version judged better (HF RL #1, 23.01.2026) | Alternative. **No FR/DE lyrics** (zh, en, ja, ko, es). The plain `HeartCodec-oss` repo returns 401; use the dated one |
| `MiniMaxAI/MiniMax-Music3` | none in metadata; **LICENSE = "MiniMax-Music3 Community License"** (custom) | no | safetensors + `.pth` (VAE 9.8 GB) | 57 GB | 07.08.2026 / 26.10.2026 | `1b525ccb685a` | mlx-audio (mlx-community 4/6/8-bit, licence "other") | HN 11.09.2026: less clean than YuE2 | **Excluded** (custom licence). `Comfy-Org/MiniMax-Music-3` is tagged apache-2.0: **mislabelled** |
| `m-a-p/YuE2-3B` | cc-by-nc-4.0 | no | safetensors | 7.26 GB | 09.09.2026 | `8f24312f1877` | ComfyUI-YuE2, ran on an M1 (HN) | Most interesting for composition (symbolic planning, ABC input, MIDI covers) | **Excluded** (non-commercial). YuE v1 repos are Apache 2.0, but their `xcodec_mini_infer` codec is `.pth`/`.bin` → flagged |

- Also excluded: `ASLP-lab/DiffRhythm2` (Apache 2.0 but has a `.bin`, and needs MuQ-MuLan, CC BY-NC), `lglg666/SongGeneration-v2-large` (LeVo 2: licence "unknown", `.pt` only), SongBloom (CC BY-NC-SA upstream; safetensors copies have no licence), `declare-lab/JAM-0.5` ("other"), `stabilityai/stable-audio-3-*` ("other", gated).
- Recommendation: **ACE-Step 1.5 XL via `Comfy-Org/ACE-Step-1.5`**, then HeartMuLa-RL 3B as an alternative (no FR/DE lyrics).

### 2. Instrumental text-to-music

No separate compliant model. ACE-Step 1.5 does instrumentals (tip from HF #31: name a lead instrument first in the caption). Excluded: MusicGen/MAGNeT/JASCO (CC BY-NC), Stable Audio 3 small-music (Stability licence, gated), Magenta RealTime 2 (CC BY 4.0; `magenta-community/magenta-realtime-2` is relabelled Apache 2.0 without basis).
Recommendation: covered by #1.

### 3. Symbolic composition / MIDI generation / sheet music

| Repo | Licence | Gated | Formats | Size | Date | Commit | Mac runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **`stanford-crfm/music-large-800k`** (Anticipatory Music Transformer, 780M) | apache-2.0 | no | safetensors | 3.12 GB | 13.03.2024 | `e206a88d4658` | `anticipation` package (Apache 2.0, updated 19.07.2026), transformers; MPS not verified | HN 20.08.2026: praised. HF #1 (22.09.2025): missing tokenizer file | **Recommended.** Accompaniment to a given melody and infilling, multi-instrument MIDI. Old but unmatched among compliant models |
| **`loubb/aria-medium-base`** (EleutherAI Aria, 1B, piano) | apache-2.0 | no | safetensors (+ `.py`, `.tar.gz` to leave out) | `model-gen.safetensors` 2.63 GB (+ `model-demo` 2.45 GB for the real-time demo; repo 7.72 GB) | 05.06.2025 / 13.04.2026 | `5a1ef36c5007` | `aria` package (Apache 2.0): **native MLX**, plus a real-time MLX piano-continuation demo (CoreMIDI) | No user reports | **Recommended.** Expressive solo-piano continuation of your own MIDI; take only `model-gen.safetensors` |
| `skytnt/midi-model-tv2o-medium` | apache-2.0 | no | safetensors (+ `.bin`, `.onnx` to leave out) | 0.47 GB | 31.10.2024 | `0f8f265d4330` | PyTorch/ONNX "midi-composer" app; MPS not verified | None found | Optional. Multi-track MIDI generation/continuation, light |
| Local LLM writing ABC / LilyPond / MusicXML (general LLMs) | – | – | – | 0 | – | – | + tools in #13 | HN: limited success; scores are hard for LLMs (14.07.2026, 23.06.2026) | Free path for lead sheets and harmony checks; expect errors |

- Excluded: NotaGen / NotaGen-X (MIT but `.pth` only), text2midi (`.bin`/`.pkl`), MIDI-LLM (Llama 3.2 licence), ChatMusician (LLaMA-2 base), MIDI-GPT (CC BY-NC, gated), Moonbeam (`.pt`), Orpheus Music Transformer (`.pth`/pickle), SongComposer (`.bin`, InternLM base), musiclang (GPL-3.0/none), YuE2 (CC BY-NC).
- Recommendation: **Anticipatory Music Transformer large + Aria**, with the LLM route for scores.

### 4. Accompaniment / arrangement / continuation / stems

No extra download. ACE-Step 1.5 **XL-base** provides lego (add a track), extract (stems), complete (continue) and repaint/cover. Symbolic accompaniment: Anticipatory Music Transformer (#3). Piano continuation: Aria (#3).
Recommendation: ACE-Step 1.5 XL-base (#1).

### 5. Source separation

| Repo | Licence | Gated | Formats | Size | Date | Commit | Mac runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **`cstr/mel-band-roformer-vocals-GGUF`** (Kimberley Jensen weights, MIT) | mit | no | gguf | 0.46 GB | 19.07.2026 / 02.08.2026 | `d6909215e1d7` | CrispASR (MIT), Metal | RoFormer family judged the best (HN 29.08.2026). CrispASR #568 (02.11.2026): another RoFormer gives silent vocals on Metal, so test with a known song | **Recommended** for vocals/instrumental |
| **`mlx-community/demucs-mlx-fp16`** (all 8 Demucs models) | mit | no | safetensors (+ export `.py`) | htdemucs_ft 0.34 + htdemucs_6s 0.06 = **0.39 GB** if only these files are taken (repo 3.36 GB) | 16.03.2026 | `908d2d05cf30` | MLX: `mlx-audio-separator` (MIT code; #4 near-silent stems on macOS 27, fixed 22.09.2026); Demucs PyTorch MPS | Good but not great, artifacts (HN 29.08.2026); widely used offline (HN 26.10.2026) | **Recommended** for 4 and 6 stems |
| `ssmall256/mlx-audio-separator` (BS-RoFormer-SW 6-stem, Mel-RoFormer InstV7n, HTDemucs…) | **unknown** | no | safetensors | 0.70 GB (BS-RoFormer-SW) … 2.70 GB (all) | 11.10.2026 | `679ec88c16a2` | MLX native | None | **Flag**: best 6-stem option on MLX, licence not stated |
| `Kijai/MelBandRoFormer_comfy` | none (upstream MIT) | no | safetensors | 0.46 GB fp16 | 23.08.2025 | `7dc5fa7824f1` | ComfyUI node (no licence) | HF #1: quality judged excellent | **Flag**: no licence tag; the cstr GGUF covers the same weights with MIT |

- Excluded: community BS/Mel-RoFormer fine-tunes (no licence, `.ckpt`), becruily "deux" (CC BY-NC), anvuew de-reverb/karaoke (GPL-3.0), UVR/audio-separator packs (`.ckpt`/`.pth`/ONNX), SCNet repos, SAM-Audio (SAM licence, gated).
- Recommendation: **Mel-RoFormer vocals GGUF + Demucs MLX (htdemucs_ft, htdemucs_6s)**.

### 6. Transcription audio → MIDI

| Repo | Licence | Gated | Formats | Size | Date | Commit | Mac runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **`cstr/mt3-GGUF`** (Magenta MT3, multi-instrument) | apache-2.0 | no | gguf | 0.10 GB | 02.09.2026 | `4299d5f308dc` | CrispASR `--backend mt3`, Metal | None | **Recommended** (bands, ensembles) |
| **`cstr/hft-transformer-GGUF`** (piano) | mit | no | gguf | 0.03 GB | 23.09.2026 | `17d72a2429f1` | CrispASR | None; CrispASR: 70.5 % note F1 on MusicNet piano, slow | **Recommended** for piano |
| `cstr/onsets-and-frames-GGUF` (piano) | mit | no | gguf | 0.16 GB | 22.09.2026 | `e19fdd5dab82` | CrispASR | None; 69.0 % F1, faster | Optional |
| `cstr/basic-pitch-GGUF` | apache-2.0 | no | gguf | < 1 MB | 30.08.2026 | `49d4c2ef90d5` | CrispASR; or `pip install basic-pitch` (a tool) | Mac app easy to build (HN 25.05.2026, NeuralNote) | Optional: any instrument, humming |

- Excluded: YourMT3 / YourMT3+ (`.ckpt`, code GPL-3.0), Transkun (`.pt` in the pip package), `xavriley/midi-transcription-models` (mostly `.pth`), ByteDance piano transcription original (`.pth`).
- Recommendation: **CrispASR + MT3 + hFT-Transformer GGUF** (≈ 0.13 GB).

### 7. Music understanding / tagging / captioning / embeddings

| Repo | Licence | Gated | Formats | Size | Date | Commit | Mac runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **`mlx-community/MOSS-Music-8B-Thinking-8bit`** | apache-2.0 | no | safetensors | 10.22 GB | 27.06.2026 | `7b2c41e689a4` | **mlx-audio** | No MOSS-Music reports; MOSS-Audio good but not enough out of the box (HN 11.08.2026) | **Recommended**: captioning, structure, chord/key/tempo, lyrics ASR with timestamps (en/zh) |
| `OpenMOSS-Team/MOSS-Music-8B-Instruct` | apache-2.0 | no | safetensors + `.py` (remote code) | 18.11 GB | 21.04.2026 / 01.05.2026 | `fce7f8304e96` | SGLang/transformers | None | Alternative (bf16 original) |
| `ACE-Step/acestep-captioner` (Qwen2.5-Omni-7B fine-tune) | mit | no | safetensors (+ tiny `.pt`) | 22.36 GB | 23.01.2026 | `7109e9af1c6c` | transformers, MPS not verified | – | Optional: captions for ACE-Step LoRA training |
| `laion/clap2-large-audioxl-s1B` | apache-2.0 | no | safetensors | 2.72 GB | 26.10.2026 / 12.11.2026 | `1fc47b9ed155` | transformers | None (3 weeks old) | Optional: text ↔ audio search in a library |

- Excluded: MERT, MuQ, MuQ-MuLan (CC BY-NC), Music Flamingo and Audio Flamingo (NVIDIA licence), Qwen3-Omni Captioner ("other"), `laion/larger_clap_music` (`.bin` only), Audiobox Aesthetics (CC BY 4.0).
- Recommendation: **MOSS-Music 8B Thinking 8-bit (MLX)**.

### 8. Chord / beat / key / tempo

| Repo | Licence | Gated | Formats | Size | Date | Commit | Mac runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **`cstr/beat-this-GGUF`** (CPJKU Beat This!, ISMIR 2024) | mit | no | gguf | 0.12 GB | 20.07.2026 | `aa82ae3fc3a4` | CrispASR `--beats` | None | **Recommended** for beats and downbeats |
| MOSS-Music (see 7) | apache-2.0 | – | – | – | – | – | mlx-audio | – | Chords and key by question |
| ACE-Step 1.5 built-in analysis (see 1) | mit | – | – | – | – | – | – | – | BPM, key, time signature |

- No compliant dedicated chord model: BTC is CC BY-NC-SA; madmom and Essentia model licences not checked. Tool: librosa (ISC) for tempo and key.
- Recommendation: **Beat This GGUF + MOSS-Music**.

### 9. Lyrics alignment and lyrics transcription

| Repo | Licence | Gated | Formats | Size | Date | Commit | Mac runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| MOSS-Music (see 7) | apache-2.0 | – | – | – | – | – | mlx-audio | – | **Recommended**: lyrics ASR with timestamps (claimed), en/zh |
| `HeartMuLa/HeartTranscriptor-oss` | apache-2.0 | no | safetensors | 3.06 GB | 14.01.2026 / 19.01.2026 | `918f88917c17` | heartlib (MPS issues) | None | Alternative; zh/en/ja/ko/es |
| `Qwen/Qwen3-ForcedAligner-0.6B` | apache-2.0 | no | safetensors | 1.84 GB | 28.01.2026 | `c7cbfc2048c4` | mlx-audio | Speech aligner; untested on singing | Optional: align known FR/DE lyrics on a separated vocal (#5); already has a record (`models/qwen3-forcedaligner-0.6b.json`) |
| `ACE-Step/acestep-transcriber` | mit | no | safetensors | 22.36 GB | 23.01.2026 | `53062cf7d0e0` | transformers | None | Not recommended (size) |

- Excluded: MMS-300m forced aligner (CC BY-NC).
- Recommendation: **MOSS-Music**, plus Qwen3-ForcedAligner for FR/DE lyrics.

### 10. Singing voice synthesis / conversion

| Repo | Licence | Gated | Formats | Size | Date | Commit | Mac runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **`mlx-community/SoulX-Singer-bf16`** (SVS + SVC weights) | apache-2.0 | no | safetensors | 2.81 GB | 31.05.2026 | `09d874592571` | `ailuntx/SoulX-Singer-MLX` (still uses the PyTorch model structure) | Thin: upstream HF #3 found it very useful (15.02.2026); #7 (29.10.2026) asks how to sing from MIDI + text | Candidate: sings a MIDI line with lyrics. Upstream `Soul-AILab/SoulX-Singer` is `.pt` only |

- Excluded: YingMusic-Singer/SVC (CC BY-NC; Plus CC BY 4.0), Vevo2 (CC BY-NC-ND), Seed-VC (GPL-3.0), RVC voice packs, DiffSinger community voices.
- **Ethics**: use your own voice or synthetic voices; never clone a real singer without consent.
- Recommendation: **SoulX-Singer bf16 (MLX)**.

### 11. Sound effects

Only `OpenMOSS-Team/MOSS-SoundEffect-v2.0` (Apache 2.0, `e35df4d82fbe`) is close, but its required VAE is `vae/vae_128d_48k.pth` (1.49 GB): **flagged**. `ilintar/moss-soundeffect-gguf` (Apache 2.0, 7.06 GB, `b5556f201d62`) packs everything as GGUF but needs the `pwilkin/openmoss` C++ runtime, not checked on the Mac. No HN feedback.

### 12. Restoration / super-resolution / mastering

| Repo / tool | Licence | Gated | Formats | Size | Date | Commit | Mac runtime | Feedback | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| `drbaph/AudioSR` (safetensors of AudioSR; upstream code MIT, `haoheliu/audiosr_basic` Apache 2.0) | mit | no | safetensors | `audiosr_basic_fp32` 6.18 GB | 08.01.2026 / 27.01.2026 | `f07b25d4b7e5` | ComfyUI-AudioSR (MIT), MPS not verified; 50–100 diffusion steps | None | Candidate: MP3 / low-bandwidth → 48 kHz |
| matchering (tool) | GPL-3.0 | – | – | – | 07.10.2026 | – | Python, CPU | None in window | Tool: master a song against a reference track |

- Excluded: Apollo (CC BY-SA), FlashSR (`.pth`), `aufklarer/AudioSR-MLX-*` and FlashSR-MLX (CC BY-NC relabel), `haoheliu/audiosr_speech` (no licence).
- Recommendation: **matchering** (tool) for mastering; AudioSR for old or low-bandwidth recordings.

### 13. Notation, engraving and MIDI rendering (tools)

| Tool | Licence | Install | Verdict |
|---|---|---|---|
| **MuseScore 4** | GPL-3.0 | musescore.org (Homebrew not checked) | **Recommended**: edit MIDI/MusicXML, playback, print |
| **LilyPond** | GPL-3.0 | lilypond.org (Homebrew not checked) | Recommended for scores written by an LLM (text in, PDF out) |
| **music21** | BSD-3 | `uv pip install music21` | Python glue: ABC ↔ MusicXML ↔ MIDI, analysis |
| abcMIDI / abcm2ps | GPL | not checked | Small tools for ABC from LLMs |
| FluidSynth + a General MIDI SoundFont | LGPL; SoundFont licences vary | `brew install fluid-synth` | Render model MIDI to audio; needed by the Aria demo |

## Points to watch

- The official ACE-Step repos need `silence_latent.pt` (pickle) and `.py` files; the Comfy-Org repack avoids them.
- Two Mel-RoFormer conversions (`ssmall256/mlx-audio-separator`, `Kijai/MelBandRoFormer_comfy`) have no licence tag.
- Mislabelled repacks to avoid: Comfy-Org MiniMax-Music-3 (Apache 2.0 tag), magenta-community/magenta-realtime-2 (Apache 2.0 tag), Kijai/MMAudio_safetensors (MIT tag).
- New runtime: CrispASR (MIT, GGUF + Metal) for separation, transcription and beats.

**Third-party conversions**: the `cstr` GGUF files (Mel-RoFormer, MT3, hFT, Basic Pitch, Beat This), `drbaph/AudioSR` and the `mlx-community` builds (Demucs, MOSS-Music 8-bit, SoulX-Singer) are conversions published by individuals or an open community organisation, not by the original authors; check them with the method in [`../research-method.md`](../research-method.md#third-party-conversions) before relying on them. Official alternative for MOSS-Music: `OpenMOSS-Team/MOSS-Music-8B-Instruct` (Apache 2.0, 18.1 GB, no native MLX yet).
