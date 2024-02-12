# Part 4: Visual Studio Code Test Explorer Integration
* To run test suites using the GUI, set the config below in `.vscode/settings.json`:
```json
{
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```