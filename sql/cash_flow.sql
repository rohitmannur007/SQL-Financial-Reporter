SELECT
    strftime('%Y-%m', TransactionDate) AS Month,
    SUM(TransactionAmount) * -1 AS Cash_Outflow,
    SUM(CustAccountBalance) AS Cash_Inflow,
    SUM(CustAccountBalance) - SUM(TransactionAmount) AS Net_Cash_Flow
FROM transactions
WHERE TransactionDate IS NOT NULL
GROUP BY Month
ORDER BY Month;