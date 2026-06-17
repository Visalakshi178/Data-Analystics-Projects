"""
Ecommerce Demand Planning Analytics
Tools: Python, SQL, ETL, Pandas, NumPy
Author: Visalakshi Polepalli
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings("ignore")

# ── 1. Generate Sample Data ───────────────────────────────────────────────────
np.random.seed(42)

dates = pd.date_range(start="2022-01-01", end="2024-12-31", freq="D")
products = ["Electronics", "Clothing", "Home & Garden", "Sports", "Books"]
regions = ["North", "South", "East", "West"]

rows = []
for date in dates:
    for product in products:
        base_demand = {"Electronics": 120, "Clothing": 200, "Home & Garden": 80,
                       "Sports": 150, "Books": 60}[product]
        seasonality = 1 + 0.3 * np.sin(2 * np.pi * date.month / 12)
        noise = np.random.normal(1, 0.1)
        demand = max(0, int(base_demand * seasonality * noise))
        revenue = round(demand * np.random.uniform(15, 200), 2)
        rows.append({
            "date": date,
            "product_category": product,
            "region": np.random.choice(regions),
            "units_sold": demand,
            "revenue": revenue,
            "inventory_level": np.random.randint(50, 500),
            "price": round(revenue / demand if demand > 0 else 0, 2),
            "returns": int(demand * np.random.uniform(0, 0.05)),
        })

df = pd.DataFrame(rows)
print("=" * 60)
print("ECOMMERCE DEMAND PLANNING ANALYTICS")
print("=" * 60)
print(f"\nDataset Shape: {df.shape}")
print(f"Date Range: {df['date'].min()} to {df['date'].max()}")
print("\nFirst 5 rows:")
print(df.head())

# ── 2. ETL Pipeline ──────────────────────────────────────────────────────────
print("\n--- ETL: Cleaning & Transforming ---")

# Extract
raw_df = df.copy()

# Transform
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["quarter"] = df["date"].dt.quarter
df["day_of_week"] = df["date"].dt.day_name()
df["net_units"] = df["units_sold"] - df["returns"]
df["net_revenue"] = (df["revenue"] * (1 - df["returns"] / df["units_sold"].replace(0, 1))).round(2)

# Load — aggregate to monthly
monthly_df = df.groupby(["year", "month", "product_category"]).agg(
    total_units=("net_units", "sum"),
    total_revenue=("net_revenue", "sum"),
    avg_inventory=("inventory_level", "mean"),
    avg_price=("price", "mean")
).reset_index()

print(f"Raw records: {len(raw_df)}")
print(f"Monthly aggregated records: {len(monthly_df)}")
print("\nMissing values after transform:", df.isnull().sum().sum())

# ── 3. Demand Forecasting ────────────────────────────────────────────────────
print("\n--- Demand Forecasting ---")

# Simple moving average forecast per product
forecasts = []
for product in products:
    prod_df = monthly_df[monthly_df["product_category"] == product].copy()
    prod_df = prod_df.sort_values(["year", "month"])
    prod_df["ma_3"] = prod_df["total_units"].rolling(3).mean()
    prod_df["ma_6"] = prod_df["total_units"].rolling(6).mean()
    prod_df["forecast"] = prod_df["ma_3"].fillna(prod_df["total_units"])
    prod_df["forecast_error"] = abs(prod_df["total_units"] - prod_df["forecast"])
    prod_df["accuracy"] = (1 - prod_df["forecast_error"] / prod_df["total_units"].replace(0, 1)) * 100
    forecasts.append(prod_df)

forecast_df = pd.concat(forecasts)
avg_accuracy = forecast_df["accuracy"].mean()
print(f"Average Forecast Accuracy: {avg_accuracy:.1f}%")

# ── 4. Key Metrics ───────────────────────────────────────────────────────────
print("\n--- Key Business Metrics ---")
print(f"Total Revenue: ${df['net_revenue'].sum():,.2f}")
print(f"Total Units Sold: {df['net_units'].sum():,}")
print(f"Avg Daily Revenue: ${df['net_revenue'].mean():,.2f}")

top_product = df.groupby("product_category")["net_revenue"].sum().idxmax()
print(f"Top Revenue Product: {top_product}")

# ── 5. Visualizations ────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Ecommerce Demand Planning Analytics", fontsize=16, fontweight="bold")

# Monthly revenue trend
monthly_total = df.groupby(["year", "month"])["net_revenue"].sum().reset_index()
monthly_total["period"] = monthly_total["year"].astype(str) + "-" + monthly_total["month"].astype(str).str.zfill(2)
axes[0, 0].plot(range(len(monthly_total)), monthly_total["net_revenue"], color="#2196F3", linewidth=2)
axes[0, 0].set_title("Monthly Revenue Trend")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Revenue ($)")
axes[0, 0].tick_params(axis="x", rotation=45)

# Revenue by product
product_revenue = df.groupby("product_category")["net_revenue"].sum().sort_values(ascending=True)
axes[0, 1].barh(product_revenue.index, product_revenue.values, color="#4CAF50")
axes[0, 1].set_title("Total Revenue by Product Category")
axes[0, 1].set_xlabel("Revenue ($)")

# Seasonality — avg units by month
seasonal = df.groupby("month")["net_units"].mean()
axes[1, 0].bar(seasonal.index, seasonal.values, color="#FF9800")
axes[1, 0].set_title("Avg Units Sold by Month (Seasonality)")
axes[1, 0].set_xlabel("Month")
axes[1, 0].set_ylabel("Avg Units Sold")
axes[1, 0].set_xticks(range(1, 13))

# Forecast accuracy
accuracy_by_product = forecast_df.groupby("product_category")["accuracy"].mean().sort_values()
axes[1, 1].barh(accuracy_by_product.index, accuracy_by_product.values, color="#9C27B0")
axes[1, 1].set_title("Forecast Accuracy by Product (%)")
axes[1, 1].set_xlabel("Accuracy (%)")
axes[1, 1].axvline(x=80, color="red", linestyle="--", label="80% threshold")
axes[1, 1].legend()

plt.tight_layout()
plt.savefig("demand_planning_analysis.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nPlot saved: demand_planning_analysis.png")

# ── 6. Export ────────────────────────────────────────────────────────────────
monthly_df.to_csv("monthly_demand_data.csv", index=False)
forecast_df.to_csv("demand_forecast_output.csv", index=False)
print("Exported: monthly_demand_data.csv, demand_forecast_output.csv")
print("\nDone!")
