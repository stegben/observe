import pandas as pd


def observe(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError('input of "observe" should be pandas dataframe')
