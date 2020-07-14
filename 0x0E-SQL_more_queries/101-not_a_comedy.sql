-- lists all shows without the genre Comedy in the database 

SELECT ts.title FROM tv_shows ts WHERE ts.id NOT IN (SELECT ts.id FROM tv_shows ts INNER JOIN tv_show_genres tsg ON ts.id = tsg.show_id INNER JOIN tv_genres tg ON tsg.genre_id = ts.id
WHERE tg.name = "Comedy")
ORDER BY ts.title;