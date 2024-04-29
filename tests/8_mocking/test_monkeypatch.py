import pytest

from demos.api_lib import APIClient 


@pytest.fixture
def api_client():
    return APIClient()
    

@pytest.mark.api
def test_get(api_client):
    """This will fail if the external API is down or access is restricted.
    """
    # Send a request to the API server and store the response
    response = api_client.get()

    # Confirm that the request-response cycle completed successfully
    assert response.ok


# TODO: Instantiate with different status codes
# 200, 202, 400, 401, 404, 500
# custom class to be the mock return value of requests.get()
class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code
    
    def ok(self):
        if self.status_code < 400:
            return True
        else:
            return False
    
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


# monkeypatched requests.get moved to a fixture
@pytest.fixture
def mock_client(monkeypatch):
    """APIClient.get() mocked to return {'mock_key':'mock_response'}."""

    def mock_get(*args, **kwargs):
        return MockResponse(200)

    monkeypatch.setattr(APIClient, "get", mock_get)
    

def test_get_mocked(mock_client):
    # Send a request to the API server and store the response
    api_client = APIClient()
    response = api_client.get()

    # Confirm that the request-response cycle completed successfully
    assert response.ok()