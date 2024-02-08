# Part 2: Creating Tests
## How to Write a Test
* `assert expression1, expression2`, is equivalent to:
  ```python
  if not expression1: raise AssertionError(expression2)
  ```
* Can group tests in classes, but `pytest` also provides more flexible grouping features
* We'll cover how to write DRY tests using fixtures and parametrized tests

## Testing Directory Structure
Two recommended ways to structure your tests:
1. Tests separate from app code
```
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    test_app.py
    test_view.py
    ...
```
2. Tests as part of app code
```
src/mypkg/
    __init__.py
    app.py
    view.py
    tests/
        __init__.py
        test_app.py
        test_view.py
        ...
```
* Can encounter `ImportError` when importing source modules into test scripts without proper test layout and pythonpath/import config
* More info on test directory structure can be found in [`pytest` documentation](https://docs.pytest.org/en/7.4.x/explanation/goodpractices.html) and [stack overflow](https://stackoverflow.com/a/50610630)