-- Write your PostgreSQL query statement below

Select
    ma.name
from employee em
join employee ma
    on em.managerId = ma.id
group by ma.id, ma.name
HAVING COUNT(em.id) >=5 ;
