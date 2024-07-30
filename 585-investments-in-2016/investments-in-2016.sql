-- Write your PostgreSQL query statement below

select
    round(sum(tiv_2016)::numeric,2)  "TIV_2016"
from 
    insurance i1
where
    i1.tiv_2015 in (select i2.tiv_2015 from insurance i2 where i1.pid != i2.pid) 
and
    (i1.lat, i1.lon) not in (select lat, lon from insurance i3 where i1.pid != i3.pid)
;