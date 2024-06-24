import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merge_df = pd.merge(visits, transactions, on = 'visit_id', how = 'left')
    merge_df = merge_df[merge_df['transaction_id'].isna()]
    merge_df = merge_df.groupby(['customer_id'])['visit_id'].count().reset_index()
    merge_df = merge_df.rename({'visit_id': 'count_no_trans'}, axis = 1)
    return merge_df