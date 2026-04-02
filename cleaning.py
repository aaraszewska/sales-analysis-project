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



## Fill missing values in the 'product_type' column with 'Unknown'
df['product_type'] = df['product_type'].fillna('Unknown')
print(df.duplicated().sum())
print(df_transactions.duplicated().sum())
print(df['product_code'].isnull().sum())
print(df['customer_code'].isnull().sum())
print(df['market_code'].isnull().sum())
print(df['order_date'].isnull().sum())
print(df['sales_amount'].isnull().sum())
print(df['sales_qty'].isnull().sum())
nulls = df.isnull().sum().sort_values(ascending=False)
print(nulls[nulls > 0])



df['sales_amount'] = pd.to_numeric(df['sales_amount'], errors='coerce')
df['sales_qty'] = pd.to_numeric(df['sales_qty'], errors='coerce')

df['product_type'] = df['product_type'].fillna('Unknown')

text_cols = df.select_dtypes(include='object').columns
for col in text_cols:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

print("Duplikaty:", df.duplicated().sum())
print("\nBraki danych:")
print(df.isnull().sum().sort_values(ascending=False))

print("\nUjemna sales_amount:", (df['sales_amount'] < 0).sum())
print("Zero lub mniej sales_qty:", (df['sales_qty'] <= 0).sum())

print("\nZakres dat:")
print(df['order_date'].min(), df['order_date'].max())

df = df.drop_duplicates()
print(df.shape)
df = df[df['sales_amount'] >= 0]
df.rename(columns={
    'custmer_name': 'customer_name',
    'markets_name': 'market_name'
}, inplace=True)

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

df['month_name'] = pd.Categorical(df['month_name'], categories=month_order, ordered=True)
df['date_yy_mmm'] = df['date_yy_mmm'].str.strip()
df.sort_values('sales_amount', ascending=False).head(10)
df.reset_index(drop=True, inplace=True)
df['date_yy_mmm'] = df['date_yy_mmm'].str.strip()
df['price_per_unit'] = df['sales_amount'] / df['sales_qty']
df['year_month'] = df['order_date'].dt.to_period('M').astype(str)
df['is_return'] = df['sales_amount'] < 0

## Save the cleaned dataframe to a new CSV file
df.to_csv("sales_cleaned.csv", index=False)

print(df[['sales_qty', 'sales_amount', 'price_per_unit']].head(10))
print(df[df['sales_amount'] == 0].head())
print(df[df['price_per_unit'] == 0].head())
print((df['sales_amount'] == 0).sum())
print((df['sales_amount'] == 0).mean())