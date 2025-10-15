# Processed Data

Outputs from scripted pipelines and notebooks after segmentation, cleaning, and windowed analysis. Use this directory for QA-ready tables, metrics, and subject-level exports that precede the final deliverables.

## Subdirectory Schemas

- `ecg/{subject_id}/`: Contains `preprocessed_ecg.csv`, `hrv_metrics.xlsx`, and `rsa_metrics.xlsx`. See `data/processed/ecg/README.md` for full column definitions.
- `eda/{subject_id}/`: Contains `preprocessed_eda.csv` and `eda_features.xlsx` with the schema documented in `data/processed/eda/README.md`.

Files in this stage retain subject-specific granularity and feed the aggregation notebooks that populate `data/final`.
