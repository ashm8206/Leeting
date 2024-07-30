-- Write your PostgreSQL query statement below
    with cte as (
            Select
                customer_id,
                min(order_date) min_order_date
    from delivery
    group by customer_id
    )

    select 
        Round(COUNT(
                CASE WHEN 
                    order_date = customer_pref_delivery_date 
                    THEN order_date 
                    ELSE NULL 
                END)*100 / count(delivery_id)::numeric,2) as immediate_percentage
    from delivery d
    join cte c
    on c.customer_id = d.customer_id
    and d.order_date = min_order_date

