SELECT time, today, yesterday, avg_last_week, avg_last_month,
       today - avg_last_week AS diff_today_avg_week,
       today - avg_last_month AS diff_today_avg_month
FROM (
  SELECT time, today, yesterday, avg_last_week, avg_last_month
  FROM checkout_1
  UNION ALL
  SELECT time, today, yesterday, avg_last_week, avg_last_month
  FROM checkout_2
) AS combined_data
ORDER BY time;