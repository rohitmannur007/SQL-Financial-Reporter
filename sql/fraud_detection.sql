WITH baselines AS (
    SELECT
        CustomerID,
        AVG(TransactionAmount) AS avg_amt,
        sqrt(AVG(TransactionAmount * TransactionAmount) -
             AVG(TransactionAmount) * AVG(TransactionAmount)) AS std_amt
    FROM cleaned_transactions
    GROUP BY CustomerID
),

flagged AS (
    SELECT
        t.*,
        b.avg_amt,
        b.std_amt,
        (t.TransactionAmount - b.avg_amt) /
        NULLIF(b.std_amt, 0) AS z_score
    FROM cleaned_transactions t
    JOIN baselines b
      ON t.CustomerID = b.CustomerID
)

SELECT
    TransactionID,
    CustomerID,
    formatted_date AS TransactionDate,
    TransactionAmount,
    z_score,
    CASE
        WHEN z_score > 3 THEN 'SUSPICIOUS'
        ELSE 'OK'
    END AS fraud_status
FROM flagged
WHERE z_score > 3
ORDER BY z_score DESC;