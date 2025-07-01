from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

"""
base classes that all your page and element classes will inherit from.
"""

MAX_WAIT_SECONDS = 10.0
DEFAULT_WINDOW_SIZE = (1300, 2300)

class WebPage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._driver.set_window_size(*DEFAULT_WINDOW_SIZE)
        self._driver.implicitly_wait(5)
        self._wait = WebDriverWait(driver, MAX_WAIT_SECONDS)
    
class WebComponent(WebPage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
