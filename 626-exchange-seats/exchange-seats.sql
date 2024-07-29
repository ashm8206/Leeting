# Write your MySQL query statement below
SELECT 
     ID,
     IFNULL(CASE WHEN id % 2 != 0 
                 THEN lead(student) over ()  
                 ELSE lag(student) over ()
            END, student
            ) AS student
     FROM seat;