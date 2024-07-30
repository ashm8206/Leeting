-- Write your PostgreSQL query statement below
Select
    user_id as buyer_id,
    join_date,
    COUNT(case when order_date between '2019-01-01' AND '2019-12-31' THEN order_date ELSE NULL END ) as orders_in_2019
from users u
left join orders o
on u.user_id = o.buyer_id
GROUP by 1, 2
order by 1

