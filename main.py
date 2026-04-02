import mysql.connector
import pandas as pd
## Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="mysql123",  
    database="sales"
)

  ## read the tables into pandas dataframes

df_customers = pd.read_sql("SELECT * FROM customers", conn)
print(df_customers.head())
df_dates = pd.read_sql("SELECT * FROM date", conn)
print(df_dates.head())
df_markets = pd.read_sql("SELECT * FROM markets", conn)
print(df_markets.head())
df_products = pd.read_sql("SELECT * FROM products", conn)
print(df_products.head())   
df_transactions = pd.read_sql("SELECT * FROM transactions", conn)
print(df_transactions.head())


## Merge the dataframes to create a single dataframe for analysis
df = df_transactions.merge(df_customers, on='customer_code', how='left')
df = df.merge(df_products, on='product_code', how='left')
df = df.merge(df_markets, on='market_code', how='left')
df = df.merge(df_dates, on='order_date', how='left')

## Perform basic data exploration
df.shape
df.head()
df.info()
## data cleaning and preprocessing
df['order_date'] = pd.to_datetime(df['order_date'])
df['cy_date'] = pd.to_datetime(df['cy_date'])


print(df['product_type'].isnull().sum())

df['product_type'] = df['product_type'].fillna('Unknown')
