import unittest
from main import add_num, sub_num


class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add_num(10, 5), 15)
        self.assertEqual(add_num(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub_num(10, 5), 5)
        self.assertEqual(sub_num(5, 10), -5)


if __name__ == "__main__":
    unittest.main()
