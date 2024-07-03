import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    data = teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index().rename(columns = {'subject_id': 'cnt'})
    return data