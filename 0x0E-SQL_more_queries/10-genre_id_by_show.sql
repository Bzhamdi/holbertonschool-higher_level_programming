-- join

SELECT t.title, tg.genre_id FROM tv_shows t JOIN tv_show_genres tg on tg.show_id = t.id ORDER BY t.title ,tg.genre_id;
