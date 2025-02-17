import pytest
import requests
from main.py import url, data_types


@pytest.fixture
def get_response():
    responses = []
    for data_type in data_types:
        responses.append(requests.get(url))
    return responses

def test_get_response_status_code(get_response):
    for response in get_response:
        assert response.status_code == 200