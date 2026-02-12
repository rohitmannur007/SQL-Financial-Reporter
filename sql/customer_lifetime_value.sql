SELECT
    CustomerID,
    COUNT(*) AS total_transactions,
    SUM(TransactionAmount) AS lifetime_value,
    AVG(TransactionAmount) AS avg_transaction_value
FROM fact_transactions
GROUP BY CustomerID
ORDER BY lifetime_value DESC;