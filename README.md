# Unit-Test Project Template

A clean template configured for Python development and automated testing using VS Code and pytest.

This template is set up with a `pyproject.toml` configuration, allowing developers to install the workspace in editable mode via `pip install -e .`. It also includes customized VS Code launch configurations to easily debug tests by file names or specific function targets directly using F5. Additionally, it automatically generates HTML reports and code coverage dashboards on every run.

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

## Getting Started & Environment Setup

The project packaging and dependencies are already pre-configured in the `pyproject.toml` file. Follow these steps to set up your local virtual environment, install the project in development mode, and run your tests:

### 1. Create a Virtual Environment
Navigate to the project root directory and create a isolated environment named `.venv`:
```bash
python -m venv .venv
```
*(Use `python3` instead of `python` if required by your operating system)*

### 2. Activate the Virtual Environment
Activate the environment based on your operating system:
* **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate.bat
  ```
* **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install the Project in Development Mode
Install the package in editable mode along with its development dependencies (`pytest`) defined in `pyproject.toml`:
```bash
pip install -e .[dev]
```
*(This allows you to change your source code and instantly test or execute the package without re-installing it)*

### 4. Run the Tests
Verify everything is working correctly by triggering `pytest`:
```bash
pytest
```

## IDE Configuration (VS Code)

This template includes predefined workspace settings (located in `.vscode/settings.json`) optimized for pytest. 

If you are using a virtual environment (like `venv` or `poetry`), make sure to select the correct Python Interpreter in VS Code (`Ctrl+Shift+P` / `Cmd+Shift+P` -> **Python: Select Interpreter**) so it can find the correct version of `pytest` installed in your environment.

## Debugging with VS Code (F5 Workflows) (Optional)

This template includes three predefined debugging profiles inside `.vscode/launch.json`. To use them, open the **Run and Debug** tab in VS Code (`Ctrl+Shift+D` / `Cmd+Shift+D`), select your desired configuration from the dropdown, and press **F5**.

### 1. Execute All Tests
Runs the entire automated test suite across your whole project while remaining attached to the debugger.
* **How to use:** Select `Pytest: Run All Tests` and press **F5**.
* **Best for:** Verifying total project stability after major code changes.

### 2. Execute by File Names
Targets single or multiple specific test files, isolating them from the rest of your suite.
* **How to use:** Select `Pytest: Run by File Names` and press **F5**. 
* **Input format:** Enter relative paths to your files separated by spaces in the top prompt bar.
  ```text
  tests/test_core.py tests/test_advanced.py
  ```
* **Best for:** Speeding up execution when you are only modifying isolated modules.

### 3. Execute by Test Function Names
Runs specific test methods without needing to type out full file system paths. This relies on `pytest`'s custom filtering parameters.
* **How to use:** Select `Pytest: Run by Test Function Names` and press **F5**.
* **Input options:**
  * **Option A (Keyword Search):** Type a specific test name token (e.g., `test_add`). Pytest will scan your suite and selectively execute any test containing that string.
  * **Option B (Exact Target):** Paste an explicit function path pointing directly to a specific unit test file using double-colons:
    ```text
    tests/test_core.py::test_add
    ```
* **Best for:** Deep-diving into a single failing unit test or stepping through code lines chronologically.
