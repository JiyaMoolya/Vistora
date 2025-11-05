# feature_engineering.py
import snowflake.connector, pandas as pd
conn = snowflake.connector.connect(user='YOUR_USER',password='YOUR_PASS',
    account='YOUR_ACCOUNT_ID',warehouse='COMPUTE_WH',
    database='MY_DATABASE',schema='PUBLIC')
cur = conn.cursor()
cur.execute("""
CREATE OR REPLACE VIEW customer_features AS
SELECT customer_id,
       AVG(spend) AS avg_spend,
       MAX(spend) AS max_spend,
       COUNT(order_id) AS order_count
FROM sales_data
GROUP BY customer_id;
""")
cur.execute("SELECT * FROM customer_features;")
df = pd.DataFrame(cur.fetchall(), columns=['customer_id','avg_spend','max_spend','order_count'])
print(df)
conn.close()
