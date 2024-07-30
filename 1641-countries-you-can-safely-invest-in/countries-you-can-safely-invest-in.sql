-- Write your PostgreSQL query statement below
-- with users as (
--     select
--     p.id,
--     p.name
--     ,c.name as country_name
-- from person p
-- left join country c
--     on SUBSTRING(p.phone_number,1,3) = c.country_code
-- )
-- , avg_by_country_cte as (
--     select 
--     caller_id,
--     callee_id,
--     duration,
--     ucaller.country_name as caller_country,
--     ucallee.country_name as callee_country,
--     AVG(duration) OVER(partition by ucaller.country_name) avg_by_country,
--     AVG(duration) OVER() avg_global
-- from calls c
-- join users ucaller
--     on ucaller.id = c.caller_id
-- join users ucallee
--     on ucallee.id = c.callee_id
-- )

-- select
--     distinct caller_country as country
-- from avg_by_country_cte
-- where avg_by_country > avg_global


SELECT
 co.name AS country
FROM
 person p
 JOIN
     country co
     ON SUBSTRING(phone_number,1,3) = country_code
 JOIN
     calls c
     ON p.id IN (c.caller_id, c.callee_id)
GROUP BY
 co.name
HAVING
 AVG(duration) > (SELECT AVG(duration) FROM calls)






