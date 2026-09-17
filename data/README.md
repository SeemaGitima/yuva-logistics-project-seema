# Dataset Documentation

## Dataset Name

**E-Commerce Order Fulfillment Dataset — 50K Records**

This folder contains the dataset used for the **E-Commerce Order Fulfillment Analytics** project.

The dataset is used to analyze order fulfillment, delivery performance, shipping costs, delivery status, and operational patterns.

---

## Dataset File

Place the following CSV file in this folder:

```text
E-Commerce_Order_Fulfillment_Dataset_50K_Records.csv
```

The expected file path is:

```text
data/E-Commerce_Order_Fulfillment_Dataset_50K_Records.csv
```

---

## Dataset Overview

| Attribute      | Details                                  |
| -------------- | ---------------------------------------- |
| Records        | 50,000                                   |
| Format         | CSV                                      |
| Domain         | E-Commerce / Logistics                   |
| Purpose        | Order fulfillment and delivery analytics |
| Analysis Tool  | Python                                   |
| Main Libraries | Pandas, NumPy, Matplotlib, Seaborn       |

The dataset contains order-level information related to customers, products, shipping, delivery, costs, and delivery outcomes.

---

## Key Columns

The dataset includes the following important fields:

* **Order_ID** — Unique identifier for each order
* **Customer_Region** — Region associated with the customer/order
* **Product_Category** — Category of the ordered product
* **Order_Date** — Date when the order was placed
* **Ship_Date** — Date when the order was shipped
* **Delivery_Date** — Date when the order was delivered or completed
* **Shipping_Mode** — Shipping method such as Standard, Express, or Same Day
* **Shipping_Cost** — Cost associated with shipping
* **Delivery_Status** — Delivery outcome such as Delivered, Delayed, or Returned
* **Delivery_Days** — Number of days taken for delivery

---

## Dataset Usage

The dataset is used throughout the project for:

1. Data quality validation
2. Missing-value and duplicate checks
3. Exploratory Data Analysis (EDA)
4. Delivery performance analysis
5. Shipping cost analysis
6. Delivery-status analysis
7. Regional analysis
8. Shipping-mode analysis
9. KPI calculation
10. Business insights and recommendations

---

## Data Processing

The raw dataset is used as the input for the data-cleaning workflow.

The script:

```text
scripts/01_data_audit_cleaning.py
```

reads the raw CSV from this folder and generates the cleaned dataset:

```text
data/orders_clean.csv
```

The cleaned dataset is then used by subsequent analysis scripts.

---

## Data Source

The dataset was provided for the **Yuva Internship — Logistics Track** project and is used for educational and analytical purposes.

If the original dataset source or download link is available, it can be added here for reference.

---

## Version Control

The raw dataset is **not committed to this repository**.

Large data files are intentionally kept outside Git version control to keep the repository lightweight and easier to manage.

If dataset versioning is required in the future, **Git LFS (Large File Storage)** or an external dataset repository can be used.

---

## Privacy & Data Handling

This project is intended for educational and portfolio purposes.

The dataset should not contain personally identifiable or confidential customer information. If sensitive information is introduced in future versions, it should be removed or anonymized before being shared publicly.

---

## Folder Structure

```text
data/
├── README.md
├── E-Commerce_Order_Fulfillment_Dataset_50K_Records.csv
└── orders_clean.csv
```

> Note: The CSV files may not appear in the public GitHub repository if they are excluded through `.gitignore`.

---

## Related Project Files

The analysis workflow is organized as follows:

```text
scripts/
├── 01_data_audit_cleaning.py
├── 02_eda_visualization.py
└── 03_predictive_modeling.py
```

The main exploratory analysis notebook is available under:

```text
notebooks/
└── E-Commerce_Order_Fulfillment_Analysis.ipynb
```

