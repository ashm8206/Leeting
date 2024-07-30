-- Write your PostgreSQL query statement below
with cte as (
    select distinct l1.id
from logins l1 
join logins l2 on l1.id=l2.id and l1.login_date+ interval '1 day' = l2.login_date
join logins l3 on l3.id=l2.id and l2.login_date+interval '1 day' = l3.login_date
join logins l4 on l4.id=l3.id and l3.login_date+interval '1 day' = l4.login_date
join logins l5 on l5.id=l4.id and l4.login_date + interval '1 day' = l5.login_date
)
select id, name from accounts
where id in (select distinct id from  cte)
order by id 
;