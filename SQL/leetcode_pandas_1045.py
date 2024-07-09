import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    pr_len = len(product)
    data = customer.groupby('customer_id')['product_key'].count().reset_index()
    data = data[data['product_key'] == pr_len][['customer_id']]
    return data