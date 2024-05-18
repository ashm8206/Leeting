-- Write your PostgreSQL query statement below

    with cte as (
        Select
        d.name as department
        ,e.name as employee
        ,e.salary 
        ,dense_rank() OVER( PARTITION BY d.id ORDER BY salary desc) rank
    from employee e
    join department d
        on e.departmentId = d.id
    )
     select
         department
        ,employee
        ,salary 
     from cte
     where rank <= 3;