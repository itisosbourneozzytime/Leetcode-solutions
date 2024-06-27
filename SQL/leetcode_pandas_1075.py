import pandas as pd


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(project, employee, on='employee_id', how='inner')
    return df.groupby('project_id')['experience_years'].mean().reset_index().rename({'experience_years': 'average_years'}, axis=1)
