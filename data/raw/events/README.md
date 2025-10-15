# Raw Event Logs

Mindware-exported event tables (typically `.txt`) reside here. Each file records stimulus onsets/offsets used by the segmentation utilities to define analysis windows.

## File Schema

Event exports are tab-delimited text with a single header row:

| Column | Type | Description |
| --- | --- | --- |
| `Event Type` | string | Mindware event category (e.g., `Physical Event trigger (e.g., button press, acquisition)`ß). |
| `Name` | string | Label applied during acquisition (baseline, story ID). |
| `Time` | float | Timestamp of the event in seconds relative to recording start. |

Rows appear in chronological order and are consumed directly by the segmentation helpers under `src/ecg_utils/data_utils.py`.
