# Glossary

Terms, software and organisations met when choosing and running open-weight AI models locally. Created on 14.11.2026; new terms are added as they come up.

Terms are sorted alphabetically within each section (case ignored, backticks and brackets ignored).

The translation columns are left empty when the English term is used as is in that language, or when a translation makes no sense (product and company names).

## Model basics

| Term | Explanation | French | German | Italian |
|---|---|---|---|---|
| Active parameters | The part of a MoE model used per token; it drives speed. | paramètres actifs | aktive Parameter | parametri attivi |
| Agent | A model that acts with tools (files, shell, web) to reach a goal, e.g. Claude Code, Goose. | agent | Agent | agente |
| B (billion) | Unit of the parameter count: 7B, 120B. | milliard (Md) | Milliarde (Mrd.) | miliardo (mld) |
| Base model | A model before instruction tuning: it continues text rather than answering. | modèle de base | Basismodell | modello base |
| Benchmark | A standard test used to compare models. | banc d'essai | Benchmark | benchmark |
| Context window | How many tokens a model can take into account at once. | fenêtre de contexte | Kontextfenster | finestra di contesto |
| Dense model | Every parameter is used for every token. | modèle dense | dichtes Modell | modello denso |
| Distillation | Training a small model to imitate a big one. | distillation | Destillation | distillazione |
| Fine-tune | A model trained further from another one, for a task or a language. | affinage, modèle affiné | Feinabstimmung, feinabgestimmtes Modell | fine-tuning, modello affinato |
| Hallucination | A confident but false answer. | hallucination | Halluzination | allucinazione |
| Inference | Running a model to get an answer (as opposed to training it). | inférence | Inferenz | inferenza |
| Instruct model | A model tuned to follow instructions and chat. | modèle instruct | Instruct-Modell | modello instruct |
| KV cache | Memory used to keep the context during generation; grows with the context length. | cache KV | KV-Cache | cache KV |
| LLM (large language model) | A model that reads and writes text. | grand modèle de langage | großes Sprachmodell | modello linguistico di grandi dimensioni |
| LoRA | A small add-on file that adapts a base model (often used for image models). | | | |
| MCP (Model Context Protocol) | Standard format to connect tools and data sources to agents. | | | |
| Model | A trained neural network: its architecture plus its weights. | modèle | Modell | modello |
| MoE (mixture of experts) | Only a few "experts" are active per token, e.g. 35B-A3B = 35B total, 3B active. Fast for its size, but all of it must fit in memory. | mélange d'experts | Mixture of Experts | miscela di esperti |
| MTP (multi-token prediction) | An extra model part that guesses several tokens at once to speed up generation (DeepSeek). | prédiction multi-jetons | Multi-Token-Vorhersage | previsione multi-token |
| Multimodal | A model that handles several kinds of input, e.g. text and images. | multimodal | multimodal | multimodale |
| Omni model | A model that takes and produces text, images and speech, e.g. real-time speech to speech. | modèle omni | Omni-Modell | modello omni |
| Open weights | Weights published for download; it does not imply that the training data or code are open. | poids ouverts | offene Gewichte | pesi aperti |
| Parameters | The number of weights, e.g. 7B = 7 billion. Gives a rough idea of size and memory needs. | paramètres | Parameter | parametri |
| Prompt | The text given to a model. | invite, prompt | Prompt, Eingabeaufforderung | prompt |
| Reasoning model | A model that "thinks" (writes intermediate steps) before answering. | modèle de raisonnement | Reasoning-Modell | modello di ragionamento |
| Speculative decoding | A small "draft" model proposes tokens that the big model checks; faster, same result. | décodage spéculatif | spekulatives Dekodieren | decodifica speculativa |
| System prompt | Standing instructions given to the model before the conversation. | prompt système | Systemprompt | prompt di sistema |
| Token | The unit of text a model reads and writes (a word piece). About 0.75 English words. | jeton | Token | token |
| Tokenizer | Converts text into tokens and back. | tokeniseur | Tokenizer | tokenizzatore |
| Tool call | A request from the model to run a tool. | appel d'outil | Tool-Aufruf | chiamata di strumento |
| Training | Learning the weights from data. | entraînement | Training | addestramento |
| VLM (vision language model) | An LLM that also reads images. | modèle vision-langage | Vision-Sprachmodell | modello visione-linguaggio |
| Weights | The learned numbers of a model, stored in large files. Downloading a model means downloading its weights. | poids | Gewichte | pesi |

## Files, formats and quantisation

