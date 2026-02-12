WITH aggregates AS (
    SELECT
        SUM(CustAccountBalance) AS total_balances,
        SUM(CASE WHEN TransactionAmount > 0 THEN TransactionAmount ELSE 0 END) AS inflows,
        SUM(CASE WHEN TransactionAmount < 0 THEN ABS(TransactionAmount) ELSE 0 END) AS outflows
    FROM cleaned_transactions
)

SELECT
    'Assets' AS category,
    total_balances + inflows AS amount
FROM aggregates

UNION ALL

SELECT
    'Liabilities',
    total_balances - outflows AS amount  -- Net liabilities post-outflows
FROM aggregates

UNION ALL

SELECT
    'Equity',
    inflows - outflows AS amount  -- Retained earnings proxy
FROM aggregates;