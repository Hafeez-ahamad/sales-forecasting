import unittest
import pandas as pd
from src.preprocess import preprocess_data

class TestPreprocess(unittest.TestCase):
    def test_preprocess_data(self):
        data = preprocess_data('../data/sales_data.csv')
        self.assertIsInstance(data, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
