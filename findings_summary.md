# Key Findings Summary

## Week 1-2: Data Quality
- 50,000 orders, 10 columns, no missing values, no duplicate Order_IDs, all date sequences logically valid.
- `Delivery_Days` = Ship_Date to Delivery_Date only (confirmed by cross-check), **not** total Order_Date-to-Delivery_Date cycle time. Use `Order_to_Delivery_Days` for true end-to-end cycle time.
- `Shipping_Cost` has a naturally right-skewed distribution ($50-$399); the ~6% flagged as IQR outliers are valid high-cost (mostly Same Day) orders, not errors.

## Week 3: EDA
- Baseline: mean transit time 5.99 days, mean shipping cost $138.84, 15.01% delayed, 4.87% returned.
- Delay rate is flat across region (14.55%-15.41%) and shipping mode (14.87%-15.40%).
- Same Day shipping costs ~3x Standard ($299.59 vs $99.29); Express ~1.7x ($164.58).
- No numeric field correlates meaningfully with Delivery_Days or delay outcome.

## Week 4: Modeling
- Regression (Linear + Random Forest) predicting Delivery_Days: R² ≈ 0 for both models.
- Classification predicting Delayed status: 60.2% accuracy, worse than the 85.0% naive baseline (always predict "not delayed").
- Conclusion: Customer_Region, Product_Category, Shipping_Mode, and Shipping_Cost carry no predictive signal for delivery outcomes in this dataset.

## Recommendation
1. Re-evaluate premium shipping tier spend — Express/Same Day show no measurable service benefit over Standard.
2. Capture additional operational fields (carrier ID, warehouse ID, route/distance) to enable a genuinely predictive delay-risk model in a future iteration.
