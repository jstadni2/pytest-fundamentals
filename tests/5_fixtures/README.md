# Part 5: Fixtures
* Fixture functions are used to provide test context
* Tests can request multiple fixtures
* Fixtures defined in `conftest.py` can be used by any test in its directory
* [Yield fixtures](https://docs.pytest.org/en/7.4.x/how-to/fixtures.html#yield-fixtures-recommended) are recommended to manage teardown
* Fixtures are:
  * created when first requested by a test
  * destroyed during teardown of the last test based on `scope` (`function` [default], `class`, `session`, etc.)
  * able to request other fixtures