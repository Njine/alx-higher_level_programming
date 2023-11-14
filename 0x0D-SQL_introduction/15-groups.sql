-- MySQL script to list the count of records with the same score value
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
