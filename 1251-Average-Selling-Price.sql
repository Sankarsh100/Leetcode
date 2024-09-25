# Write your MySQL query statement below
WITH TotalSales AS (
    SELECT 
        p.product_id,
        SUM(us.units * p.price) AS total_revenue,
        SUM(us.units) AS total_units
    FROM Prices p
    JOIN UnitsSold us
    ON p.product_id = us.product_id
    AND us.purchase_date BETWEEN p.start_date AND p.end_date
    GROUP BY p.product_id
)
SELECT
    p.product_id,
    ROUND(COALESCE(ts.total_revenue / NULLIF(ts.total_units, 0), 0), 2) AS average_price
FROM Prices p
LEFT JOIN TotalSales ts
ON p.product_id = ts.product_id
GROUP BY p.product_id;
