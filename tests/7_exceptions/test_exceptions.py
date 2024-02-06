import pytest

from demos.identity import valid_illinois_domain


@pytest.mark.parametrize(
    "email",
    [
        ('hank.williamson@yahoo.com'),
        ('c00lguy1337@aol.com'),
    ]
)
def test_valid_illinois_domain_raises(email):
    with pytest.raises(Exception) as e_info:
        valid_illinois_domain(email, raise_exc=True)
    
    assert 'has an invalid domain' in str(e_info.value)


@pytest.mark.parametrize(
    "email",
    [
        ('hank.williamson@yahoo.com'),
        ('c00lguy1337@aol.com'),
    ]
)
def test_valid_illinois_domain_raises_match(email):
    with pytest.raises(Exception, match='has an invalid domain'):
        valid_illinois_domain(email, raise_exc=True)
