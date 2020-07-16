-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.

SELECT tg.name, SUM(rate) AS rating FROM tv_genres tg
JOIN tv_show_genres tsg ON tsg.genre_id = tg.id
JOIN tv_show_ratings tsr ON tsr.show_id = tsg.show_id
GROUP BY tg.name ORDER BY rating DESC;
