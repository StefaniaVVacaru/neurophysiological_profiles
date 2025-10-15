# Final ECG Metrics

Contains vetted ECG-derived metrics (e.g., HRV aggregates) approved for dissemination. Files should align with the specifications documented in project reports.

## File Schema

`group_level_blc_ecg_metrics.xlsx` merges windowed HRV outputs with segment-level RSA summaries:

| Column | Type | Description |
| --- | --- | --- |
| `segment_name` | string | Segment identifier (baseline, story blocks, etc.). |
| `subject_id` | string | Participant identifier. |
| `HRV_*` columns | float | Time-domain HRV metrics propagated from processed outputs (MeanNN, SDNN, RMSSD, pNN20/50, etc.). |
| `heart_rate_bpm` | float | Mean heart rate for the segment. |
| `RSA_*` columns | float | RSA metrics (Porges-Bohrer, peak-to-trough variants, etc.). |
| `usable_analysis_windows_in_segment` | int | Count of analysis windows contributing to the aggregate. |
| `*_baseline` columns | float | Baseline values retained for comparison. |
| `*_corrected` columns | float | Baseline-corrected metrics used in group analyses. |

These columns map directly onto the exports from `data/processed/ecg/{subject_id}` produced by `compute_windowed_hrv_across_segments` and `calculate_rsa_per_segment`.
