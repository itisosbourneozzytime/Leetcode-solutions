import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    filter_year = sales.groupby(['product_id'])['year'].min().reset_index()
    filter_sales = sales.groupby(['product_id', 'year'])[['quantity', 'price']].sum().reset_index()
    data = pd.merge(filter_sales, filter_year, on = ['product_id', 'year'] , how = 'inner').rename(columns = {'year': 'first_year'})
    return data