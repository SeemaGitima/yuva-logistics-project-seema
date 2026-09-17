# Data

Place `E-Commerce_Order_Fulfillment_Dataset_50K_Records.csv` in this folder before running the scripts.

The dataset is not committed to this repository (keep large data files out of version control — use `.gitignore` or Git LFS if you need to track it).

Running `scripts/01_data_audit_cleaning.py` will read the raw CSV from here and write `orders_clean.csv` back into this folder.
