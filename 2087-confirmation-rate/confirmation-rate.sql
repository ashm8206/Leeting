-- Write your PostgreSQL query statement below

Select
    u.user_id,
    CASE WHEN ROUND( count(case when action = 'confirmed' then action else NULL end)/ NULLIF(count(action)::numeric,0), 2)  IS NULL THEN 0
    ELSE 
        ROUND( count(case when action = 'confirmed' then action else NULL end)/ NULLIF(count(action)::numeric,0), 2)
    END
    AS confirmation_rate
from signups u
left join confirmations c
on u.user_id = c.user_id
group by 1;