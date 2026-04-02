# 📊 Sales Analysis Project

## 🚀 Overview

This project focuses on cleaning, transforming, and analyzing sales data using Python (Pandas) and MySQL.
The goal was to build a complete data pipeline and extract meaningful business insights from raw transactional data.

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy)
* MySQL
* Git & GitHub

---

## 🔄 Data Pipeline

1. Extracted data from MySQL database
2. Cleaned and standardized column names
3. Merged multiple tables:

   * customers
   * products
   * markets
   * transactions
   * date
4. Handled missing values and inconsistencies
5. Removed duplicate records
6. Converted date columns to datetime format
7. Performed feature engineering:

   * `year_month`
   * `price_per_unit`
   * `is_return`
8. Validated data quality and anomalies

---

## 🧹 Data Cleaning Highlights

* Fixed inconsistent column names (e.g. `markets_code` → `market_code`)
* Standardized date formats across tables
* Handled missing values (~36% in `product_type`)
* Removed duplicate records
* Identified zero-value transactions (~1%) and handled them separately

---

## 📊 Key Analysis

* Revenue trends over time (monthly & yearly)
* Sales performance by market and region
* Top customers and product categories
* Customer segmentation (E-Commerce vs Brick & Mortar)

---

## 📈 Dataset

* ~150,000+ rows
* Cleaned and validated dataset ready for analysis and visualization

---

## 💡 Key Learnings

* End-to-end data pipeline development
* Data cleaning and validation techniques
* Handling real-world data issues (missing values, inconsistencies, anomalies)
* Feature engineering for business analysis
## 📊 Key Insights

### 📈 Revenue Trends (2017–2020)

* Revenue increased significantly from 2017 to 2019, indicating strong business growth.
* Peak performance was observed in 2018–2019, with the highest monthly spikes.
* A clear decline is visible in 2020, suggesting potential external disruption or incomplete data.

---

### 🌍 Market Performance

* Revenue is highly concentrated in a few top markets (e.g., Delhi NCR, Mumbai).
* The top market alone contributes over 50% of total revenue in some years.
* Several markets show negative or very low contribution, indicating underperformance or inefficiency.

---

### 🧑‍💼 Customer Insights

* A small number of customers generate a disproportionately large share of revenue.
* The top customer contributes significantly more than others, confirming a strong Pareto effect.
* This indicates high dependency on key accounts, which may pose business risk.

---

### 📦 Product Performance

* A few products dominate sales, with the top product significantly outperforming others.
* There is a steep drop-off after top products, indicating limited diversification in revenue streams.

---

### 💰 Profitability Analysis

* Profit margins fluctuate across months and markets.
* Some markets show negative profit contribution despite generating revenue.
* Profitability is not evenly distributed and depends heavily on specific regions and customers.

---

### 📉 Performance Variability

* Revenue trends show noticeable fluctuations month-to-month, indicating potential seasonality or demand volatility.
* Sharp peaks followed by drops suggest inconsistent sales performance.

---

### ⚠️ Business Risks & Opportunities

* Heavy reliance on a few markets and customers increases business risk.
* Underperforming markets represent an opportunity for optimization or expansion strategies.
* Decline in 2020 suggests need for further investigation into external or operational factors.



## 📌 Author

GitHub: https://github.com/aaraszewska
