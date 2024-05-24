# Part 8: Mocking APIs
What is a mock?
- An object that mimics its production counterpart in a controlled way

Why mock an external API?
- Create isolated tests for how your code handles various responses expected from the external API
- You can still run your test suites when the external API is down
- Avoid costs if the external API charges usage fees
- Test suite functionality is isolated from external data
- Can perform internal integration tests

There are two methods of mocking with Pytest fixtures.

## `monkeypatch`
- [`monkeypatch`](https://docs.pytest.org/en/latest/how-to/monkeypatch.html) is the mocking fixture included with base pytest
- Provides helper methods for setting/deleting:
  - Attributes
  - Dictionary items
  - Environment variables
- Can also modify `sys.path` for importing and change current working directory

## `pytest-mock`
- [`mock`](https://docs.python.org/3/library/unittest.mock.html) is a more feature-rich module included in the Python standard libary as `unittest.mock`
- The [`pytest-mock`](https://pytest-mock.readthedocs.io/en/latest/) plugin provides a `mocker` fixture as a wrapper for the `mock` package
### Installation
```
pip install pytest-mock
```
### Additional Features
- [Autospeccing](https://docs.python.org/3/library/unittest.mock.html#autospeccing)
- Mock [usage tracking methods](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called)
- Enforce mock parity with `spec_set` argument

## Other Python packages for common mocking use cases 
- [Responses: mocking the Python Requests library](https://github.com/getsentry/responses)
- [vcrpy: Automatically mock your HTTP interactions to simplify and speed up testing](https://github.com/kevin1024/vcrpy)
- [FreezeGun: mocking the datetime module](https://github.com/spulec/freezegun)
