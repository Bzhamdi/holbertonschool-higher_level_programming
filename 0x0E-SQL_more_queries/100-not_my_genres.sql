-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT DISTINCT name FROM tv_genres tg WHERE tg.id NOT IN (SELECT genre_id FROM tv_show_genres tsg LEFT JOIN tv_shows ts ON ts.id = tsg.show_id WHERE ts.title = 'Dexter') 
ORDER BY tg.name ASC; 