import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    data = pd.merge(register, users, on = 'user_id', how = 'left')
    length = len(users)
    data = data.groupby(['contest_id'])['user_id'].count().reset_index()
    data['percentage'] = (data['user_id'] * 100 / length).round(2)
    return data[['contest_id', 'percentage']].sort_values(by = ['percentage', 'contest_id'], ascending = [False, True])