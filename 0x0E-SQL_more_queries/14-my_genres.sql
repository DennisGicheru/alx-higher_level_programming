-- script that uses the hbtn_0d_tvshows to list all genres of show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
SELECT tv_genres.name name
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title LIKE '%Dexter%'
ORDER BY tv_genres.name ASC;
