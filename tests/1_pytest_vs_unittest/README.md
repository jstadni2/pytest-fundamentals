# Part 1: `pytest` vs `unittest` 
* [`unittest`](https://docs.python.org/3/library/unittest.html) is the unit testing framework included in base Python
* `pytest` is a third party package
  
## Advantages of `pytest`:
### Concise Syntax
* It's easier to read and write pytests
* Uses generic Python asserts

### Command-Line Interface
* CLI output is more informative

To run a unittest:
```
python -m unittest tests/1_pytest_vs_unittest/test_unittest.py
```

To run a pytest:
```
pytest tests/1_pytest_vs_unittest/test_pytest.py
```
* Verbosity can be increased via the flags `-v` or `--verbose`

* Visit the [CLI Reference](https://docs.pytest.org/en/8.0.x/reference/reference.html#command-line-flags) or run `pytest --help` to learn more

### Features
* 1000+ plugins listed on [pytest.org](https://docs.pytest.org/en/8.0.x/reference/plugin_list.html)
* Its test runner can be used to run unittest suites
```
pytest -v tests/1_pytest_vs_unittest/test_unittest.py
```