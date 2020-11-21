import pandas as pd
import json

## Managing NaN values
# Note: this method is taken from the Time_Series_Forecasting
# Excercise solution in the ML_SageMaker_Studies Lesson
def fill_nan_with_mean(df):
    '''Fills NaN values in a given dataframe with the average values in a column.
        The technique works well for filling missing hourly values
        that will later be averaged into energy stats over a day'''
    
    # filling nan with mean value of any columns
    num_cols = len(list(df.columns.values))
    for col in range(num_cols):
        df.iloc[:,col]=df.iloc[:,col].fillna(df.iloc[:,col].mean())
        
    return df

def series_to_obj(ts, cat=None):
    obj = {"start": str(ts.index[0]), "target": list(ts)}
    if cat is not None:
        obj["cat"] = cat
    return obj

def series_to_jsonline(ts, cat=None):
    return json.dumps(series_to_obj(ts, cat))