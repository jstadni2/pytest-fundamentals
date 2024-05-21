# Part 8: Mocking APIs
What is a mock?

Why mock an external API?
- Create isolated tests for how your code handles various responses expected from the external API
- You can still run your test suites when the external API is down
- Avoid costs if the external API charges per use
- Test suite functionality is isolated from external data
- Can perform internal integration tests


There are two methods of mocking with Pytest fixtures:
  1. monkeypatch: fixture included with base pytest
  2. pytest-mock: pytest plugin that provides a thin-wrapper around the [`mock package`]()


## `monkeypatch`
Mock an external API

```
pytest tests/8_mocking/test_monkeypatch.py -k "not api"
```

### Context manager implementation


## `pytest-mock`
- `mock` is included in the Python standard libary as `unittest.mock`
- [Mock.assert_called... methods](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called)
- [unittest.mock.PropertyMock](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock)


# Other Python packages for common use cases of mocking
- [Responses: mocking the Python Requests library](https://github.com/getsentry/responses)
- [kevin1024/vcrpy: Automatically mock your HTTP interactions to simplify and speed up testing](https://github.com/kevin1024/vcrpy)
- [FreezeGun: mocking the datetime module](https://github.com/spulec/freezegun)


# REFERENCE

[auto-speccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing)
