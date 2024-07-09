import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    data = customer.groupby('customer_id')['product_key'].count().reset_index()
    return data.loc[data.product_key == len(product)][['customer_id']]