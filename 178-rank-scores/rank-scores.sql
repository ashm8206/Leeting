-- Write your PostgreSQL query statement below

    select
        score
        ,DENSE_RANK() OVER(ORDER BY SCORE DESC) rank
    from scores
    order by score desc;
