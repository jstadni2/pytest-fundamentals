import pytest

from demos.identity import valid_illinois_domain, register


@pytest.fixture
def john_smith():
    identity = {
        'first_name': 'John',
        'last_name': 'Smith',
        'invalid_email': 'john.smith@aol.com',
        'valid_email': 'jsmith@illinois.edu',
    }
    return identity


def test_valid_domain(john_smith):
    assert valid_illinois_domain(john_smith['valid_email'])
    assert not valid_illinois_domain(john_smith['invalid_email'])


def test_registration(john_smith):
    # Attempt to register with invalid email
    response = register(
        john_smith['first_name'],
        john_smith['last_name'],
        john_smith['invalid_email'])
    assert "registration failed" == response
    
    # Register with valid email
    response = register(
        john_smith['first_name'],
        john_smith['last_name'],
        john_smith['valid_email'])
    assert "registered new user" in response


@pytest.mark.gui
def test_view_my_profile(webdriver, john_smith):
    html = webdriver.login(john_smith)
    expected_welcome = f"Welcome {john_smith['first_name']} {john_smith['last_name']}!"
    assert expected_welcome in html 
