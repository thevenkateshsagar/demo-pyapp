import unittest
from main import add, sub


class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(5, 10), -5)


if __name__ == "__main__":
    unittest.main()
