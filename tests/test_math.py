import unittest
from main import add, sub


class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_sub(self):
        self.assertEqual(sub(10, 4), 6)


if __name__ == "__main__":
    unittest.main()
