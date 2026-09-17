# E-Commerce Order Fulfillment Analytics (Yuva Internship — Logistics Track)

A four-week data analytics project focused on analyzing e-commerce order fulfillment and delivery performance using Python and data analysis techniques.

The project uses a dataset containing 50,000 e-commerce orders and covers data understanding, validation, cleaning, exploratory data analysis, KPI analysis, and predictive modeling as part of the overall project roadmap.

---

## 📌Project Objective

The main objective of this project is to analyze e-commerce order fulfillment data and identify important patterns related to:

- Order delivery performance
- Delayed and returned orders
- Shipping costs
- Delivery success rate
- Shipping modes
- Customer regions
- Product categories
- Operational efficiency

The analysis is intended to support better understanding of logistics performance and help identify areas for improvement.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab
- GitHub

---

# 🗂️ Project Structure

```text
E-Commerce-Order-Fulfillment-Analytics/
│
├── data/
│   └── README.md
│       # Instructions for placing the dataset CSV
│
├── notebooks/
│   └── E-Commerce_Order_Fulfillment_Analysis.ipynb
│       # Complete analysis notebook
│
├── scripts/
│   ├── 01_data_audit_cleaning.py
│   │   # Week 2: Data quality audit and cleaning
│   │
│   ├── 02_eda_visualization.py
│   │   # Week 3: Exploratory data analysis and visualizations
│   │
│   ├── 03_kpi_analysis.py
│   │   # Week 4: KPI and operational performance analysis
│   │
│   └── 04_predictive_modeling.py
│       # Predictive modeling
│
├── outputs/
│   └── charts/
│       # Generated PNG charts and visualizations
│
├── docs/
│   └── findings_summary.md
│       # Key findings and insights across the project
│
├── requirements.txt
│   # Required Python libraries
│
└── README.md
    # Project documentation
```

## Key Findings (see docs/findings_summary.md for details)

- The dataset is largely clean (no missing values, no duplicate order IDs), but `Delivery_Days` measures **ship-to-delivery** time only, not total fulfillment time — an important field-definition catch from Week 2.
- Delay rate (~15%) and return rate (~5%) are statistically flat across region, product category, and shipping mode.
- Premium shipping modes (Express, Same Day) cost 1.7x-3x more than Standard but show **no** measurable improvement in delay rate or transit time.
- Regression (R² ≈ 0) and classification (accuracy below the naive baseline) models confirm the available order attributes do not predict delivery outcomes — a genuine negative result pointing to missing operational fields (carrier ID, warehouse ID, route/distance) as the likely true drivers of delay.

# 🗓️ Four-Week Project Roadmap

## Week 1 — Strategic Planning & Data Exploration

The first week focused on understanding the logistics problem, defining objectives, exploring the dataset, and identifying important business questions.

### Activities

* Business problem identification
* Dataset understanding
* Initial data exploration
* KPI identification
* Data validation
* Logistics background research
* Analytical roadmap preparation

---

## Week 2 — Data Quality Audit & Cleaning

The second week focused on preparing the dataset for reliable analysis.

### Activities

* Dataset structure validation
* Missing-value analysis
* Duplicate-value checking
* Data type verification
* Date-column validation
* Categorical-value inspection
* Data cleaning
* Preparation of analysis-ready data

**Script:**

```text
scripts/01_data_audit_cleaning.py
```

---

## Week 3 — Exploratory Data Analysis & Visualization

The third week focuses on exploring patterns and relationships within the fulfillment data.

### Analysis Areas

* Delivery performance
* Delivery days
* Shipping costs
* Delivery status
* Shipping modes
* Customer regions
* Product categories
* Delayed orders
* Returned orders
* Operational trends

### Visualizations

Charts are generated and stored in:

```text
outputs/charts/
```

**Script:**

```text
scripts/02_eda_visualization.py
```

---

## Week 4 — KPI Analysis & Predictive Modeling

The final stage focuses on measuring operational performance through KPIs and applying predictive analytics.

### KPI Analysis

Important metrics include:

* Average Delivery Days
* Delayed Orders
* Delay Rate
* Average Shipping Cost
* Delivered Orders
* Delivery Success Rate
* Return Rate

**Script:**

```text
scripts/03_kpi_analysis.py
```

### Predictive Modeling

The project also includes predictive modeling to explore whether order-level information can be used to predict relevant fulfillment outcomes.

**Script:**

```text
scripts/04_predictive_modeling.py
```

The modeling workflow may include:

* Feature preparation
* Train-test split
* Model training
* Model evaluation
* Performance comparison
* Interpretation of results

---

# 📈 Key Findings

The initial analysis identified the following operational metrics from the dataset:

| KPI                   |    Result |
| --------------------- | --------: |
| Total Orders          |    50,000 |
| Average Delivery Days | 5.99 days |
| Delayed Orders        |     7,505 |
| Delay Rate            |    15.01% |
| Average Shipping Cost |    138.84 |
| Delivered Orders      |    40,062 |
| Delivery Success Rate |    80.12% |
| Returned Orders       |     2,433 |

### Delivery Status Distribution

```text
Delivered    → 40,062
Delayed      → 7,505
Returned     → 2,433
```

These metrics provide a baseline view of fulfillment performance and can be further analyzed across shipping modes, regions, product categories, and other operational factors.

---

# 🛠️ Technologies & Tools

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Development Environment

* Google Colab
* Jupyter Notebook

### Version Control

* Git
* GitHub

---

# 🔄 Analytics Workflow

```text
Business Problem
       ↓
Dataset Collection
       ↓
Data Understanding
       ↓
Data Quality Audit
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Visualization
       ↓
KPI Analysis
       ↓
Predictive Modeling
       ↓
Model Evaluation
       ↓
Business Insights
       ↓
Final Findings
```

---

# 📁 Outputs

The project generates analytical outputs such as:

* Data quality results
* KPI summaries
* Exploratory analysis results
* Visualization charts
* Predictive model results
* Key findings and insights

Charts are stored in:

```text
outputs/charts/
```

Project findings are documented in:

```text
docs/findings_summary.md
```

---

# 💡 Business Questions

The analysis is designed to answer questions such as:

1. What is the average delivery time?
2. What percentage of orders are delayed?
3. Which shipping modes have different delivery-cost patterns?
4. What proportion of orders are returned?
5. How does delivery performance vary across regions?
6. Which product categories show different fulfillment patterns?
7. What factors are associated with delivery delays?
8. Can fulfillment outcomes be predicted using available order information?

---

# 🚀 Future Scope

The project can be extended with:

* Advanced feature engineering
* Additional machine learning models
* Hyperparameter tuning
* Model explainability
* Interactive dashboards using Power BI or Tableau
* Streamlit deployment
* Automated KPI reporting
* Advanced logistics optimization analysis

---

# 📌 Project Status

**Project Type:** Data Analytics & Predictive Modeling
**Domain:** E-Commerce & Logistics
**Duration:** 4 Weeks
**Dataset Size:** 50,000 Records
**Primary Language:** Python

---

## 👩‍💻 Author

**Seema Das**

M.Tech — Computer Science Engineering
Aspiring Data Scientist

### GitHub

[GitHub Profile](https://github.com/SeemaGitima)

---

## ⭐ Project Highlights

This project demonstrates an end-to-end analytics workflow covering:

**Data Understanding → Data Cleaning → EDA → Visualization → KPI Analysis → Predictive Modeling → Business Insights**

The project is developed as part of the **Yuva Internship — Logistics Analytics Track**.


## Weekly Reports

The four weekly Word-document reports (submitted separately per task requirements) are built from the exact code in this repo.
