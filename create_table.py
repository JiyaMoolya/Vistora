# create_table.py
import snowflake.connector
conn = snowflake.connector.connect(user='YOUR_USER',password='YOUR_PASS',
    account='YOUR_ACCOUNT_ID',warehouse='COMPUTE_WH',
    database='MY_DATABASE',schema='PUBLIC')
cur = conn.cursor()
cur.execute("""
CREATE OR REPLACE TABLE sales_data(
 customer_id INT, order_id INT, order_date DATE, spend FLOAT);
""")
cur.execute("""
INSERT INTO sales_data VALUES
(1,1001,'2025-01-05',200.5),
(1,1002,'2025-02-10',150.0),
(2,1003,'2025-02-15',400.0),
(2,1004,'2025-03-05',220.0),
(3,1005,'2025-03-20',180.0);
""")
print("✅ Table and data created!")
conn.close()
