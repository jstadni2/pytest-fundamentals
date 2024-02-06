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

## [Optional] Debug Config
* Specify `"purpose": ["debug-test"]` in `.vscode/launch.json` to set a debug config 
* Used when runnning **Test: Debug All Tests**, **Test: Debug Tests in Current File** and **Test: Debug Test at Cursor** commands

For example:
```json
{
  "name": "Python: Debug Tests",
  "type": "python",
  "request": "launch",
  "program": "${file}",
  "purpose": ["debug-test"], 
  "console": "integratedTerminal",
  "justMyCode": true
}
```

* You can learn more about Visual Studio Code's testing integration with Pyton [here](https://code.visualstudio.com/docs/python/testing#_debug-tests)