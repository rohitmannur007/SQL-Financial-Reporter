SELECT
    CustomerID,
    total_spend,
    RANK() OVER (ORDER BY total_spend DESC) AS spending_rank,
    DENSE_RANK() OVER (ORDER BY total_spend DESC) AS dense_rank,  -- Handles ties
    PERCENT_RANK() OVER (ORDER BY total_spend) * 100 AS percentile_spend  -- Elite: Distribution
FROM (
    SELECT CustomerID, SUM(TransactionAmount) AS total_spend
    FROM cleaned_transactions
    GROUP BY CustomerID
) sub
ORDER BY spending_rank;