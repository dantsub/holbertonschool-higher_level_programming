-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_s.`title`, tc_g.`name`
FROM `tv_shows` AS tv_s
LEFT JOIN `tv_show_genres` AS tv_sg
       ON tv_s.`id` = tv_sg.`show_id`
LEFT JOIN `tv_genres` AS g
       ON tv_sg.`genre_id` = g.`id`
ORDER BY tv_s.`title`, g.`name`;
