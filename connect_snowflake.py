# connect_snowflake.py
import snowflake.connector
conn = snowflake.connector.connect(
    user='JiyaMoolya',
    password='JiyaM@',
    account='jiyamoolya433@gmail.com',
    warehouse='COMPUTE_WH',
    database='VISTORA_DB',
    schema='PUBLIC'
)
print("✅ Connected successfully!")
conn.close()
