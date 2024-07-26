-- Write your PostgreSQL query statement below
SELECT
i.item_category as Category,

SUM(CASE WHEN date_part('dow', CAST(order_date AS TIMESTAMP))= 1 THEN quantity ELSE 0 END) as "Monday",
SUM(CASE WHEN date_part('dow', CAST(order_date AS TIMESTAMP))= 2 THEN quantity ELSE 0 END) as "Tuesday",
SUM(CASE WHEN date_part('dow', CAST(order_date AS TIMESTAMP))= 3 THEN quantity ELSE 0 END) as "Wednesday",
SUM(CASE WHEN date_part('dow', CAST(order_date AS TIMESTAMP))= 4 THEN quantity ELSE 0 END) as "Thursday",
SUM(CASE WHEN date_part('dow', CAST(order_date AS TIMESTAMP))= 5 THEN quantity ELSE 0 END) as "Friday",
SUM(CASE WHEN date_part('dow', CAST(order_date AS TIMESTAMP))= 6 THEN quantity ELSE 0 END) as "Saturday",
SUM(CASE WHEN date_part('dow', CAST(order_date AS TIMESTAMP))= 0 THEN quantity ELSE 0 END) as "Sunday"
FROM items as i
LEFT JOIN orders as o
on i.item_id = o.item_id
group by 1
order by 1