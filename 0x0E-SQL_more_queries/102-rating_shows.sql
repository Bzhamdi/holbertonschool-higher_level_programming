-- lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT t.title, SUM(tsg.rate) AS rating FROM tv_shows ts INNER JOIN tv_show_ratings tsg
ON ts.id = tsg.show_id GROUP BY ts.id ORDER BY rating DESC;