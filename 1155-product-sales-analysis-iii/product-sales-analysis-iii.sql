-- Write your PostgreSQL query statement below

    -- select
    --     product_id,
    --     year as first_year, 
    --     quantity,
    --     price
    -- from sales p1
    -- where year = (
    --         select 
    --             min(year) 
    --         from sales p2
    --         where p1.product_id = p2.product_id
    --  group by p2.product_id )

--Option 2

SELECT 
  product_id, 
  year AS first_year, 
  quantity, 
  price 
FROM 
  Sales 
WHERE 
  (product_id, year) IN (
    SELECT 
      product_id, 
      MIN(year) AS year 
    FROM 
      Sales 
    GROUP BY 
      product_id)