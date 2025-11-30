import requests
import pandas as pd


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def get_status_code(url):
    """Call API and return status code"""
    response = requests.get(url)
    return response.status_code


def read_csv_file(path):
    """Read CSV and return number of rows"""
    df = pd.read_csv(path)
    return len(df)


if __name__ == "__main__":
    print("Add:", add(5, 3))
    print("Sub:", sub(10, 4))
    print("API Status Code:", get_status_code("https://google.com"))
    print("CSV Rows:", read_csv_file("data.csv"))
