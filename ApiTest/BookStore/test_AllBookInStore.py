import requests
import numpy as np

def test_get_BookStore_v1_Books():
    "Get all of the books in the store"
    url = "http://demoqa.com/BookStore/v1/Books"

    response = requests.get(url)
    print(response.content)
    assert (response.status_code == 200)


def test_get_BookStore_v1_Book():
    "Get just one book"
    url = "http://demoqa.com/BookStore/v1/Book"

    inputParams = (
        ('ISBN', '9781449325862'),    #9781449325862 is the ISBN number for Git Pocke Guide
    )
    response = requests.get(url, params = inputParams)
    print(response.content)
    assert (response.status_code == 200)


def test_get_BookStore_v1_Book_with_bad_ISDN():
    "try to get a book with a bad ISDN"
    url = "http://demoqa.com/BookStore/v1/Book"
    authHeaders = \
        {
            'accept': 'application/json',
            'authorization': 'Basic ZGVhbjpQYXNzd29yZCox',
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImRlYW4iLCJwYXNzd29yZCI6IlBhc3N3b3JkKjEiLCJpYXQiOjE2MDk3NzY3NzN9.Ifx5Ytb0MdiVcu8wMt3jUDvzJio27Ocs6dQn8JkiAz8',
        }
    inputParams = (
        ('ISBN', '9781449325865'),
    )
    response = requests.get(url, headers=authHeaders, params=inputParams)
    print(response.content)
    assert (response.status_code == 400)  # 400 is for Book is not available in Books Collection

