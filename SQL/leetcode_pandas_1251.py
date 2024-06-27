import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(prices, units_sold, on = 'product_id', how = 'left')
    df = df[(df['start_date'] <= df['purchase_date']) & (df['end_date'] >= df['purchase_date'])]
    df['revenue'] =  df['price'] * df['units']
    revenue = df.groupby(['product_id'])['revenue'].sum().reset_index()
    units = df.groupby(['product_id'])['units'].sum().reset_index()
    merged_df = pd.merge(revenue, units, on = 'product_id', how = 'inner')
    merged_df['average_price'] = round(merged_df['revenue'] / merged_df['units'] , 2)
    return merged_df[['product_id', 'average_price']]

def average_selling_price_laconiccally(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(prices, units_sold, on = 'product_id', how = 'left')
    df = df[(df['start_date'] <= df['purchase_date']) & (df['end_date'] >= df['purchase_date'])]
    df['total_revenue'] = df.units * df.price
    df = df.groupby('product_id').agg(total_revenue=('total_revenue', 'sum'), total_units_sold=('units', 'sum')).reset_index()
    df['average_price'] = np.where(df.total_units_sold != 0, round(df.total_revenue/df.total_units_sold,2), 0)
    return df[['product_id', 'average_price']]
