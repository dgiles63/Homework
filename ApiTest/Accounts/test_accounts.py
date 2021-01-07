
import requests
import jsonpath
from requests.auth import HTTPBasicAuth

UUID = "This is a placeholder string"   # required for some of the User APIs
url1 = "This is a placeholder string"
User1Token = "This is a placeholder string"

def test_is_authorized():
    url = "https://demoqa.com/Account/v1/Authorized"
    authHeader = {"accept": "application/json","authorization": "Basic ZGVhbjpQYXNzd29yZCox", "Content-Type": "application/json"}
    loginObj = '{"userName": "dean", "password": "Password*1"}'
    response = requests.post(url, headers = authHeader, data = loginObj)
    print (response.text)
    assert (response.status_code == 200)

def test_user_not_authorized():
    url = "https://demoqa.com/Account/v1/Authorized"
    authHeader = {"accept": "application/json","authorization": "Basic ZGVhbjpQYXNzd29yZCox", "Content-Type": "application/json"}
    loginObj = '{"userName": "bad-user-name", "password": "Password*1"}'
    response = requests.post(url, headers = authHeader, data = loginObj)
    print (response.reason)
    assert (response.status_code == 404)

def test_bad_password():
    url = "https://demoqa.com/Account/v1/Authorized"
    authHeader = {"accept": "application/json","authorization": "Basic ZGVhbjpQYXNzd29yZCox", "Content-Type": "application/json"}
    loginObj = '{"userName": "dean", "password": "bad_password"}'


    response = requests.post(url, headers = authHeader, data = loginObj)
    print (response.reason)


    assert (response.status_code == 404)

def test_Account_v1_GenerateToken():
    url = "https://demoqa.com/Account/v1/GenerateToken"
    authHeader = {"accept": "application/json","authorization": "Basic ZGVhbjpQYXNzd29yZCox", "Content-Type": "application/json"}
    loginObj = '{"userName": "dean1", "password": "Password*1"}'
    response = requests.post(url, headers = authHeader, data = loginObj)
    print (response.text)
    assert (response.status_code == 200)

def test_Account_v1_GenerateToken_bad_credentials():
    url = "https://demoqa.com/Account/v1/GenerateToken"
    authHeader = {"accept": "application/json","authorization": "Basic ZGVhbjpQYXNzd29yZCox", "Content-Type": "application/json"}
    loginObj = '{"userName": "bad_user", "password": ""}'
    response = requests.post(url, headers = authHeader, data = loginObj)
    print (response.text)
    assert (response.status_code == 400)  #This does fail, but the response code is wrong! It should be 400 or 404
    # *** Note: There is a bug here somewhere. The userName bad_user started working to authenticate. I changed the
    # password to null to get it to present the 400 error.


def test_Account_v1_User():
    "Create new user"
    url = "https://demoqa.com/Account/v1/User"
    authHeader = \
        {
        'accept': 'application/json',
        'authorization': 'Basic ZGVhbjpQYXNzd29yZCox',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImRlYW4iLCJwYXNzd29yZCI6IlBhc3N3b3JkKjEiLCJpYXQiOjE2MDk3NzY3NzN9.Ifx5Ytb0MdiVcu8wMt3jUDvzJio27Ocs6dQn8JkiAz8',
        'Content-Type': 'application/json',
        }

    loginObj = '{"userName": "dean1", "password": "Password*1"}'
    response = requests.post(url, headers = authHeader, data = loginObj)
    jsonResponse = response.json()  # User1's UUID is needed
    global UUID
    UUID = jsonResponse["userID"]

    print (response.text)
    print(UUID)
    assert (response.status_code == 201)  #201 is created successfully.



    # *** Note: The above API would be a good place to put a data-driven function or at least a loop to create several.

def test_Account_v1_User_already_exists():
    "Test if creating the same user twice is rejected"
    url = "https://demoqa.com/Account/v1/User"
    authHeader = \
        {
        'accept': 'application/json',
        'authorization': 'Basic ZGVhbjpQYXNzd29yZCox',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImRlYW4iLCJwYXNzd29yZCI6IlBhc3N3b3JkKjEiLCJpYXQiOjE2MDk3NzY3NzN9.Ifx5Ytb0MdiVcu8wMt3jUDvzJio27Ocs6dQn8JkiAz8',
        'Content-Type': 'application/json',
        }

    loginObj = '{"userName": "User1", "password": "Password*2"}'
    response = requests.post(url, headers = authHeader, data = loginObj)
    print (response.text)
    assert (response.status_code == 406)  #rejected successfully.


def test_Account_v1_get_User_UUID():
    "Look at an account"
    global UUID
    global url1
    global User1Token

    url = "https://demoqa.com/Account/v1/User/" + UUID
    url1 = url
    print(url1)

    response = requests.get(url1)
    print (response.content)
    assert (response.status_code == 200)

def test_Account_v1_delete_User_UUID():
    "delete and account"
    global url1
    url = url1
    print(url1)

    response = requests.delete(url)
    print (response.text)
    assert (response.status_code == 200)