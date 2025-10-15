# Raw Data

Unmodified exports from Mindware, including ECG, EDA, and event logs. Preserve the original file names and timestamps; downstream notebooks expect these inputs and only read from this location.

## Subdirectory Schemas

- `signals/`: Tab-delimited Mindware signal exports. Each file starts with `Sample Rate:` metadata followed by columns `Time (s)`, `MWMOBILEJ_Bio`, and optionally `MWMOBILEJ_GSC`. See the respective README files for details.
- `events/`: Event annotations with columns `Event Type`, `Name`, `Time` (seconds since start). Used to derive segment onsets/offsets.

Treat these files as read-only sources; all preprocessing steps copy schemas into `data/interim`.
