from unittest import TestCase

from ..observe import observe

class TestObserve(TestCase):

    def test_raise_if_not_df(self):
        wrong_df = 12
        with self.assertRaises(TypeError):
            observe(df=wrong_df)
