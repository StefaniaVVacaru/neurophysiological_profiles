# Data Directory

Central hub for all project datasets. Subdirectories reflect the data lifecycle: raw Mindware exports, interim cleaned assets, processed analysis outputs, final deliverables, and behavioral measures aligned to physiological segments. Treat raw files as read-only and promote derivatives through the structure as they are generated.

## Directory Overview

| Folder | Purpose | Key Schemas |
| --- | --- | --- |
| `raw/` | Mindware source exports (`signals/`, `events/`, and batch add-ons). | `.txt` signals with `Time (s)` + `MWMOBILEJ_*` channels; event logs with `Event Type`, `Name`, `Time`. |
| `interim/` | Joined signal/event tables ready for segmentation. | CSV/Excel with `time_seconds_original_file`, `MWMOBILEJ_*`, `event_name`, `on_offset`, `subject_id`. |
| `processed/` | Subject-level cleaned ECG/EDA outputs. | `preprocessed_*` timeseries, `hrv_metrics.xlsx`, `rsa_metrics.xlsx`, `eda_features.xlsx`. |
| `final/` | Wide dataset ready for further (statistical) analysis | Aggregated ECG (`HRV_*`, `RSA_*`), EDA (`EDA_*`, `SCR_*`), and combined neuro-behavioral workbooks. |
| `behavioral/` | Questionnaire and demographic context. | Participant-level Excel with attachment, EUQ, ASA, and story metadata fields. |

Refer to each subdirectory README for detailed column definitions and any future schema updates.
