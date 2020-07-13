-- no link
SELECT score, name FROM second_table WHERE name IS NOT NULL GROUP BY score, name ORDER BY score DESC;
