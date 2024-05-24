import pytest
import requests

from demos.api_lib import APIClient 


# Calling external APIs can result in flaky tests
# Can exclude them from CI/CD pipeline by marking them
@pytest.mark.externalapi
def test_get():
    """This will fail if the external API is down or access is restricted.
    """
    api_client = APIClient()
    
    # Send a request to the API server and store the response
    response = api_client.get()

    # Confirm that the request-response cycle completed successfully
    assert response.ok


# Custom class to mock return values of APIClient
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
def mock_requests(monkeypatch):
    def mock_get(*args, **kwargs):
        """requests.get() mocked to return {'mock_key':'mock_response'}."""
        return MockResponse(200)

    def mock_post(*args, **kwargs):

        return MockResponse(202)

    monkeypatch.setattr(requests, "get", mock_get)
    monkeypatch.setattr(requests, "post", mock_post)
    

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