| Term | Explanation | French | German | Italian |
|---|---|---|---|---|
| BF16 / FP16 | 16-bit weights: full quality, large files. | | | |
| Checkpoint | A saved state of the weights. | point de contrôle | Checkpoint | checkpoint |
| `config.json` | Describes the architecture of a model. | | | |
| Diffusers | Hugging Face library and folder layout for image models (`unet/`, `vae/`, `text_encoder/`). | | | |
| FP32 | 32-bit floating point: full precision, twice the size of BF16 / FP16. | | | |
| FP8 | 8-bit floating-point weights. | | | |
| GGUF | Single-file weight format of llama.cpp and Ollama, usually quantised; data only (weights and the metadata needed to load them, no executable code). "GG" are the initials of Georgi Gerganov, author of llama.cpp and of its tensor library GGML; the full name is often given as "GPT-Generated Unified Format", but the specification gives no official expansion. Successor of the older GGML and GGJT files. | | | |
| imatrix (importance matrix) | Statistics used to choose what to keep precise when quantising. | matrice d'importance | Wichtigkeitsmatrix | matrice di importanza |
| IQ2_XXS, IQ2_M | Very low (≈ 2-bit) "importance" quantisations of llama.cpp; they need an importance matrix. | | | |
| Model card | The `README.md` of a Hugging Face repository: description, licence, use. | fiche du modèle | Modellkarte | scheda del modello |
| NOTICE file | File that lists the authors and original licences of the work a repository is derived from. | fichier NOTICE | NOTICE-Datei | file NOTICE |
| NPZ (`.npz`) | NumPy archive of arrays; data only if loaded without `allow_pickle`. | | | |
| ONNX | Open format for exchanging models between frameworks. | | | |
| Pickle (`.bin`, `.pt`, `.pth`, `.ckpt`, `.pkl`) | Python format that can run code when loaded, hence a security risk. Prefer safetensors or GGUF. | | | |
| PTQ (post-training quantisation) | Quantisation applied after training, without retraining. | quantification après entraînement | Quantisierung nach dem Training | quantizzazione post-addestramento |
| Q8_0, Q4_K_M, Q4K | GGUF quantisation levels: the number is the bits per weight; K = "k-quant" method. | | | |
| Quantisation | Storing weights with fewer bits (e.g. 4 instead of 16) to save memory, at some cost in quality. | quantification | Quantisierung | quantizzazione |
| Remote code (`.py` in a repository) | Python files a library runs when loading the model (`trust_remote_code`); they can run anything, so they are a security risk. | code distant | Remote-Code | codice remoto |
| Repack | Rewrites weights into another file layout without changing their values (no requantisation). | réemballage | Umpacken | riconfezionamento |
| safetensors | Safe weight format: data only, no executable code. | | | |
| Safetensors header | Start of a safetensors file listing tensor names, shapes and types; readable through the Hugging Face API without downloading the weights. | en-tête safetensors | Safetensors-Header | intestazione safetensors |
| Shard | One part of a model split into several files (`model-00001-of-00004.safetensors`). | fragment | Teil, Shard | frammento |
| Third-party conversion | Copy of a model converted by someone other than its publisher (e.g. to MLX or safetensors); trusted only after checking its provenance. | conversion tierce | Drittanbieter-Konvertierung | conversione di terzi |
| TorchScript | Compiled PyTorch model format; a pickle-based file. | | | |
| UD (Unsloth Dynamic) | Unsloth's quantisation that keeps the sensitive layers at higher precision. | | | |

## Kinds of models (tasks)

