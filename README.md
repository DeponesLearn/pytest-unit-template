# Unit-PyTest Project Template

A clean template configured for Python development and automated testing using VS Code and pytest.

## Environment Requirements

To ensure the automated test discovery and settings function correctly, this template is built and verified using the following environment setup:

* **Python Version:** `3.11.x` (or specify your version, e.g., `>=3.10`)
* **pytest Version:** `8.x.x` (or specify your version, e.g., `>=7.0`)

If you experience issues with test discovery (`python.testing.autoTestDiscoverOnSaveEnabled`), please verify that your local environment matches or is compatible with these versions.

## How to Check Your Local Versions

Before running or troubleshooting the template, you can verify your installed versions by running the following commands in your terminal:

### 1. Check Python Version
```bash
python --version
```
*(Depending on your system setup, you may need to use `python3 --version`)*

### 2. Check pytest Version
```bash
pytest --version
```

## IDE Configuration (VS Code)

This template includes predefined workspace settings (located in `.vscode/settings.json`) optimized for pytest. 

If you are using a virtual environment (like `venv` or `poetry`), make sure to select the correct Python Interpreter in VS Code (`Ctrl+Shift+P` / `Cmd+Shift+P` -> **Python: Select Interpreter**) so it can find the correct version of `pytest` installed in your environment.
