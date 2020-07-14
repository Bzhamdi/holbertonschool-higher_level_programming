-- selct 

SELECT t.title, tg.genre_id FROM tv_shows t LEFT JOIN tv_shows_genres tg ON tg.show_id=t.id ORDER BY t.title, tg.genre_id;