import unittest
from main import read_csv_file


class TestPandas(unittest.TestCase):

    def test_csv_rows(self):
        rows = read_csv_file("data.csv")
        self.assertGreater(rows, 0)


if __name__ == "__main__":
    unittest.main()
