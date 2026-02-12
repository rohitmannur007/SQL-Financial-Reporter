import streamlit as st
import sqlite3
import pandas as pd

# ==============================
# PAGE CONFIG (Dark executive UI)
# ==============================

st.set_page_config(
    page_title="Financial Intelligence Platform",
    layout="wide"
)

st.title("🏦 Financial Intelligence Platform")

DB_PATH = "data/bank.db"


# ==============================
# FAST SQL ENGINE (cached)
# ==============================

@st.cache_data
def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


# ==============================
# GLOBAL FILTERS
# ==============================

st.sidebar.header("🎛 Global Filters")

date_filter = st.sidebar.checkbox("Last 12 Months Only")

customer_filter = st.sidebar.text_input(
    "Filter Customer ID (optional)"
)

base_query = "SELECT * FROM cleaned_transactions"

if customer_filter:
    base_query += f" WHERE CustomerID = '{customer_filter}'"

transactions = run_query(base_query)


# ==============================
# KPI EXECUTIVE SUMMARY
# ==============================

kpi = run_query("""
SELECT
    COUNT(*) AS total_txn,
    COUNT(DISTINCT CustomerID) AS customers,
    SUM(TransactionAmount) AS volume,
    AVG(TransactionAmount) AS avg_txn
FROM cleaned_transactions
""")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Transactions", f"{int(kpi.iloc[0,0]):,}")
col2.metric("Customers", f"{int(kpi.iloc[0,1]):,}")
col3.metric("Total Volume", f"₹{kpi.iloc[0,2]:,.0f}")
col4.metric("Avg Transaction", f"₹{kpi.iloc[0,3]:,.0f}")

st.divider()


# ==============================
# TABS (Executive drill-down)
# ==============================

tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Financial Trend",
    "⚠️ Risk & Fraud",
    "🏆 Customers",
    "📅 Cohort Intelligence"
])


# ==============================
# TAB 1 — FINANCIAL TREND
# ==============================

with tab1:

    st.subheader("Monthly Financial Performance")

    pnl = run_query("""
    SELECT * FROM regulatory_summary
    ORDER BY month
    """)

    st.line_chart(
        pnl.set_index("month")[["total_volume", "avg_txn_amount"]]
    )

    st.dataframe(pnl, use_container_width=True)


# ==============================
# TAB 2 — RISK & FRAUD
# ==============================

with tab2:

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Risk Distribution")

        risk = run_query(open("sql/risk_scoring.sql").read())

        risk_counts = risk["risk_level"].value_counts()

        st.bar_chart(risk_counts)

        st.dataframe(risk.head(20), use_container_width=True)

    with col2:
        st.subheader("Fraud Detection")

        fraud = run_query(open("sql/fraud_detection.sql").read())

        st.metric("Suspicious Transactions", len(fraud))

        if not fraud.empty:
            st.bar_chart(
                fraud.head(20)
                .set_index("TransactionID")["TransactionAmount"]
            )

        st.dataframe(fraud.head(20), use_container_width=True)


# ==============================
# TAB 3 — CUSTOMER ANALYTICS
# ==============================

with tab3:

    st.subheader("Top Customers by Spend")

    ranking = run_query(open("sql/customer_ranking.sql").read())

    st.bar_chart(
        ranking.head(20)
        .set_index("CustomerID")["total_spend"]
    )

    st.subheader("Customer Lifetime Value")

    clv = run_query(open("sql/customer_lifetime_value.sql").read())

    st.bar_chart(
        clv.head(20)
        .set_index("CustomerID")["lifetime_value"]
    )

    st.dataframe(clv.head(50), use_container_width=True)


# ==============================
# TAB 4 — COHORT INTELLIGENCE
# ==============================

with tab4:

    st.subheader("Customer Retention Matrix")

    cohort = run_query(open("sql/cohort_analysis.sql").read())

    pivot = cohort.pivot(
        index="cohort_month",
        columns="activity_month",
        values="active_customers"
    )

    st.dataframe(pivot, use_container_width=True)


st.divider()

st.caption("⚡ Powered by Advanced SQL Warehouse Architecture")