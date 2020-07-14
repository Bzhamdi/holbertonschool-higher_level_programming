-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.

SELECT ts.name, SUM(tsr.rate) AS rating FROM ts INNER JOIN tsg
ON ts.id = tsg.genre_id INNER JOIN tsr
ON tsg.show_id = tsr.show_id GROUP BY ts.id ORDER BY rating DESC;