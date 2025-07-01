from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from src.coingecko.base import WebPage
from src.coingecko.elements import CryptoListElement
from src.coingecko.locators import CryptoCurrencyListLocator


class LandingPage(WebPage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def get_cryptocurrencies_on_first_page(self) -> CryptoListElement:
        return CryptoListElement(self._driver)

    def get_cryptocurrencies_on_next_page(self) -> CryptoListElement:
        try:
            # Find the pagination link with aria-label="next"
            next_button = self._wait.until(EC.presence_of_element_located(
                *CryptoCurrencyListLocator.PAGINATION_BUTTON
            ))

            # Scroll into view
            self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)

            # Wait until it's clickable and click
            self._wait.until(EC.element_to_be_clickable(*CryptoCurrencyListLocator.PAGINATION_BUTTON)).click()
            print("Navigated to next page.")
        except Exception as e:
            print("No more pages or an error occurred:", str(e))

        return CryptoListElement(self._driver)
