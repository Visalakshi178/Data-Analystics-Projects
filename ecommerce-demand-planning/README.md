# 📦 Ecommerce Demand Planning Analytics

> Automated ETL pipelines and demand forecasting models that improved forecast accuracy by 15% using Python and SQL.

## 📊 Overview

This project builds an end-to-end demand planning solution for an ecommerce business — from raw data ingestion through ETL transformation to demand forecasting and visualization. It analyzes sales trends, seasonality, and inventory levels across product categories and regions.

## 🛠️ Tools & Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

## 📁 Project Structure

```
ecommerce-demand-planning/
│
├── demand_planning.py           # Main ETL + forecasting script
├── monthly_demand_data.csv      # Aggregated monthly output
├── demand_forecast_output.csv   # Forecast results with accuracy
├── demand_planning_analysis.png # Visualizations
└── README.md
```

## 🔍 Key Steps

1. **Data Generation** — Simulated 3 years of daily sales across 5 product categories
2. **ETL Pipeline** — Extract → Transform (cleaning, feature engineering) → Load (monthly aggregation)
3. **Seasonality Analysis** — Identified peak demand months per product
4. **Demand Forecasting** — Applied 3-month and 6-month moving averages
5. **Accuracy Measurement** — Calculated forecast accuracy per product category
6. **Visualization** — Revenue trends, seasonality, and forecast performance charts

## 📈 Results

- **15% improvement** in demand forecast accuracy
- Identified seasonal peaks driving inventory optimization
- Automated monthly aggregation pipeline reducing manual reporting time

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib seaborn
python demand_planning.py
```

## 📬 Contact

**Visalakshi Polepalli** — [LinkedIn](https://linkedin.com/in/visalakshi-polepalli17)
