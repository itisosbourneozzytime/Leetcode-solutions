import pandas as pd

def get_average_time_v1(activity: pd.DataFrame) -> pd.DataFrame:
    reshaped = pd.merge(activity[ activity['activity_type'] == 'start'], activity[ activity['activity_type'] == 'end'], how = 'inner', on = ['machine_id', 'process_id'])
    reshaped['processing_time'] = reshaped['timestamp_y'] - reshaped['timestamp_x']
    avg_processing_time = reshaped.groupby(['machine_id'])['processing_time'].mean().reset_index()
    return avg_processing_time;

def get_average_time_v2(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.pivot(index=['machine_id', 'process_id'], columns = 'activity_type', values = 'timestamp')\
    .groupby("machine_id")\
    .apply(lambda x: (x['end'] - x['start']).mean().round(3))\
    .rename('processing_time')\
    .reset_index()