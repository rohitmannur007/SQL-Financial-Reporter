import sqlite3
import pandas as pd
import os

DATA_PATH = "data/bank_transactions.csv"
DB_PATH = "data/bank.db"
REPORTS_DIR = "reports"

os.makedirs(REPORTS_DIR, exist_ok=True)


# ----------------------------
# Load raw CSV + normalize + create views
# ----------------------------
def load_csv_to_db():
    df = pd.read_csv(DATA_PATH)

    # 🔥 Normalize column names (critical fix)
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
    )

    # Auto-map messy Kaggle column names → clean SQL names
    rename_map = {}

    for col in df.columns:
        if "TransactionAmount" in col:
            rename_map[col] = "TransactionAmount"
        elif "CustAccountBalance" in col:
            rename_map[col] = "CustAccountBalance"
        elif "TransactionDate" in col:
            rename_map[col] = "TransactionDate"
        elif "CustomerID" in col:
            rename_map[col] = "CustomerID"
        elif "TransactionID" in col:
            rename_map[col] = "TransactionID"

    df = df.rename(columns=rename_map)

    conn = sqlite3.connect(DB_PATH)

    # Load raw table
    df.to_sql("transactions_raw", conn, if_exists="replace", index=False)

    # Create cleaned + regulatory SQL views
    with open("sql/create_views.sql", "r") as f:
        conn.executescript(f.read())

    # Create warehouse schema (fact + dimension tables)
    with open("sql/schema_upgrade.sql", "r") as f:
        conn.executescript(f.read())

    conn.close()

    print("✅ Data normalized + SQL warehouse created")


# ----------------------------
# Run SQL report → CSV
# ----------------------------
def run_query(name, sql_file):
    with open(sql_file, "r") as f:
        query = f.read()

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()

    df.to_csv(f"{REPORTS_DIR}/{name}.csv", index=False)

    print(f"✅ {name} report generated")


# ----------------------------
# Main pipeline
# ----------------------------
def main():
    load_csv_to_db()

    reports = {
        "profit_loss": "sql/profit_loss.sql",
        "balance_sheet": "sql/balance_sheet.sql",
        "risk_scoring": "sql/risk_scoring.sql",
        "customer_ranking": "sql/customer_ranking.sql",
        "anomalies": "sql/anomalies.sql",
        "fraud_detection": "sql/fraud_detection.sql",
        "cohort_analysis": "sql/cohort_analysis.sql",
        "customer_lifetime_value": "sql/customer_lifetime_value.sql",
    }

    for name, file in reports.items():
        run_query(name, file)


if __name__ == "__main__":
    main()