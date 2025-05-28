# Write your MySQL query statement below
SELECT score,   DENSE_RANK() OVER ( ORDER BY Score Desc) AS "Rank"
FROM Scores
