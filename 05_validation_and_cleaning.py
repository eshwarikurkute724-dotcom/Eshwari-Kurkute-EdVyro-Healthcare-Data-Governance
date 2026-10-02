import pandas as pd
import numpy as np

raw = pd.read_csv("01_raw_synthetic_patient_records.csv")
df = raw.copy()

numeric = ["age_years","systolic_bp_mmHg","diastolic_bp_mmHg","heart_rate_bpm","hba1c_percent"]
for c in numeric:
    df[c] = pd.to_numeric(df[c], errors="coerce")

for c in ["sex","condition","smoker","state"]:
    df[c] = df[c].astype("string").str.strip()

df = df.drop_duplicates(keep="first")

df.loc[(df["age_years"] < 0) | (df["age_years"] > 120), "age_years"] = np.nan
df.loc[(df["systolic_bp_mmHg"] < 70) | (df["systolic_bp_mmHg"] > 250), "systolic_bp_mmHg"] = np.nan
df.loc[(df["diastolic_bp_mmHg"] < 40) | (df["diastolic_bp_mmHg"] > 150), "diastolic_bp_mmHg"] = np.nan
df.loc[(df["heart_rate_bpm"] < 30) | (df["heart_rate_bpm"] > 220), "heart_rate_bpm"] = np.nan
df.loc[(df["hba1c_percent"] < 3) | (df["hba1c_percent"] > 10), "hba1c_percent"] = np.nan

df.loc[~df["sex"].isin(["F","M"]), "sex"] = pd.NA
df.loc[~df["smoker"].isin(["Yes","No"]), "smoker"] = pd.NA
df.loc[~df["state"].isin(["Maharashtra","Gujarat","Karnataka","Goa"]), "state"] = pd.NA
df.loc[df["condition"].fillna("").eq(""), "condition"] = pd.NA

df.to_csv("02_cleaned_patient_records.csv", index=False)
print("Cleaning complete.")
print("Raw rows:", len(raw))
print("Duplicate rows removed:", raw.duplicated().sum())
print("Clean rows:", len(df))
