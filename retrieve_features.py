# retrieve_features.py
import snowflake.connector, pandas as pd
conn = snowflake.connector.connect(user='YOUR_USER',password='YOUR_PASS',
    account='YOUR_ACCOUNT_ID',warehouse='COMPUTE_WH',
    database='MY_DATABASE',schema='PUBLIC')
cur = conn.cursor()
cur.execute("SELECT * FROM feature_store;")
df = pd.DataFrame(cur.fetchall(), columns=['customer_id','avg_spend','max_spend','order_count'])
print("✅ Retrieved features:")
print(df)
conn.close()
