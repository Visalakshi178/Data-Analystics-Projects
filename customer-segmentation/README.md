# 🛍️ Customer Segmentation & Marketing Analytics

> Identifying high-value audience segments using K-Means clustering to drive targeted marketing campaigns and improve ROI.

## 📊 Overview

This project applies unsupervised machine learning (K-Means clustering) to segment customers based on behavioral and demographic data. The resulting segments inform targeted marketing strategies, contributing to a **12% lift in campaign ROI**.

## 🛠️ Tools & Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📁 Project Structure

```
customer-segmentation/
│
├── customer_segmentation.py   # Main analysis script
├── customer_segments_output.csv  # Output with cluster labels
├── segmentation_analysis.png  # Visualizations
└── README.md
```

## 🔍 Key Steps

1. **Data Generation** — Simulated 500 customer records with income, spending, frequency, and region
2. **EDA** — Explored distributions, missing values, and correlations
3. **Feature Engineering** — Created ROI score and value segment features
4. **K-Means Clustering** — Used elbow method + silhouette score to find optimal k
5. **Segment Profiling** — Analyzed each cluster's behavioral characteristics
6. **Recommendations** — Mapped each segment to targeted marketing strategies

## 📈 Results

| Segment | Strategy |
|---------|----------|
| Budget Shoppers | Discount campaigns & loyalty rewards |
| High Value Loyalists | VIP perks & personalized offers |
| Occasional Buyers | Re-engagement email campaigns |
| Premium Customers | Upsell & exclusive membership tiers |

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python customer_segmentation.py
```

## 📬 Contact

**Visalakshi Polepalli** — [LinkedIn](https://linkedin.com/in/visalakshi-polepalli17)
