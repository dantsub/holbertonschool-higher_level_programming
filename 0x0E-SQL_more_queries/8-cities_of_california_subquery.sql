-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT c.`id`, c.`name`
FROM `states` AS s, `cities` AS c
WHERE s.`id` = c.`state_id` AND s.`name` = "California";
