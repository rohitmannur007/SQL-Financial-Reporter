DROP VIEW IF EXISTS cleaned_transactions;

CREATE VIEW cleaned_transactions AS
SELECT
    TransactionID,
    CustomerID,
    date(TransactionDate) AS formatted_date,
    COALESCE(CAST(CustAccountBalance AS REAL), 0) AS CustAccountBalance,
    COALESCE(CAST(TransactionAmount AS REAL), 0) AS TransactionAmount
FROM transactions_raw
WHERE TransactionID IS NOT NULL;


DROP VIEW IF EXISTS regulatory_summary;

CREATE VIEW regulatory_summary AS
SELECT
    strftime('%Y-%m', formatted_date) AS month,
    COUNT(*) AS txn_count,
    SUM(TransactionAmount) AS total_volume,
    AVG(TransactionAmount) AS avg_txn_amount
FROM cleaned_transactions
GROUP BY month;