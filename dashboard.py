import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "data/bank.db"

st.set_page_config(page_title="Financial Dashboard", layout="wide")

st.title("📊 SQL Financial Reporting Dashboard")

def load_query(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

st.sidebar.header("Reports")

report = st.sidebar.selectbox(
    "Choose report",
    ["Profit & Loss", "Balance Sheet", "Cash Flow", "Anomalies"]
)

if report == "Profit & Loss":
    df = load_query("""
        SELECT
            strftime('%Y-%m', TransactionDate) AS Month,
            SUM(TransactionAmount) AS Expenses
        FROM transactions
        GROUP BY Month
        ORDER BY Month
    """)
    st.subheader("Profit & Loss")
    st.dataframe(df)
    st.line_chart(df.set_index("Month"))

elif report == "Balance Sheet":
    df = load_query("""
        WITH cleaned AS (
            SELECT
                COALESCE(CAST(CustAccountBalance AS REAL), 0) AS balance,
                COALESCE(CAST(TransactionAmount AS REAL), 0) AS txn
            FROM transactions
        )
        SELECT
            'Assets' AS Category,
            SUM(balance + txn) AS Amount
        FROM cleaned
        UNION ALL
        SELECT
            'Liabilities',
            SUM(balance)
        FROM cleaned
        UNION ALL
        SELECT
            'Equity',
            SUM(txn)
        FROM cleaned;
    """)
    st.subheader("Balance Sheet")
    st.dataframe(df)
    st.bar_chart(df.set_index("Category"))

elif report == "Cash Flow":
    df = load_query("""
        SELECT
            strftime('%Y-%m', TransactionDate) AS Month,
            SUM(TransactionAmount) AS CashFlow
        FROM transactions
        GROUP BY Month
        ORDER BY Month
    """)
    st.subheader("Cash Flow")
    st.dataframe(df)
    st.line_chart(df.set_index("Month"))

elif report == "Anomalies":
    df = load_query("""
        SELECT
            TransactionID,
            CustomerID,
            TransactionAmount
        FROM transactions
        WHERE TransactionAmount > 100000
        ORDER BY TransactionAmount DESC
    """)
    st.subheader("Anomaly Detection")
    st.dataframe(df)