| Term | Explanation | French | German | Italian |
|---|---|---|---|---|
| ASR (automatic speech recognition) | Speech to text, transcription. | reconnaissance automatique de la parole | automatische Spracherkennung | riconoscimento automatico del parlato |
| Background removal (matting) | Cuts out the subject of an image. | détourage | Freistellen | scontornatura |
| Baseline (seasonal naive) | Simple reference forecast, e.g. repeating last week or last year; a forecasting model is useful only if it beats it. | prévision de référence (naïve saisonnière) | Referenzprognose (saisonal naiv) | previsione di riferimento (naïve stagionale) |
| Code completion (FIM) | Completes code at the cursor; FIM = fill in the middle. | autocomplétion de code | Code-Vervollständigung | completamento del codice |
| Colourisation | Adds colours to a black-and-white photo. | colorisation | Kolorierung | colorazione |
| Covariates | Extra series known to influence the forecast (prices, holidays, weather). | covariables | Kovariaten | covariate |
| CRPS, MASE | Error measures for forecasts: CRPS for probabilistic forecasts, MASE relative to a naive forecast; lower is better. | | | |
| Diarisation | Who speaks when, in a recording. | segmentation par locuteur | Sprecherdiarisierung | diarizzazione |
| Diffusion model | Image (or sound) model that builds the result by removing noise step by step. | modèle de diffusion | Diffusionsmodell | modello di diffusione |
| Embedding | The vector produced by an embedding model. | plongement, vecteur | Einbettung | embedding, vettore |
| Embedding model | Turns a text or image into a vector of numbers, to search by meaning. | modèle de plongement | Embedding-Modell | modello di embedding |
| Face restoration | Repairs blurred or damaged faces. | restauration de visages | Gesichtsrestaurierung | restauro dei volti |
| Guard model | Classifies a prompt or answer as safe or unsafe. | modèle garde-fou | Schutzmodell | modello di guardia |
| Image editing | Changes an existing image from an instruction. | retouche d'image | Bildbearbeitung | modifica di immagini |
| Image quality assessment (IQA) | Scores the quality of an image, and explains it. | évaluation de la qualité d'image | Bildqualitätsbewertung | valutazione della qualità delle immagini |
| Layout analysis | Finds the blocks of a page (titles, paragraphs, tables, figures) and their reading order, before OCR. | analyse de mise en page | Layoutanalyse | analisi del layout |
| Machine translation (MT) | Automatic translation. | traduction automatique | maschinelle Übersetzung | traduzione automatica |
| Mastering | Final balancing of a track's loudness and tone (matchering). | matriçage, mastering | Mastering | mastering |
| MIDI | Format that stores notes, not sound. | | | |
| Object removal (inpainting) | Erases an object and fills the hole. | effacement d'objet, retouche | Objektentfernung, Inpainting | rimozione di oggetti, inpainting |
| OCR | Reading text from images or scanned documents. | reconnaissance optique de caractères | Texterkennung | riconoscimento ottico dei caratteri |
| Prompt injection | Hidden instructions in a document or web page that try to take control of an agent. | injection de prompt | Prompt-Injection | prompt injection |
| Quantile forecast | Forecast given as a range (e.g. 10 %, 50 %, 90 % quantiles) instead of a single value. | prévision par quantiles | Quantilprognose | previsione per quantili |
| RAG (retrieval-augmented generation) | Search your documents, then give the passages found to the LLM. | génération augmentée par récupération | abrufgestützte Generierung | generazione aumentata dal recupero |
| Reranker | Re-orders search results by relevance to a question. | reclasseur | Reranker | riordinatore |
| Segmentation | Selects the pixels of an object (SAM). | segmentation | Segmentierung | segmentazione |
| SoundFont | A bank of instrument sounds used to play MIDI (FluidSynth). | banque de sons | | |
| Source separation (stems) | Splits a song into voice, drums, bass, etc. | séparation de sources | Quellentrennung | separazione delle sorgenti |
| Symbolic music model | Works on notes (MIDI) rather than on audio, e.g. Aria, Anticipatory Music Transformer. | modèle de musique symbolique | symbolisches Musikmodell | modello musicale simbolico |
| Text encoder | The part of an image or music model that reads the prompt. | encodeur de texte | Text-Encoder | codificatore di testo |
| Text to image | Generates an image from a description. | texte vers image | Text-zu-Bild | testo in immagine |
| Time series forecasting | Predicts future values of numerical data. | prévision de séries temporelles | Zeitreihenprognose | previsione di serie temporali |
| TTS (text to speech) | Speech synthesis. | synthèse vocale | Sprachsynthese | sintesi vocale |
| UCI (Universal Chess Interface) | Standard protocol between a chess engine and a chess program. | | | |
| Upscaling (super-resolution) | Enlarges an image while adding detail. | agrandissement, super-résolution | Hochskalierung | upscaling, super-risoluzione |
| VAE | The part of an image model that converts between pixels and the compact internal form. | | | |
| Vector database | Stores embeddings and finds the nearest ones. | base de données vectorielle | Vektordatenbank | database vettoriale |
| Vectorisation | Converts a bitmap image to vector shapes (SVG); VTracer. | vectorisation | Vektorisierung | vettorizzazione |
| Voice cloning | TTS that imitates a voice from a short recording. | clonage de voix | Stimmklonen | clonazione vocale |
| Voice design | TTS that creates a new voice from a text description ("calm, low, older man"). | conception de voix | Stimmdesign | progettazione vocale |

## Software and runtimes

