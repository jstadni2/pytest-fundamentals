# Part 8: Mocking APIs
Why mock an external API?
- Create test how your code handles various responses expected from the external API
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


# REFERENCE

[auto-speccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing)
