-- Write your PostgreSQL query statement below

WITH first_logins AS (
  SELECT
    A.player_id,
    MIN(A.event_date) AS first_login
  FROM
    Activity A
  GROUP BY
    A.player_id
), consec_logins AS (
  SELECT
    COUNT(A.player_id) AS num_logins
  FROM
    first_logins F
    INNER JOIN Activity A ON F.player_id = A.player_id
    AND F.first_login = A.event_date -  '1 day'::interval
)
SELECT
  ROUND(
    ((SELECT C.num_logins FROM consec_logins C)
    / (SELECT COUNT(F.player_id) FROM first_logins F)::FLOAT)::NUMERIC
  , 2) AS fraction