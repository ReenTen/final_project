import requests


def add_pet_to_store():

    global new_pet

    new_pet = {"id": 1, "category": {"id": 1, "name": "dogs"}, "name": "Cake",
               "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}],
               "status": "available"}

    response = requests.post(url='https://petstore.swagger.io/v2/pet', json=new_pet)
    assert response.status_code == 200, 'Error! New pet doesn\'t add to store!'


def check_add_pet_to_store():
    response = requests.get(url='https://petstore.swagger.io/v2/pet/1').json()
    assert response == new_pet, "Error! Data doesn\'t match!"


def delete_pet_from_store():
    response = requests.delete(url='https://petstore.swagger.io/v2/pet/1')
    assert response.status_code == 200, 'Error! You can\'t delete this pet from store!'


def check_delete_pet_from_store():
    response = requests.get(url='https://petstore.swagger.io/v2/pet/1').json()
    assert response['message'] == 'Pet not found', 'Error! Pet doesn\'t delete. Check your request!'


def create_user():

    global new_user

    new_user = {
        "id": 1,
        "username": "tompson7",
        "firstName": "Marshall",
        "lastName": "Tompson",
        "email": "marshalltompson@gmail.com",
        "password": "123456",
        "phone": "+45085625783",
        "userStatus": 1
    }

    response = requests.post(url='https://petstore.swagger.io/v2/user', json=new_user)
    assert response.status_code == 200, 'Error! New user doesn\'t add!'


def check_add_user():
    response = requests.get(url='https://petstore.swagger.io/v2/user/tompson7').json()
    assert response == new_user, 'Error! Data doesn\'t match!'


def change_user_info():

    global new_user_info

    new_user_info = {
        "id": 1,
        "username": "tompson7",
        "firstName": "Daniel",
        "lastName": "Tompson",
        "email": "danieltompson@gmail.com",
        "password": "123456",
        "phone": "+45085625783",
        "userStatus": 1
    }

    response = requests.put(url='https://petstore.swagger.io/v2/user/tompson7', json=new_user_info)
    assert response.status_code == 200, 'Error! New user info doesn\'t add!'


def check_change_user_first_name():
    response = requests.get(url='https://petstore.swagger.io/v2/user/tompson7').json()
    assert response['firstName'] == new_user_info['firstName'], 'Error! User first name doesn\'t change!'
