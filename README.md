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

---

## 🔜 Next Steps

* Build interactive dashboard (Tableau / Power BI)
* Add advanced analysis (customer segmentation, forecasting)

---

## 📌 Author

GitHub: https://github.com/aaraszewska
