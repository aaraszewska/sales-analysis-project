import pandas as pd
df = pd.read_csv('sales_cleaned.csv')
print(df[['sales_qty', 'sales_amount', 'price_per_unit']].head(10))
print(df[df['sales_amount'] == 0].head())
print(df[df['price_per_unit'] == 0].head())
print((df['sales_amount'] == 0).sum())
print((df['sales_amount'] == 0).mean())