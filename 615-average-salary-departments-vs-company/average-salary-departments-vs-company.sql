-- Write your PostgreSQL query statement below

with cte as (
    select
    TO_CHAR(pay_date,'YYYY-MM') as pay_month,
    department_id,
    AVG(amount) avg_dep
from salary s
join  employee e
    on s.employee_id = e.employee_id
group by 1,2
)
, total_avg_cte as (
    Select
    TO_CHAR(pay_date,'YYYY-MM') pay_month,
    AVG(amount) total_avg
from salary
group by 1
)
Select
    c.pay_month,
    c.department_id,
    case when avg_dep < total_avg then 'lower'
         when avg_dep > total_avg then 'higher'
        else 'same'
    end as  comparison
from cte c
join total_avg_cte t
    on c.pay_month = t.pay_month