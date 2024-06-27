import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema['description'] != 'boring') & (cinema['id'] % 2 == 1)]
    return df.sort_values(by='rating', ascending=False)