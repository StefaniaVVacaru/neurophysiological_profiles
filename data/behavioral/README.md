# Behavioral Data

Behavioral assessments or questionnaire outputs synced with physiological segments. Use this space for files that augment ECG/EDA metrics with behavioral context.

## File Schema

The workbook `filtered_data_v3 (with ASAs).xlsx` contains participant-level questionnaire and demographic information. Column definitions:

| Column | Type |
| --- | --- |
| `ParticipantID` | string |
| `Gender` | string |
| `DOB` | date |
| `Ethnicity`, `Ethnicity_Other` | string |
| `EduLvl`, `EduLvl_Other` | string |
| `LTDatingPrtn`, `LTDatingPrtn_Other` | string |
| `MothEduLvl`, `FatherEduLvl` | string |
| `MedicCond`, `MedicCond_Other` | string |
| `HeartCond`, `HeartCond_Other` | string |
| `Smoking`, `Smoking_Freq`, `Alcohol`, `Alcohol_Freq`, `Caffeine`, `Exercise` | string |
| `Height`, `Weight`, `BMI` | float |
| `ECR_*` columns | float |
| `ECR*RS` columns | float |
| `ECRAvoidanceScore_*`, `ECRAnxietyScore_*` | float |
| `EUQ_*` columns | float |
| `EarlyLifeUnpredictability` | float |
| `ASAOrder`, `ASA_tot` | float |
| `STORY{1-5}NAME`, `Story{2-5}_Score` | string/float |

Any downstream merges that combine behavioral metrics with physiology should retain these column names to preserve reproducibility.
