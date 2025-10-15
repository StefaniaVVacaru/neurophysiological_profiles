# Interim Data

Holds intermediate datasets produced during cleaning, alignment, or exploratory steps. Files here are mutable checkpoints created by notebooks prior to formal processing.

## Subdirectory Schemas

- `signals/`: CSV exports combining raw signals with event annotations (`time_seconds_original_file`, `MWMOBILEJ_*`, `event_name`, etc.).
- `events/`: Excel workbooks mirroring the signal CSV schema for quick inspection of segment boundaries.

These structures are fed directly into segmentation and feature-extraction scripts under `src/ecg_utils/`.
