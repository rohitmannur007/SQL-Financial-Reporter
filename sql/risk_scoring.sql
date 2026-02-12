WITH customer_stats AS (
    SELECT
        CustomerID,
        COUNT(*) AS txn_count,
        SUM(TransactionAmount) AS total_spend,
        AVG(TransactionAmount) AS avg_txn
    FROM cleaned_transactions
    GROUP BY CustomerID
),

stats AS (
    SELECT
        AVG(total_spend) AS mean_spend,
        sqrt(AVG(total_spend * total_spend) -
             AVG(total_spend) * AVG(total_spend)) AS std_spend
    FROM customer_stats
),

z_scores AS (
    SELECT
        cs.*,
        (cs.total_spend - s.mean_spend) /
        NULLIF(s.std_spend, 0) AS spend_zscore
    FROM customer_stats cs
    CROSS JOIN stats s
)

SELECT
    *,
    CASE
        WHEN spend_zscore > 2 THEN 'HIGH'
        WHEN spend_zscore > 1 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS risk_level
FROM z_scores
ORDER BY total_spend DESC;