-- Write your PostgreSQL query statement below
with clean_user as ( 
        select
            users_id,
            role
        from Users
        where banned = 'No'
)
select
    request_at as "Day" ,
    ROUND (CAST(SUM(CASE WHEN STATUS != 'completed' THEN 1 ELSE 0 END) / CAST(COUNT(id) AS FLOAT) AS NUMERIC ) , 2)  as "Cancellation Rate"
from trips t
join clean_user c on  c.users_id = client_id
join clean_user d on  d.users_id = driver_id 
where request_at >=  '2013-10-01' and request_at <= '2013-10-03'
-- order by 1
group by 1