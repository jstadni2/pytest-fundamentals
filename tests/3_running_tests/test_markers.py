import pytest

from demos.identity import valid_illinois_domain


def test_valid_domain():
    assert valid_illinois_domain('efrank@illinois.edu')
    assert not valid_illinois_domain('c00lguy1337@aol.com')


@pytest.mark.gui
def test_registration():
    pass  


@pytest.mark.gui
def test_view_my_profile():
    pass
