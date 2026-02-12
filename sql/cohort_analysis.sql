WITH first_purchase AS (
    SELECT
        CustomerID,
        MIN(formatted_date) AS first_date
    FROM fact_transactions
    GROUP BY CustomerID
),

cohorts AS (
    SELECT
        f.CustomerID,
        strftime('%Y-%m', fp.first_date) AS cohort_month,
        strftime('%Y-%m', f.formatted_date) AS activity_month
    FROM fact_transactions f
    JOIN first_purchase fp
      ON f.CustomerID = fp.CustomerID
)

SELECT
    cohort_month,
    activity_month,
    COUNT(DISTINCT CustomerID) AS active_customers
FROM cohorts
GROUP BY cohort_month, activity_month
ORDER BY cohort_month, activity_month;