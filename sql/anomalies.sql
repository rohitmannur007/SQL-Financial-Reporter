WITH customer_anomalies AS (
    SELECT
        *,
        PERCENT_RANK() OVER (
            PARTITION BY CustomerID 
            ORDER BY TransactionAmount DESC
        ) AS txn_percentile
    FROM cleaned_transactions
    WHERE TransactionAmount > 0
)

SELECT
    TransactionID,
    CustomerID,
    formatted_date AS TransactionDate,
    TransactionAmount
FROM customer_anomalies
WHERE txn_percentile <= 0.05  -- Top 5% per customer = anomaly
ORDER BY CustomerID, TransactionAmount DESC;