# Processed EDA

Electrodermal activity outputs following preprocessing, artifact handling, and segmentation. Store QA-friendly tables and figures that support downstream reporting.

## File Schemas

Each subject subfolder contains the following exports:

### `preprocessed_eda.csv`

| Column | Type | Description |
| --- | --- | --- |
| `time_seconds_original_file` | float | Original recording timestamp for each sample. |
| `source_file_signal` | string | Mindware signal filename used as input. |
| `Event Type` | string | Event category at the sample (blank between events). |
| `event_name` | string | Assigned segment label. |
| `source_file_event` | string | Source event log filename. |
| `on_offset` | string | Event boundary flag (`onset`/`offset`). |
| `subject_id` | string | Participant identifier. |
| `EDA_Raw` | float | Unprocessed skin conductance signal (µS). |
| `EDA_Clean` | float | Cleaned signal returned by `nk.eda_process`. |
| `EDA_Tonic` | float | Slow-varying tonic component. |
| `EDA_Phasic` | float | Phasic component isolated by NeuroKit. |
| `SCR_Onsets` | int | Binary indicator of detected SCR onsets. |
| `SCR_Peaks` | int | Binary indicator of SCR peaks retained after artifact filtering. |
| `SCR_Height` | float | Peak height per sample. |
| `SCR_Amplitude` | float | Skin conductance response amplitude (µS). |
| `SCR_RiseTime` | float | Response rise time in seconds. |
| `SCR_Recovery` | float | Recovery value per sample. |
| `SCR_RecoveryTime` | float | Recovery duration in seconds. |

### `eda_features.xlsx`

Segment-level feature summary used for group analyses.

| Column | Type | Description |
| --- | --- | --- |
| `SCR_Peaks_N` | int | Count of SCR peaks within the segment. |
| `SCR_Peaks_Amplitude_Mean` | float | Mean SCR amplitude (µS). |
| `EDA_Tonic_SD` | float | Standard deviation of tonic component. |
| `EDA_Sympathetic` / `EDA_SympatheticN` | float | Sympathetic activation indices from NeuroKit. |
| `EDA_Autocorrelation` | float | Autocorrelation of the cleaned signal. |
| `segment_name` | string | Segment identifier. |
| `subject_id` | string | Participant identifier. |
| `segment_length_seconds` | float | Segment duration derived from sample count. |
| `SCR_Peaks_N_per_seconds` | float | Peak frequency (count per second). |
| `EDA_Tonic_Mean` | float | Mean tonic conductance (µS). |
