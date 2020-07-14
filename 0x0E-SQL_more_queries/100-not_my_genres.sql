-- list all genres not linked to the show Dexter

SELECT tg.name FROM tv_genres tg WHERE tg.id NOT IN (SELECT tg.id FROM tv_genres tg
INNER JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
INNER JOIN tv_shows ts
ON tsg.show_id = ts.id
WHERE ts.title = "Dexter")
ORDER BY tg.name;