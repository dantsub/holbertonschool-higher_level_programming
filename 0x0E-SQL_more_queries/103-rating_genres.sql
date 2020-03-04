-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT `name`, SUM(`rate`) AS `rating`
FROM `tv_genres` AS tv_g
INNER JOIN `tv_show_genres` AS tv_sg
       ON tv_sg.`genre_id` = tv_g.`id`
INNER JOIN `tv_show_ratings` AS tv_r
       ON tv_r.`show_id` = tv_sg.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;
