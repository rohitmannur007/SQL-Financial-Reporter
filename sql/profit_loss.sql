WITH monthly AS (
    SELECT
        rs.month,
        rs.total_volume AS expenses,  -- Use actual volume
        rs.total_volume * 1.2 AS revenue  -- Elite: Dynamic revenue (e.g., 20% margin)
    FROM regulatory_summary rs
)

SELECT
    month,
    expenses,
    revenue,
    revenue - expenses AS net_profit,
    (revenue - expenses) / revenue * 100 AS profit_margin_pct
FROM monthly
ORDER BY month;