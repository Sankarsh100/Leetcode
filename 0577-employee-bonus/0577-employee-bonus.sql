# Write your MySQL query statement below
SELECT E.name, B.bonus
From Employee AS E
LEFT JOIN BONUS AS B 
ON E.empId=B.empId
WHERE B.bonus<1000 OR B.bonus IS NULL
;