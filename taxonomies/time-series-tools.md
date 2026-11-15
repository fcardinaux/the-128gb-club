# Taxonomy of local AI time-series tools

Research of 15 November 2026, metadata and user feedback only. Companion of the other files in this folder.
"Covered by documented models?" tells whether the task is already covered by models with a record in [`../model-comparison.md`](../model-comparison.md#time-series-forecasting): Chronos-2, Granite PatchTST-FM r2, Moirai, t0-gamma, TimesFM 2.5 and 3.0, Timestral, TiRex-2 and Toto 2.0.
"Licence and format pitfalls" assume a strict policy: Apache 2.0 or MIT licences, safetensors or GGUF weights, no gated repository.
**Reddit could not be read**. Licences, gating, sizes and commits come from the Hugging Face API, read on 15.11.2026; commits are the first 12 characters.

## Reference resources

| Resource | Last update | What it covers | Strengths | Weaknesses |
|---|---|---|---|---|
| [GIFT-Eval](https://huggingface.co/spaces/Salesforce/GIFT-Eval) | 13.11.2026 | 97 configurations; MASE and CRPS relative to seasonal naive | Broad; the de facto ranking of forecasting foundation models | Pretraining overlap and leakage concerns; self-submitted |
| [fev-bench](https://huggingface.co/spaces/autogluon/fev-bench) | 13.11.2026 | 100 tasks including covariates | Covers covariates and multivariate tasks | Same leakage risk |
| [TS-Arena](https://ts-arena.live/) ([paper](https://arxiv.org/abs/2512.20761)) | live; contents not checked | Forecasts registered before the truth exists | Leakage-free by design | Energy data only; few rounds |

## Taxonomy

| # | Category → sub-tasks | Typical uses | Covered by documented models? | Licence and format pitfalls |
|---|---|---|---|---|
| 1 | **Zero-shot probabilistic forecasting** | Demand, energy, monitoring | **Yes** (8 records) | Moirai: CC BY-NC; TiRex v1: community licence and `.ckpt`; Timestral: modified MIT |
| 2 | **Covariates and multivariate forecasting** | Prices, promotions, weather drivers | **Yes** (Chronos-2, TimesFM, TiRex-2) | Simons: OpenMDW 1.1 |
| 3 | **Anomaly detection** | Operations monitoring | No | – |
| 4 | **Classification, imputation, embeddings** | Sensors, health data | No | MOMENT repositories hold a duplicate `.bin` |
| 5 | **Domain-specific models** (financial candlesticks) | Market data | No | – |
| 6 | **Ensembles** | A robust default | No | The IBM ensemble pulls in PatchTST-FM r2 |
| 7 | **Classical baselines** → seasonal naive, AutoARIMA, ETS, Theta (statsforecast), Prophet, gradient boosting | Always benchmark these first | – | Licences of statsforecast and Prophet not checked |

**Cross-cutting note**: HN comments repeatedly say to compare a foundation model against seasonal naive and gradient boosting before trusting it (see below).

## Hacker News comments used

Algolia API, comments only. Window: since 13.05.2026.

- Timestral tops the metabonet dataset but did not beat XGBoost or a custom transformer on one user's glucose data ([0xdeadf1sh, 15.11.2026](https://news.ycombinator.com/item?id=50505072)).
- For e-commerce projections, seasonal naive usually wins ([jc4p, 19.10.2026](https://news.ycombinator.com/item?id=50155295)); foundation models make sense for thousands of short series ([logancbrown, 19.10.2026](https://news.ycombinator.com/item?id=50152506)).
- In slow domains such as power prices, out-of-sample performance is hard to verify because of possible pretraining leakage ([sambucini, 20.10.2026](https://news.ycombinator.com/item?id=50163023)); scepticism about real-world usefulness ([beernet, 19.10.2026](https://news.ycombinator.com/item?id=50151235)).
- A study comparing foundation models with ECMWF for operational weather decisions ([natemurthy, 25.10.2026](https://news.ycombinator.com/item?id=50234270)).
- Searches with no usable result: Timer-S1, Sundial, Kairos, MOMENT, TSPulse, statsforecast.

## Candidates by category

"Main option" = the best candidate under the strict policy; "Alternative" = also usable; "Flag" = usable only after a check. No HN or Hugging Face feedback was found for any model below: **feedback is thin**.

### 1–2. Forecasting

| Repo | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| `thuml/Timer-S1` (8.3B MoE, 0.75B active) | Apache 2.0 | 16.61 GB | `dd92ce51c691` | Transformers on CPU or MPS (MPS not checked) | Alternative: zero-shot quantiles (09.05.2026) |
| `thuml/sundial-base-128m` | Apache 2.0 | 0.51 GB | `3212e4256449` | Transformers | Alternative: zero-shot, generative |
| `mldi-lab/Kairos_50m` | Apache 2.0 | 0.20 GB | `b788434dd95f` | PyTorch | Alternative: small |
| `ibm-granite/granite-timeseries-ttm-r3` | Apache 2.0 | 0.01 GB | `ea17cfd2e3ed` | granite-tsfm, CPU | Alternative: tiny, fine-tunable; covariate support not checked |
| `Maple728/TimeMoE-200M` | Apache 2.0 | 0.91 GB | – | Transformers | Alternative |
| `ibm-granite/granite-timeseries-ensemble-r1` | Apache 2.0 | framework, no weights | `90a45c945c73` | granite-tsfm | **Flag**: the default ensemble includes PatchTST-FM r2; with PatchTST-FM r1, FlowState r1.1 and TTM-r3 only, every part is Apache 2.0 |

The documented Apache models (Chronos-2, t0-gamma, TiRex-2, Toto 2.0, TimesFM 2.5) remain the better-tested options.

- Excluded: Moirai MoE and Moirai 2.0 (CC BY-NC 4.0; documented), timeh2o v1 and tiny (non-commercial, gated), Simons-297M (OpenMDW 1.1), TiRex v1 (community licence, `.ckpt`/ONNX), yug (CC BY-NC), ci-proto (custom licence, `.ckpt`), TabPFN v2 and TabPFN-TS (Prior Labs licence, `.ckpt`).
- Flagged: Lag-Llama (Apache 2.0; a `.ckpt` checkpoint next to a small safetensors file, which one the library loads was not checked).

### 3–4. Anomaly detection, classification, imputation

| Repo | Licence | Size | Commit | Runtime | Verdict |
|---|---|---|---|---|---|
| `ibm-granite/granite-timeseries-tspulse-r1` | Apache 2.0 | small (weights partly in branches, not checked) | `2e64fcdc2a06` | granite-tsfm | Alternative |
| `AutonLab/MOMENT-1-large` (also small) | MIT | 1.39 GB | `ca58581bc7be` | momentfm on PyTorch | Alternative: take only the safetensors file |

### 5. Domain-specific

| Repo | Licence | Size | Commit | Verdict |
|---|---|---|---|---|
| `NeoQuasar/Kronos-base` | MIT | 0.41 GB | `2b554741eca4` | Niche: financial candlestick data |
