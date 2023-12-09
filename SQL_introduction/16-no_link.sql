-- script that lists the number of records with the same score
-- Lists the number of records with the same score in the table second_table with conditions
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;
