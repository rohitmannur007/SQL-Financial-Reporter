# 🏦 Advanced SQL Financial Intelligence Platform

An end-to-end **SQL-centric financial analytics platform** that simulates how modern banking systems generate regulatory and business intelligence reports.

This project implements a **mini financial data warehouse** powered by advanced SQL analytics, automated pipelines, and an interactive executive dashboard.

It demonstrates real-world skills in:

- Advanced SQL engineering
- Data warehouse architecture
- Financial analytics
- Risk & fraud modeling
- Business intelligence dashboards

---

## 🚀 Project Overview

This system builds a complete **SQL-driven analytics pipeline**:

1. Ingest raw banking transaction data
2. Normalize and structure it into a warehouse schema
3. Create reusable SQL views
4. Run advanced analytics queries
5. Generate automated financial reports
6. Visualize insights in an professional dashboard

The architecture mirrors workflows used in **financial institutions and analytics platforms**.

---

## 🏗️ Warehouse Architecture

```
Raw CSV → SQL Cleaning Views → Fact/Dimension Tables
             ↓
       Advanced SQL Analytics
             ↓
       Executive Dashboard
```

### Schema Design

- **fact_transactions** → transaction facts
- **dim_customers** → customer dimension
- **cleaned_transactions** → reusable analytics view
- **regulatory_summary** → aggregated reporting view

This follows **star-schema warehouse principles** used in enterprise systems.

---

## 📈 Advanced SQL Analytics Implemented

This project showcases **elite SQL techniques**:

### 🔹 Financial Reporting Queries

- Monthly Profit & Loss statements
- Balance sheet simulation
- Regulatory transaction summaries

### 🔹 Risk Scoring Engine

Uses:

- Aggregations
- Z-score normalization
- Statistical classification

Example:

```sql
(total_spend - mean_spend) / std_spend AS risk_score
```

### 🔹 Fraud Detection System

Implements:

- Customer transaction baselines
- Outlier detection using z-scores
- Suspicious activity flagging

### 🔹 Customer Ranking

Uses advanced window functions:

```sql
RANK() OVER (ORDER BY total_spend DESC)
DENSE_RANK()
PERCENT_RANK()
```

### 🔹 Cohort Analysis

Tracks customer retention over time using:

- First activity grouping
- Monthly cohort matrices

### 🔹 Customer Lifetime Value (CLV)

Calculates:

- Total spend per customer
- Average transaction behavior
- Revenue contribution ranking

---

## 🛠️ Core SQL Techniques Demonstrated

This project highlights:

- Complex CTE pipelines
- Window functions
- Statistical modeling in SQL
- Star schema design
- Aggregations & subqueries
- View-based ETL architecture
- Warehouse-style analytics

---

## 🖥️ Interactive Dashboard

The Streamlit dashboard provides:

- Executive KPI summary
- Financial trend visualization
- Risk & fraud analytics
- Customer intelligence
- Cohort retention matrix
- Lifetime value insights

Designed to resemble a **financial intelligence platform**.

---

## 🛠️ Tech Stack

- **SQL (SQLite)** — Advanced analytics engine
- **Python (Pandas)** — Data ingestion orchestration
- **Streamlit** — Interactive dashboard
- **Data Warehouse Design** — Star schema architecture

---

## 📂 Project Structure

```
financial-intelligence-platform/
│
├── data/        # Raw dataset + database
├── sql/         # Advanced analytics queries
├── scripts/     # ETL pipeline
├── reports/     # Generated outputs
├── dashboard.py # Executive dashboard
└── README.md
```

---

## ⚙️ Installation & Usage

### 1. Add dataset

Place:

```
bank_transactions.csv
```

inside:

```
data/
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run warehouse pipeline

```
python scripts/main.py
```

### 4. Launch dashboard

```
streamlit run dashboard.py
```

---

## 📸 Dashboard Preview

*(Add screenshots here — KPI view, charts, cohort matrix, etc.)*

---

## 💡 Skills Demonstrated

This project demonstrates expertise in:

- Advanced SQL analytics
- Data warehouse architecture
- Financial data modeling
- Risk and fraud detection logic
- ETL pipeline design
- Business intelligence dashboards

---

## 🎯 Real-World Applications

Relevant to:

- Banking analytics platforms
- Regulatory reporting systems
- Fraud detection pipelines
- Financial intelligence dashboards
- Data warehouse engineering

---

## 🔮 Future Enhancements

- Real-time streaming analytics
- Cloud data warehouse deployment
- Machine learning fraud models
- API-based reporting system

---

## 👨‍💻 Author

**Rohit Mannur**

SQL & Data Analytics Engineer

---

## ⭐ If you found this project useful

Feel free to star ⭐ the repository or suggest improvements!