import pytest

from demos.identity import valid_illinois_domain
from demos.address import parse_address


@pytest.mark.parametrize(
    "email,expected",
    [
        ('efrank@uillinois.edu', True),
        ('msmith@illinois.edu', True),
        ('djohns2@illinois.edu', True),
        ('rwhite@uic.edu', True),
        ('nfland1@uis.edu', True),
        ('hank.williamson@yahoo.com', False),
        ('c00lguy1337@aol.com', False),
    ]
)
def test_valid_illinois_domain(email, expected):
    assert valid_illinois_domain(email) == expected


@pytest.mark.parametrize(
    "address,expected",
    [
        ('123 Main St, East City, North State, 12345',
         {'address_line_1': '123 Main St',
          'address_line_2': '',
          'city': 'East City',
          'state': 'North State',
          'zipcode': '12345'}
         ),
        ('456 Pine Lane, North Village, East State, 67890',
         {'address_line_1': '456 Pine Lane',
          'address_line_2': '',
          'city': 'North Village',
          'state': 'East State',
          'zipcode': '67890'}
         ),
        ('321 Elm Street, Room 234, East Village, North State, 13579',
         {'address_line_1': '321 Elm Street',
          'address_line_2': 'Room 234',
          'city': 'East Village',
          'state': 'North State',
          'zipcode': '13579'}
         ),
    ]
)
def test_parse_address(address, expected):
    assert parse_address(address) == expected
