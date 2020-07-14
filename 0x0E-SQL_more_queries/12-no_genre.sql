-- lists all shows contained in hbtn_0d_tvshows without a genre linked. 

Select t.title , tg.genre_id FROM tv_show_genres tg LEFT JOIN tv_shows t ON t.id = tg.show_id WHERE tg.show_id IS NULL ORDER BY t.title, tg.genre_id;