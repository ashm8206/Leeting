-- Write your PostgreSQL query statement below

select
    TO_CHAR(trans_date, 'YYYY-MM') as month,
   country,
   count(trans_date) as trans_count,
   count(case when state = 'approved' then trans_date else NULL end) as approved_count,
   sum(amount) as trans_total_amount,
   sum(case when state = 'approved' then amount  else 0 end) as approved_total_amount
from Transactions
group by 1,2
