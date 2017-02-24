from unittest import TestCase

import pandas as pd

from ..observe import observe
from ..global_var import COL_STATS_KEY
from ..global_var import META_KEY

class TestObserve(TestCase):

    def test_raise_if_not_df(self):
        wrong_df = 12
        with self.assertRaises(TypeError):
            observe(df=wrong_df)

    def test_contain_correct_key(self):
        data = [1, 10, -1, 5.2, 10000000]
        col = 'column name'
        df = pd.DataFrame({col: data})
        result = observe(df)
        self.assertIn(META_KEY, result)
        self.assertIn(COL_STATS_KEY, result)
