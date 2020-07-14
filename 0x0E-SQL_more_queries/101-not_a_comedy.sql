-- lists all shows without the genre Comedy in the database 

SELECT DISTINCT ts.title 
FROM tv_shows ts WHERE ts.id NOT IN (SELECT show_id FROM tv_show_genres tsg INNER JOIN tv_genres tg ON tg.id = stg.genre_id WHERE tg.name = 'Comedy') ORDER BY ts.title ASC; 