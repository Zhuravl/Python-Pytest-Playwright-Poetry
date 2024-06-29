# Python-Pytest-Playwright-Poetry
The Test Automation Framework example based on the following tools:
 - [Python](https://www.python.org/) (the programming language)
 - [Pytest](https://pytest.org) (the testing framework for Python)
  - [Pytest-HTML](https://pypi.org/project/pytest-html/) (the plugin for reporting in HTML format)
 - [Playwright](https://playwright.dev/) (the test automation framework for web-browsers and API)
 - [Pytest-playwright](https://pypi.org/project/pytest-playwright/) (the Pytest plugin for Playwright)
 - [Poetry](https://python-poetry.org/) (the dependency management, packaging, and virtual environment handling tool)
 - [GitHub](https://github.com/) (the version control system)

## Setup Instructions

### 0: Check Git and Python:

```bash
git -v
python3 -v
```

### 1: Clone the project:

```bash
git clone https://github.com/zhuravl/Python-Pytest-Playwright-Poetry
cd Python-Pytest-Playwright-Poetry
```

### 2: Install Poetry

```bash
pip install poetry
```

### 3: Activate the Virtual Environment:

```bash
poetry shell
```

### 4: Install Dependencies:

```bash
poetry install
```

........

### n: (Before leaving) Deactivate the Current Environment:

```bash
exit
```

## Run tests

See the documentation for more detials - https://docs.pytest.org/en/8.2.x/how-to/usage.html 

### All existing tests:

```bash
pytest
```

### Specifying a specific test method:

```bash
pytest tests/test_mod.py::TestClass::test_method
```

## Create execution report

```bash
add command here
```
