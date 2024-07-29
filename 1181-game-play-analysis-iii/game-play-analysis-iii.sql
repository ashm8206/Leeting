# Write your MySQL query statement below

Select
    player_id,
    event_date,
    SUM(games_played) OVER (partition by player_id order by event_date asc) games_played_so_far
from activity;
