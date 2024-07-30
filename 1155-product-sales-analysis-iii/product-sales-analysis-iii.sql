-- Write your PostgreSQL query statement below

    select
        product_id,
        year as first_year, 
        quantity,
        price
    from sales p1
    where year = (
            select 
                min(year) 
            from sales p2
            where p1.product_id = p2.product_id
     group by p2.product_id )
