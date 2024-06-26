import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(signups, confirmations, on="user_id", how="left")
    df['confirmation_rate'] = df['action'].apply(lambda x: 1 if x == 'confirmed' else 0)
    data = df.groupby(["user_id"])["confirmation_rate"].mean().reset_index().rename(columns={'confirmed': 'confirmation_rate'}).round(2)
    return data