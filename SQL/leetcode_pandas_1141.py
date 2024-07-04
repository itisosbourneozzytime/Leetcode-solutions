import pandas as pd
from pandas.tseries.offsets import DateOffset

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity_filtered = activity[(activity['activity_date'] <= pd.Timestamp('2019-07-27')) & (activity['activity_date']  >  (pd.Timestamp('2019-07-27') - DateOffset(months=1))) ]
    data = activity_filtered.groupby(['activity_date']).nunique().reset_index().rename(columns = {'activity_date': 'day', 'user_id': 'active_users'})
    return data[['day', 'active_users']]