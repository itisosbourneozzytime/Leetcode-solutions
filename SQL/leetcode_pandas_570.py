import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(employee.groupby(['managerId']).count().reset_index()['managerId'], \
                    employee, left_on='managerId', right_on='id', how='inner')[['name']]
