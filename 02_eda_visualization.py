"""
Week 3: Exploratory data analysis and visualization for the order fulfillment dataset.

Reads data/orders_clean.csv (output of 01_data_audit_cleaning.py), computes
summary KPIs, and writes charts to outputs/charts/.
"""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "orders_clean.csv")
CHART_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs", "charts")
os.makedirs(CHART_DIR, exist_ok=True)

sns.set_style("whitegrid")


def save(fig_name):
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, fig_name), dpi=150)
    plt.close()


def main():
    df = pd.read_csv(DATA_PATH)

    print("Mean Delivery_Days:", round(df["Delivery_Days"].mean(), 2))
    print("Mean Shipping_Cost:", round(df["Shipping_Cost"].mean(), 2))
    print("Delayed rate (%):", round((df["Delivery_Status"] == "Delayed").mean() * 100, 2))
    print("Returned rate (%):", round((df["Delivery_Status"] == "Returned").mean() * 100, 2))

    plt.figure(figsize=(7, 4.5))
    sns.histplot(df["Delivery_Days"], bins=9, color="#2E5C8A")
    plt.title("Distribution of Delivery Days")
    save("delivery_days_distribution.png")

    plt.figure(figsize=(6, 4.5))
    status_counts = df["Delivery_Status"].value_counts()
    sns.barplot(x=status_counts.index, y=status_counts.values, hue=status_counts.index,
                palette="Blues_d", legend=False)
    plt.title("Order Count by Delivery Status")
    save("delivery_status_counts.png")

    plt.figure(figsize=(7, 4.5))
    sns.boxplot(data=df, x="Shipping_Mode", y="Shipping_Cost", hue="Shipping_Mode",
                palette="Set2", legend=False)
    plt.title("Shipping Cost by Shipping Mode")
    save("shipping_cost_by_mode.png")

    delay_by_region = df.groupby("Customer_Region")["Delivery_Status"] \
        .apply(lambda s: (s == "Delayed").mean() * 100).sort_values()
    plt.figure(figsize=(7, 4.5))
    sns.barplot(x=delay_by_region.values, y=delay_by_region.index, hue=delay_by_region.index,
                palette="Reds_d", legend=False)
    plt.title("Delayed-Order Rate (%) by Region")
    save("delay_rate_by_region.png")

    delay_by_mode = df.groupby("Shipping_Mode")["Delivery_Status"] \
        .apply(lambda s: (s == "Delayed").mean() * 100).sort_values()
    plt.figure(figsize=(7, 4.5))
    sns.barplot(x=delay_by_mode.values, y=delay_by_mode.index, hue=delay_by_mode.index,
                palette="Oranges_d", legend=False)
    plt.title("Delayed-Order Rate (%) by Shipping Mode")
    save("delay_rate_by_mode.png")

    num_cols = ["Shipping_Cost", "Delivery_Days", "Order_to_Ship_Days", "Order_to_Delivery_Days"]
    plt.figure(figsize=(6, 5))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)
    plt.title("Correlation Matrix")
    save("correlation_matrix.png")

    print(f"\nCharts written to {CHART_DIR}")


if __name__ == "__main__":
    main()
