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

### 1: Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2: Clone the project:

```bash
git clone https://github.com/zhuravl/Python-Pytest-Playwright-Poetry
cd Python-Pytest-Playwright-Poetry
```

### 3: Activate the Virtual Environment:

```bash
poetry shell
```

### 4: Install Dependencies:

```bash
poetry install --no-root
```

### 5: Install Playwright Browsers:

```bash
playwright install
```

### 6: Execute Tests:

Launch tests using the following command with parameters:

```bash
poetry run pytest {TEST_SCOPE} --browser {BROWSER_NAME} --base-url {TARGET_URL} --delay {DELAY}
```
Where:
 * TESTS_SCOPE — test name(s) to execute (e.g. 'tests/about_test.py' or 'tests/about_test.py::TestAbout::test_about_page_content'), optional (all tests by default)
 * BROWSER_NAME — target browser name ('chromium' or 'firefox' or 'webkit')
 * TARGET_URL — the target site URL
 * DELAY — define an executing delay in millis (e.g. '1000') to enable the debugging mode and launch the browser in the headed mode, optional ('null' by default)
 * THREAD_COUNT — specify how many threads should be allocated for this execution, optional (the one thread by default)

An example params for launching the example test using Chromium browser and the default params:

```bash
poetry run pytest tests/about_test.py --browser chromium --base-url https://usource.com.ua/
```
See the documentation for more default parameters - https://docs.pytest.org/en/8.2.x/how-to/usage.html 

### 7: See Test Execution Artifacts:

Open the `test_report.html` to see the Test Execution Report. 
Open the `test_log.log` to see the Test Execution Log. 

### n: (Before leaving) Deactivate the Current Environment:

```bash
exit
```
