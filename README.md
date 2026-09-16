# E-Commerce Order Fulfillment Analytics (Yuva Internship — Logistics Track)

Four-week data analysis project on a 50,000-record e-commerce order fulfillment dataset (Kaggle), covering strategic planning, data cleaning, exploratory analysis, and predictive modeling in Python.

## Project Structure

```
.
├── data/
│   └── README.md                  # where to place the dataset CSV
├── scripts/
│   ├── 01_data_audit_cleaning.py  # Week 2: quality audit + cleaning
│   ├── 02_eda_visualization.py    # Week 3: EDA + charts
│   └── 03_predictive_modeling.py  # Week 4: regression + classification
├── outputs/
│   └── charts/                    # generated PNG charts land here
├── docs/
│   └── findings_summary.md        # key findings across all 4 weeks
├── requirements.txt
└── README.md
```

## Dataset

`E-Commerce_Order_Fulfillment_Dataset_50K_Records.csv` — 50,000 orders with columns:

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Customer_Region | North / South / East / West / Central |
| Product_Category | Home, Grocery, Sports, Fashion, Beauty, Electronics |
| Order_Date | Date the order was placed |
| Ship_Date | Date the order left the warehouse |
| Delivery_Date | Date the order was delivered |
| Shipping_Mode | Standard / Express / Same Day |
| Shipping_Cost | Cost of shipping ($) |
| Delivery_Status | Delivered / Delayed / Returned |
| Delivery_Days | Ship-to-delivery transit time (days) — **not** total order-to-delivery time |

Place the CSV in `data/` before running the scripts (not committed to the repo due to size).

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scripts/01_data_audit_cleaning.py     # audits + writes data/orders_clean.csv
python scripts/02_eda_visualization.py       # writes charts to outputs/charts/
python scripts/03_predictive_modeling.py     # trains models, writes model charts
```

## Key Findings (see docs/findings_summary.md for details)

- The dataset is largely clean (no missing values, no duplicate order IDs), but `Delivery_Days` measures **ship-to-delivery** time only, not total fulfillment time — an important field-definition catch from Week 2.
- Delay rate (~15%) and return rate (~5%) are statistically flat across region, product category, and shipping mode.
- Premium shipping modes (Express, Same Day) cost 1.7x-3x more than Standard but show **no** measurable improvement in delay rate or transit time.
- Regression (R² ≈ 0) and classification (accuracy below the naive baseline) models confirm the available order attributes do not predict delivery outcomes — a genuine negative result pointing to missing operational fields (carrier ID, warehouse ID, route/distance) as the likely true drivers of delay.

## Weekly Reports

The four weekly Word-document reports (submitted separately per task requirements) are built from the exact code in this repo.
