-- lists all genres of the show

SELECT tg.name FROM  tv_shows ts JOIN tv_show_genres tsg ON ts.id = tsg.show_id JOIN tv_genres tg ON tg.id = tsg.genre_id WHERE ts.title = 'Dexter' ORDER BY tg.name;