# Write your MySQL query statement below
SELECT P.product_name, S.year, S.Price 
FROM Sales AS S
JOIN Product AS P ON S.product_id= P.product_id



;