import pytest

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
def mock_client(mocker):
    def mock_get(*args, **kwargs):
        """APIClient.get() mocked to return {'mock_key':'mock_response'}."""
        return MockResponse(200)

    def mock_post(*args, **kwargs):

        return MockResponse(202)

    # pytest-mock has a very similar interface to monkeypatch
    mocker.patch("requests.get", mock_get)
    mocker.patch("requests.post", mock_post)
    

def test_get_mocked(mock_client):
    # Send a request to the API server and store the response
    api_client = APIClient()
    response = api_client.get()

    # Confirm that the request-response cycle completed successfully
    assert response.ok()
    assert response.json() == {"mock_key": "mock_response"}
    

def test_post_mocked(mock_client):
    # Send a request to the API server and store the response
    api_client = APIClient()
    response = api_client.post({'key': 'value'})

    # Confirm that the request-response cycle completed successfully
    assert response.status_code == 202


# TODO: Use MagicMock in this example


