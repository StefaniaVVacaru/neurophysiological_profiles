# Raw Physiological Signals

Contains Mindware signal exports (e.g., ECG, EDA) exactly as delivered. Do not overwrite files; create cleaned derivatives under `data/interim` or `data/processed` instead.

## File Schema

Mindware `.txt` signal exports include an inline metadata row followed by tab-delimited samples:

- Line 1: `Sample Rate:\t{float}` (Hz).
- Line 2 onward: physiological samples with the following columns.

| Column | Type | Description |
| --- | --- | --- |
| `Time (s)` | float | Elapsed recording time in seconds from acquisition start. |
| `MWMOBILEJ_Bio` | float | Raw biosignal channel exported by Mindware (typically ECG voltage). |
| `MWMOBILEJ_GSC` *(optional)* | float | Galvanic skin conductance channel when recorded alongside ECG. |

Files always include `Time (s)` and `MWMOBILEJ_Bio`; `MWMOBILEJ_GSC` appears when the session captured GSR/EDA.
