import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values('recordDate', inplace=True)
    weather['temperature_lagged'] = weather['temperature'].shift(1)
    df = weather[weather['temperature'] > weather['temperature_lagged']][['id']]
    return df