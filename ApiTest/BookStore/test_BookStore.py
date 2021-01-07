
import requests
import numpy as np


def post_BookStore_v1_Books(isbnNumber):
    "add a book to a users collection"
    url = "https://demoqa.com/BookStore/v1/Books"
    authHeaders = \
        {
            'accept': 'application/json',
            'authorization': 'Basic ZGVhbjE6UGFzc3dvcmQqMQ==',
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImRlYW4iLCJwYXNzd29yZCI6IlBhc3N3b3JkKjEiLCJpYXQiOjE2MDk4ODU0NTV9.mr8NilRdyseANkK5t27U-PszxNh15B5rU1WvY6xiJm0',
            'Content-Type': 'application/json',
        }

    bookData =   '{ "userId": "9c71d7ac-a527-4e11-9e06-932d710b84f6", "collectionOfIsbns": [ { "isbn": "' + isbnNumber + '"} ]}'
    print(bookData)
    response = requests.post(url, headers=authHeaders, data=bookData)
    print(response.content)
    assert (response.status_code == 201)


def test_add_a_few_books():  #add these books to users collection
    isbnNumberArray = np.array(["9781449325862", "9781449331818", "9781449337711", "9781449365035", "9781491904244"])
    for i in isbnNumberArray:
        post_BookStore_v1_Books(i)

def test_delete_BookStore_v1_Book():
    "delete a book"
    url = "https://demoqa.com/BookStore/v1/Books?UserId=9c71d7ac-a527-4e11-9e06-932d710b84f6"

    authHeaders = \
    {
        'accept': 'application/json',
        'authorization': 'Basic ZGVhbjE6UGFzc3dvcmQqMQ==',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImRlYW4iLCJwYXNzd29yZCI6IlBhc3N3b3JkKjEiLCJpYXQiOjE2MDk4ODU0NTV9.mr8NilRdyseANkK5t27U-PszxNh15B5rU1WvY6xiJm0',
        'Content-Type': 'application/json',
    }



    response = requests.delete(url, headers = authHeaders )
    print(response.content)
    assert (response.status_code == 204)



# def test_put_BookStore_v1_Books_replace():
#     "replace a book"
#     url = "https://demoqa.com/BookStore/v1/Books/9781593277574"
#     authHeaders = \
#         {
#             'accept': 'application/json',
#             'authorization': 'Basic ZGVhbjE6UGFzc3dvcmQqMQ==',
#             'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImRlYW4iLCJwYXNzd29yZCI6IlBhc3N3b3JkKjEiLCJpYXQiOjE2MDk4ODU0NTV9.mr8NilRdyseANkK5t27U-PszxNh15B5rU1WvY6xiJm0',
#             'Content-Type': 'application/json',
#         }
#
#     bookData = '{"userId": "9c71d7ac-a527-4e11-9e06-932d710b84f6", "isbn": "9781449325862"}'
#
#     response = requests.put(url, headers=authHeaders, data=bookData)
#     print(response.content)
#     assert (response.status_code == 200)


def test_delete_BookStore_v1_Books():
    "delete all books from user collection"
    url = "https://demoqa.com/BookStore/v1/Books?UserId=9c71d7ac-a527-4e11-9e06-932d710b84f6"

    authHeaders = \
    {
        'accept': 'application/json',
        'authorization': 'Basic ZGVhbjE6UGFzc3dvcmQqMQ==',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImRlYW4iLCJwYXNzd29yZCI6IlBhc3N3b3JkKjEiLCJpYXQiOjE2MDk4ODU0NTV9.mr8NilRdyseANkK5t27U-PszxNh15B5rU1WvY6xiJm0',
        'Content-Type': 'application/json',
    }

    userParams = \
    (
        ('UserId', '9c71d7ac-a527-4e11-9e06-932d710b84f6'),
    )


    response = requests.delete(url, headers=authHeaders, params = userParams)
    print(response.text)
    assert (response.status_code == 204)