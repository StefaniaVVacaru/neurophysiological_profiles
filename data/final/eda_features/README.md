# Final EDA Features

Holds the finalized electrodermal activity feature tables destined for reporting or modeling. Ensure documentation accompanies any schema changes.

## File Schema

`group_level_blc_eda_features.xlsx` contains subject-by-segment aggregates with baseline-corrected metrics:

| Column | Type | Description |
| --- | --- | --- |
| `index` | int | Preserved index from the aggregation notebook. |
| `segment_name` | string | Segment identifier (story label or baseline). |
| `subject_id` | string | Participant identifier. |
| `segment_length_seconds` | float | Duration of the segment in seconds. |
| `SCR_Peaks_N`, `SCR_Peaks_N_per_seconds` | float | Raw peak count and rate. |
| `SCR_Peaks_Amplitude_Mean` | float | Mean SCR amplitude for the segment (µS). |
| `EDA_Tonic_Mean`, `EDA_Tonic_SD` | float | Mean and standard deviation of tonic conductance. |
| `EDA_Sympathetic`, `EDA_SympatheticN`, `EDA_Autocorrelation` | float | NeuroKit-derived sympathetic indices. |
| `*_baseline` columns | float | Segment values computed during the baseline interval. |
| `*_blc` columns | float | Baseline-corrected metrics (story minus baseline). |

Refer to `Analysis notebooks/003_eda_analyis.ipynb` and `004_reformat_final_datasets.ipynb` for the transformation logic that produces this schema.
