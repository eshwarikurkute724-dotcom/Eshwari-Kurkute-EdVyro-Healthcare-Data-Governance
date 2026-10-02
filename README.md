# Healthcare Data Governance and Cleaning

### EdVyro Data Analytics — Healthcare/Pharmacy Internship
*Candidate:* Eshwari Kurkute

## Project Overview

This project demonstrates privacy-aware healthcare data governance and cleaning using a synthetic, de-identified patient dataset.

## Objectives

- Classify healthcare data fields.
- Validate data types and ranges.
- Identify missing values.
- Detect duplicate records.
- Identify invalid categorical values.
- Apply reproducible cleaning rules.
- Document data-quality exceptions.

## Privacy and De-identification

The dataset is synthetic and does not represent real patients.

It contains no patient names, phone numbers, emails, residential addresses, Aadhaar numbers, or medical record numbers.

The patient_id field is used as a pseudonymous record key within the synthetic dataset.

## Validation Rules

- Patient ID must be unique.
- Age must be between 0 and 120 years.
- Blood pressure and heart rate must fall within defined validation ranges.
- HbA1c must be numeric and within the exercise validation range.
- Smoking status must be Yes or No.
- State must belong to the defined category list.

## Cleaning Approach

1. Converted numeric text values into numeric format.
2. Removed exact duplicate records.
3. Identified invalid age values.
4. Identified out-of-range clinical values.
5. Identified invalid categorical values.
6. Converted invalid values to missing where appropriate.
7. Documented exceptions instead of inventing clinical values.

## Files

```text
data/
├── 01_raw_synthetic_patient_records.csv
└── 02_cleaned_patient_records.csv

documentation/
├── 03_quality_exception_log.csv
└── 04_data_dictionary.csv

validation/
└── 05_validation_and_cleaning.py

EdVyro_Task1_Healthcare_Data_Governance.xlsx
