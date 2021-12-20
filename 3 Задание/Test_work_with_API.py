import requests
import pytest
from main import *


@pytest.fixture
def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )
    return response.ok


@pytest.fixture
def get_api_key(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def get_pet_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def create_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('monkey.jpg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def post_photo(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('dog.jpg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def delete(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        return True


@pytest.fixture
def put_pet():
    response = requests.put(put_info_link,
                            params=put_info_params,
                            headers=put_info_headers
                            )
    return response.ok


@pytest.mark.parametrize('link, params, header, expected_result',
                         [  # get_api_key
                             (api_key_link, get_key_params, get_key_headers, True),
                             # get_my_pets_list
                             (my_pets_link, get_params_my_pets, get_headers_my_pets, True)
                         ]
                         )

def test_get(link, params, header, expected_result):
    response = requests.get(link,
                            params=params,
                            headers=header
                            )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [
                             (DELETE_pet_link, delete_pet_params, delete_pet_headers, True)
                         ]
                         )
def test_delete(link, params, header, expected_result):
    response = requests.delete(link,
                               params=params,
                               headers=header
                               )
    assert response.ok == expected_result


def test_put(put_pet):
    assert put_pet == False