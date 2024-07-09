import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    return followers.groupby('user_id')['follower_id'].count().reset_index().rename(columns={'follower_id': 'followers_count'}).sort_values(by = 'user_id', ascending = True)