import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime("%Y-%m")
    transactions['flag_approved'] = transactions.state == 'approved'
    transactions['approved'] = np.where(transactions['state'] == 'approved',transactions['amount'],nan)
    data = transactions.groupby(['month', 'country'])\
    .agg({'state': 'count', 'amount': 'sum', 'flag_approved': 'sum', 'approved': 'sum'})\
    .rename(columns={'state': 'trans_count', 'amount': 'trans_total_amount', 'flag_approved': 'approved_count', 'approved': 'approved_total_amount'}).reset_index()
    return data