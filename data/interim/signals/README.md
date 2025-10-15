# Interim Signals

Stores partially cleaned or resampled physiological signals generated during exploratory processing. These assets feed into QA checks before full windowed analyses occur.

## File Schema

Files are CSV exports named `{subject_id}_signal_events.csv`. They combine raw signal samples with aligned event metadata:

| Column | Type | Description |
| --- | --- | --- |
| `time_seconds_original_file` | float | Original Mindware timestamp in seconds. |
| `MWMOBILEJ_Bio` | float | Raw biosignal channel copied from the Mindware export. |
| `MWMOBILEJ_GSC` | float | Raw galvanic skin conductance channel when available. |
| `source_file_signal` | string | Source filename for the Mindware signal export. |
| `Event Type` | string | Event category joined from the event log. |
| `event_name` | string | Human-readable event label (baseline, story blocks, etc.). |
| `source_file_event` | string | Source filename for the Mindware event export. |
| `on_offset` | string | Derived event marker (`onset` or `offset`). |
| `subject_id` | string | Participant identifier assigned during preprocessing. |

The CSV retains the row order of the original file. Downstream segmentation utilities expect all columns to be present even if some rows contain nulls for the event metadata.
