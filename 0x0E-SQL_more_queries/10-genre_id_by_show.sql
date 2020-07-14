-- join 

SELECT t.title, tg.genre_id from tv_shows t join tv_show_genres tg on tg.show_id = t.id order by t.title ,tg.genre_id;
