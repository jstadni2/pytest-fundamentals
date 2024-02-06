# Part 7: Expected Exceptions
* You can assert that an exception is raised via `pytest.raises()`
* `e_info` provides access to the `.type`, `.value` and `.traceback` attributes of the exception
* The `match` keyword parameter to `pytest.raises()` also tests that a regular expression matches on the string representation of an exception
* Alternative forms of asserting exceptions are described in the [pytest documentation](https://docs.pytest.org/en/stable/how-to/assert.html#assertraises)