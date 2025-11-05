# feature_store.py
import snowflake.connector
conn = snowflake.connector.connect(user='YOUR_USER',password='YOUR_PASS',
    account='YOUR_ACCOUNT_ID',warehouse='COMPUTE_WH',
    database='MY_DATABASE',schema='PUBLIC')
cur = conn.cursor()
cur.execute("CREATE OR REPLACE TABLE feature_store AS SELECT * FROM customer_features;")
print("✅ Features saved in Feature Store table!")
conn.close()
