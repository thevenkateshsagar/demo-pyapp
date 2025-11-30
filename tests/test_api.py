import unittest
from main import get_status_code


class TestAPI(unittest.TestCase):

    def test_google_api(self):
        status = get_status_code("https://google.com")
        self.assertEqual(status, 200)  # Google always returns 200


if __name__ == "__main__":
    unittest.main()
