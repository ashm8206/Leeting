-- Write your PostgreSQL query statement below
with cte as 
    (
        select
        person_name,
        SUM(weight) OVER(order by turn asc) as cumm_sum
    from queue
)
select
    person_name
from cte
where cumm_sum <= 1000
order by cumm_sum desc 
limit 1