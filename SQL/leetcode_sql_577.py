import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    bonus = pd.merge(employee, bonus, how = 'left', on = 'empId')
    return bonus[ (bonus['bonus'] < 1000) | (bonus['bonus'].isna())][['name', 'bonus']]
