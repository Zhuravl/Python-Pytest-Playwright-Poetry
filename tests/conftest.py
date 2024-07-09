import pytest
import logging
from playwright.sync_api import Playwright, Page, BrowserType

logger = logging.getLogger(__name__)
playwright = None
browser = None
context = None
page = None

def pytest_addoption(parser):
    'Defines the additional parameters for the test execution'

    parser.addoption(
        '--delay', action='store', default=None, help='The action delay value for debugging'
    )

@pytest.fixture
def get_browser(request):
    return request.config.getoption('--browser')

@pytest.fixture
def get_url(request):
    return request.config.getoption('--base-url')

@pytest.fixture
def get_delay(request):
    return request.config.getoption('--delay')

#@pytest.fixture
#def get_scope(request):
    #return request.config.getoption('--scope')

#@pytest.fixture
#def get_threads(request):
    #return request.config.getoption('--threads')

@pytest.fixture
def get_playwright():
    return playwright

@pytest.fixture
def get_browser():
    return browser

@pytest.fixture
def get_context():
    return context

@pytest.fixture
def get_page():
    return page

@pytest.fixture(autouse=True, scope='session')
def config_session():
   logging.basicConfig(filename='test_log.log', level=logging.INFO)
   logger.info("Starting tests execution...")
   yield
   logger.info('The test execution has been finished!')

@pytest.fixture(autouse=True, scope='class')
def config_class(get_playwright, get_browser, get_delay):
    get_playwright = Playwright()
    match get_browser:
        case 'firefox':
            if get_delay != None:
                get_browser = get_playwright.firefox.launch(headless=False, slow_mo=int(get_delay))
            else:
                get_browser = get_playwright.firefox.launch()
        case 'webkit':
            if get_delay != None:
                get_browser = get_playwright.webkit.launch(headless=False, slow_mo=int(get_delay))
            else:
                get_browser = get_playwright.webkit.launch()
        case _:
            if get_delay != None:
                get_browser = get_playwright.chromium.launch(headless=False, slow_mo=int(get_delay))
            else:
                get_browser = get_playwright.chromium.launch()
    yield
    get_browser.close()
    get_playwright.close()

@pytest.fixture(autouse=True, scope='function')
def config_test(get_browser, get_context, get_page):
    get_context = get_browser.new_context(viewport={'width': 1366, 'height': 768})
    get_page = get_context.new_page()
    logger.info('Executing test...')
    yield
    get_context.close()
    logger.info('Test execution has been finished!')
