import pandas as pd

from .global_var import COL_STATS_KEY
from .global_var import META_KEY


def observe(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError('input of "observe" should be pandas dataframe')

    result = {
        COL_STATS_KEY: {},
        META_KEY: {},
    }

    return result