| Term | Explanation | French | German | Italian |
|---|---|---|---|---|
| caffeinate | macOS command that prevents sleep during a long task. | | | |
| Claude Code | Anthropic's coding agent, used in the terminal. | | | |
| ComfyUI | Node-based application to run image, video and music models. | | | |
| ditto | macOS copy command that keeps all file attributes. | | | |
| DwarfStar (`antirez/ds4`) | Runtime by antirez for DeepSeek V4 on Apple Silicon. | | | |
| FluidSynth | Plays MIDI with a SoundFont. | | | |
| Goose | Open-source agent that runs on your machine and uses MCP tools. | | | |
| Hermes Agent | Open-source personal assistant agent; hermes-webui is a web interface for it. | | | |
| Homebrew (`brew`) | Package manager for macOS. | | | |
| Hugging Face Hub | The site and service that hosts most open models. | | | |
| `huggingface_hub` | Python library to read and download from the Hub (`model_info`, `snapshot_download`). | | | |
| llama.cpp | Reference runtime for GGUF models; `llama-server` gives an API. | | | |
| LM Studio | Desktop application to run LLMs (llama.cpp and MLX). | | | |
| Maia | Chess engine trained to play like humans of a given rating (CSSLab). | | | |
| matchering | Automatic mastering against a reference track. | | | |
| mflux | Runs image models (Flux, Qwen-Image…) with MLX on a Mac. | | | |
| MLX, mlx-lm | Apple's machine-learning library for Apple Silicon, and its LLM runner. | | | |
| mlx-audio | MLX library for speech recognition and synthesis on Apple Silicon. | | | |
| mlx-vlm | MLX library for vision language models and some vision models on Apple Silicon. | | | |
| MuseScore, LilyPond | Music notation software (scores). | | | |
| music21 | Python library to analyse and convert music (MIDI, MusicXML). | | | |
| ntfy | Push notification service. | | | |
| Ollama | Easy runtime for LLMs, built on llama.cpp; has its own model library and storage (`blobs`). | | | |
| Runtime (inference engine) | The program that loads a model and runs it. | moteur d'inférence | Inferenz-Engine | motore di inferenza |
| shasum | Computes file hashes (SHA-256) to check files. | | | |
| Stockfish | Strongest open-source chess engine. | | | |
| Strata | Open-source runtime (MIT) built for Qwen3.8-Flash-Next, also DeepSeek V4.1-Flash; streams weights from the SSD when memory is short; Metal, CUDA and AMD builds. | | | |
| Tailscale | Private network (VPN) between your devices. | | | |
| Transformers | Hugging Face's Python library to run models. | | | |
| uv | Fast Python package and project manager; `uv run` runs a script with its dependencies. | | | |
| vLLM | High-throughput LLM server, mainly for NVIDIA GPUs. | | | |
| VTracer | Converts bitmap images to SVG. | | | |
| whisper.cpp | Runtime for Whisper speech recognition. | | | |

## Organisations and publishers

| Term | Explanation | French | German | Italian |
|---|---|---|---|---|
| AllenAI (Ai2) | United States. Non-profit research institute; publisher of olmOCR. | | | |
| Amazon | United States. Publisher of Chronos (time series). | | | |
| antirez | Italy. Salvatore Sanfilippo, creator of Redis; publishes DeepSeek V4 GGUF files and DwarfStar. | | | |
| Baidu | China. Publisher of PaddlePaddle models and Unlimited-OCR. | | | |
| ByteDance | China. Publisher of EvoQuality and Q-Insight. | | | |
| Comfy-Org | United States. ComfyUI team; repackages models for ComfyUI. | | | |
| CSSLab | Canada. University of Toronto lab behind Maia. | | | |
| DeepSeek | China. Publisher of the DeepSeek models (V4, V4.1 Flash). | | | |
| ggml-org | International. The llama.cpp team; publishes official GGUF files. | | | |
| Hugging Face | France and United States. Company behind the Hub and the Transformers library. | | | |
| infly | China. Publisher of Infinity-Parser (OCR). | | | |
| lmstudio-community | International. LM Studio's organisation for GGUF and MLX quantisations of official models. | | | |
| Meta (`facebook`) | United States. Publisher of SAM 2.1. | | | |
| Microsoft | United States. Publisher of VibeVoice and MoGe. | | | |
| Mistral AI | France. Publisher of LLMs. | | | |
| mlx-community | International. Open organisation where anyone can publish MLX conversions; quality and origin vary. | | | |
| NX-AI | Austria. Publisher of TiRex (time series). | | | |
| onnx-community | International. Community organisation for ONNX conversions. | | | |
| OpenAI | United States. Publisher of gpt-oss (open weights) and Whisper. | | | |
| OpenBMB | China. Publisher of VoxCPM (speech synthesis). | | | |
| OpenMOSS | China. Research team (Fudan University) behind MOSS-TTS. | | | |
| Organisation (HF) | The account that publishes a repository, e.g. `Qwen`. Official publishers are more trustworthy than individual re-uploaders. | organisation | Organisation | organizzazione |
| PaddlePaddle | China. Baidu's deep-learning framework team; publisher of PaddleOCR-VL. | | | |
| Qwen (Alibaba) | China. Publisher of the Qwen models (LLMs, vision, embeddings, rerankers, guard, image). | | | |
| SenseTime (`sensenova`) | China. Publisher of SenseNova-SI. | | | |
| Stanford CRFM | United States. Stanford centre behind the Anticipatory Music Transformer. | | | |
| Swiss AI (EPFL, ETH Zurich) | Switzerland. Publishers of Apertus, a Swiss LLM (gated). | | | |
| Tencent | China. Publisher of Hy-MT2 (translation). | | | |
| The Forecasting Company | France and United States (start-up). Publisher of t0 (time series). | | | |
| TII (`tiiuae`) | United Arab Emirates. Technology Innovation Institute, publisher of the Falcon models. | | | |
| Unsloth | United States. Publishes quantisations (GGUF "UD") and fine-tuning tools. | | | |
| Zyphra | United States. Publisher of ZONOS (speech synthesis). | | | |

