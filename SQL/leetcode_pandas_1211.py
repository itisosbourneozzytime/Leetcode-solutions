import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries.rating/queries.position
    queries['poor_query_percentage'] = (queries.rating < 3) * 100
    data = queries.groupby('query_name')[['quality', 'poor_query_percentage']].mean().round(2).reset_index()
    return data