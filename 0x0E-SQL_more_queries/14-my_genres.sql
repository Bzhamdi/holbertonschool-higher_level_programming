-- lists all genres of the show
SELECT t.name FROM tv_genres t
JOIN tv_show_genres tg ON t.id = tg.genre_id
JOIN tv_shows ts ON ts.id = tg.show_id
WHERE ts.title = 'Dexter' ORDER BY tg.name;