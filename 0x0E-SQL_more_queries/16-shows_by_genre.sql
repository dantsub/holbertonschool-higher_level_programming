-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_s.`title`, tv_g.`name`
FROM `tv_shows` AS tv_s
LEFT JOIN `tv_show_genres` AS tv_sg
       ON tv_s.`id` = tv_sg.`show_id`
LEFT JOIN `tv_genres` AS tv_g
       ON tv_sg.`genre_id` = tv_g.`id`
ORDER BY tv_s.`title`, tv_g.`name`;
