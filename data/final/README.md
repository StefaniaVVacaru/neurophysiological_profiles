# Final Data

Curated deliverables ready for sharing with collaborators or for statistical modeling. Only publish vetted, analysis-ready datasets here.

## Available Datasets

- `ecg_metrics/group_level_blc_ecg_metrics.xlsx`:  ECG HRV and RSA features of all participants with baseline and baseline-corrected features (see `data/final/ecg_metrics/README.md` for the full schema).
- `eda_features/group_level_blc_eda_features.xlsx`: EDA-derived feautures of all participants including raw, baseline, and baseline-corrected features (`data/final/eda_features/README.md` documents columns).
- `neuro-behavioral_data.xlsx`: Integrated dataset combining behavioral data with key ECG/EDA features from the datasets above.

### `neuro-behavioral_data.xlsx` Schema

| Column | Type |
| --- | --- |
| `ParticipantID` | string |
| Demographics & lifestyle (`Gender`, `DOB`, `Ethnicity`, `Height`, `Weight`, `BMI`, etc.) | mixed |
| Attachment scales (`ECR_*`, `ECR*RS`, `ECRAvoidanceScore_*`, `ECRAnxietyScore_*`) | float |
| Early unpredictability (`EUQ_*`, `EarlyLifeUnpredictability`) | float |
| Story metadata (`ASAOrder`, `STORY{1-5}NAME`, `Story{2-5}_Score`, `ASA_tot`) | mixed |
| Physiological metrics (`HRV_*`, `RSA_*`, `heart_rate_bpm_*`, `EDA_Tonic_*`, `SCR_Peaks_*`) | float |
| `story_score_*` columns | float |

All final tables are column-aligned with the aggregation notebooks in `Analysis notebooks/004_reformat_final_datasets.ipynb`.
