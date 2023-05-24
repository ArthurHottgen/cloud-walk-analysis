import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# Connect to the SQL database
conn = sqlite3.connect('combined_data.db')  # Replace with your actual database name

# Execute the SQL query and retrieve the results into a pandas DataFrame
query = '''
SELECT time, today, yesterday, avg_last_week, avg_last_month,
       today - avg_last_week AS diff_today_avg_week,
       today - avg_last_month AS diff_today_avg_month
FROM sales_data
ORDER BY time;
'''
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Create the line graph
plt.plot(df['time'], df['diff_today_avg_week'], label='Today vs. Avg Last Week')
plt.plot(df['time'], df['diff_today_avg_month'], label='Today vs. Avg Last Month')
plt.xlabel('Time')
plt.ylabel('Difference in Sales')
plt.title('Anomaly Behavior: Today vs. Averages')
plt.legend()
plt.show()