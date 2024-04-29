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
    

def test_get_mocked(api_client, monkeypatch):
    # Send a request to the API server and store the response
    response = api_client.get()

    # Confirm that the request-response cycle completed successfully
    assert response.ok