## Licences and security

| Term | Explanation | French | German | Italian |
|---|---|---|---|---|
| AGPL-3.0 | Copyleft licence: changes must be shared, even for network use. | | | |
| Apache 2.0 | Permissive licence with a patent grant. | | | |
| BSD-2-Clause | Short permissive licence, similar to MIT. | | | |
| CC BY-NC | Creative Commons, non-commercial use only. | | | |
| CC BY-NC-SA | Creative Commons, non-commercial use, derivatives under the same licence. | | | |
| Commit (revision) | A fixed version of a repository, identified by a hash. Pinning it freezes the version. | commit, révision | Commit, Revision | commit, revisione |
| Gated repository | A repository that requires an account, a token and accepting conditions before download. | dépôt à accès restreint | zugangsbeschränktes Repository | repository ad accesso limitato |
| Hash (SHA-256) | A fingerprint of a file; any change gives a different hash. | empreinte | Prüfsumme, Hashwert | impronta, hash |
| MIT | Very short permissive licence. | | | |
| Pin | Fix a version so that it does not change. | épingler, figer | festlegen | fissare |
| Responsible use guidelines | Publisher's rules on intended use, referred to by a model card in addition to the licence (e.g. Ai2's). | règles d'usage responsable | Richtlinien zur verantwortungsvollen Nutzung | linee guida per l'uso responsabile |
| sudo | Runs a command as administrator; never give it to an agent. | | | |
| Supply chain attack | Malicious code hidden in a downloaded package or model. | attaque de la chaîne d'approvisionnement | Lieferkettenangriff | attacco alla catena di fornitura |
| Token (access) | A personal key to access a service. | jeton d'accès | Zugriffstoken | token di accesso |

## Hardware

| Term | Explanation | French | German | Italian |
|---|---|---|---|---|
| APFS | The file system of macOS. | | | |
| Apple Silicon | Apple's chips (M1 to M5, in base, Pro, Max and Ultra versions). | | | |
| Memory bandwidth | How fast memory is read; it drives the generation speed of LLMs. | bande passante mémoire | Speicherbandbreite | larghezza di banda della memoria |
| SSD | Fast flash storage; it sets how quickly models load. | | | |
| Throughput | Amount of data per unit of time, e.g. 1.3 GB/min. | débit | Durchsatz | velocità di trasferimento |
| Unified memory | Memory shared by CPU and GPU on Apple Silicon: it sets which models fit. | mémoire unifiée | gemeinsamer Arbeitsspeicher | memoria unificata |

## This glossary and its tool

| Term | Explanation | French | German | Italian |
|---|---|---|---|---|
| Dry run | A run that only shows what would happen. | essai à blanc | Probelauf | prova a vuoto |
| Model attic | Name of the model comparison tool that goes with this glossary. | grenier à modèles | Modell-Dachboden | soffitta dei modelli |
| Model record | One JSON file per model, with facts, sources and appraisals. | fiche de modèle | Modellsteckbrief | scheda del modello |
| Nice to have | Useful but not needed now. | souhaitable | wünschenswert | auspicabile |
| Provenance | Field of a model record for a third-party conversion: result of the checks that it holds the publisher's weights (who converted it, from which file, same parameter count or file hashes, reviewed conversion code). | provenance | Herkunft | provenienza |
