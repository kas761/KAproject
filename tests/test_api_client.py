import pytest
import requests
import sys
sys.path.insert(1, '/home/karci/KAproject/')
from main import url_base, data_types

@pytest.fixture
def get_response():
    responses = []
    for data_type in data_types:
        url = f"{url_base}{data_type}"
        response = requests.get(url)
        print(response)
        responses.append(response)
    return responses

def test_get_response_status_code(get_response):
    for response in get_response:
        assert response.status_code == 200