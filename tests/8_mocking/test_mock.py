import pytest
import requests
from unittest.mock import PropertyMock

from demos.api_lib import APIClient 


# Custom class to be the mock return values of APIClient
class MockResponse:
    def __init__(self, status_code):
        """Initialize MockResponse with a given status code.

        Args:
            status_code (int): 200, 202, 400, 401, 404, 500, etc.
        """
        self.status_code = status_code
    
    def ok(self):
        if self.status_code < 400:
            return True
        else:
            return False
    
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


@pytest.fixture
def mock_requests(mocker):
    def mock_get(*args, **kwargs):
        """requests.get() mocked to return {'mock_key':'mock_response'}."""
        return MockResponse(200)

    def mock_post(*args, **kwargs):
        return MockResponse(202)

    # pytest-mock has a very similar interface to monkeypatch
    mocker.patch("requests.get", mock_get)
    mocker.patch("requests.post", mock_post)
    

def test_get_mocked(mock_requests):
    # Send a request to the API server and store the response
    api_client = APIClient()
    response = api_client.get()

    # Confirm that the request-response cycle completed successfully
    assert response.ok()
    assert response.json() == {"mock_key": "mock_response"}
    

def test_post_mocked(mock_requests):
    # Send a request to the API server and store the response
    api_client = APIClient()
    response = api_client.post({'key': 'value'})

    # Confirm that the request-response cycle completed successfully
    assert response.status_code == 202
    # What if we want requests.Response?
    assert isinstance(response, MockResponse)


def test_autospec_response(mocker):
    """Use requests.Response spec for mock_response instead of MockResponse.
    """
    mock_response = mocker.create_autospec(spec=requests.Response)
    mock_response.status_code = 202
    mock_response.json.return_value = {"mock_key": "mock_response"}
    mocker.patch('requests.post', return_value=mock_response)
    
    api_client = APIClient()
    response = api_client.post({'key': 'value'})

    # Confirm that the request-response cycle completed successfully
    assert isinstance(response, requests.Response)
    assert response.status_code == 202
    assert response.json() == {"mock_key": "mock_response"}

    # unittest.mock.Mock comes with its own methods for tracking usage
    mock_response.json.assert_called()
    assert mock_response.json.call_count == 1


# Example with uncaught spelling error
def test_mock_mispelled_attribute(mocker):
    # Create a mock response object
    mock_response = mocker.Mock(spec=requests.Response)
    
    # Whoops, misspelled attribute!
    mock_response.status_cod = 200
    
    # Patch requests.get() to return the mock response
    mocker.patch('requests.get', return_value=mock_response)
    
    api_client = APIClient()
    response = api_client.get()
    
    # Should this fail?
    assert response.status_cod == 200


# spec_set argument helps ensure the mock matches the API of the original class
def test_mock_mispelled_attribute_spec_set(mocker):
    # Attempting to set attributes that don’t exist on the spec object
    # will raise an AttributeError.
    mock_response = mocker.Mock(spec=requests.Response, spec_set=True)
    
    # Whoops, misspelled attribute!
    mock_response.status_cod = 200
    
    mocker.patch('requests.get', return_value=mock_response)
    
    api_client = APIClient()
    response = api_client.get()
    
    # NOW this fails
    assert response.status_cod == 200


def test_strict_autospec(mocker):
    mock_response = mocker.create_autospec(requests.Response, spec_set=True)
    # Properties must be attached to the mock type object
    type(mock_response).status_code = PropertyMock(return_value=202)
    # Set the return value of Response.json()
    mock_response.json.return_value = {"mock_key": "mock_response"}

    mocker.patch('requests.post', return_value=mock_response)
    
    api_client = APIClient()
    response = api_client.post({'key': 'value'})

    # Confirm that the request-response cycle completed successfully
    assert isinstance(response, requests.Response)
    assert response.status_code == 202
    assert response.json() == {"mock_key": "mock_response"}
