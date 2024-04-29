# Part 8: Mocking APIs
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