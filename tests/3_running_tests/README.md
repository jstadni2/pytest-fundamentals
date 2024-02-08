# Part 3: How to Run a Test
Run tests in a module:
```
pytest tests/2_creating_tests/test_math_operations.py
```

Run tests in a directory:
```
pytest tests/1_pytest_vs_unittest
```

Run tests by keyword expressions:
```
pytest -k "TestAddNumbers and not negative"
```

Run tests by node ids (test function):
```
pytest tests/2_creating_tests/test_math_operations.py::test_add_numbers
```
For test class method:
```
pytest tests/2_creating_tests/test_math_operations.py::TestAddNumbers::test_positive_integers
```

## Test Discovery
* If directories, file names, or test function/class names aren't specified, collection starts from current directory
* Recurse into directories, search for `test_*.py` or `*_test.py` files
* Collect `test` prefixed functions or methods inside `Test` prefixed test classes
* Test discovery can be [customized](https://docs.pytest.org/en/7.4.x/example/pythoncollection.html)
* Test files might need unique names, otherwise could produce test discovery error (depending on the [import mode](https://docs.pytest.org/en/7.4.x/explanation/goodpractices.html#choosing-an-import-mode))

## Custom Markers
* [Custom markers](https://docs.pytest.org/en/7.4.x/example/markers.html) can be used to run/skip tests that are slow or rely on external resources

Only run tests marked with `gui`:
```
pytest -v -m gui
```
Skip tests marked `gui`:
```
pytest -v -m "not gui"
```
* Markers are registered in `pytest.ini`

Display existing markers:
```
pytest --markers
```