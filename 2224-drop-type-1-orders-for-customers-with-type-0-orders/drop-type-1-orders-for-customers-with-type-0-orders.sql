-- Write your PostgreSQL query statement below
select
    order_id,
    customer_id,
    order_type
from orders
where customer_id not in (
    SELECT 
        distinct customer_id
    from orders
    where order_type = 0
) or order_type = 0;