from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from src.coingecko.base import WebComponent
from src.coingecko.locators import SingleCryptoCurrencyLocator, LandingPageLocator


class CryptoListElement(WebComponent):

    def __init__(self, driver: WebDriver = None) -> None:
        super().__init__(driver)
        self.available_cryptocurrencies = self._get_cryptocurrencies()

    def _get_cryptocurrencies(self) -> list:
        """Find all currently available cryptocurrencies on the page."""
        self._wait.until(
            self._track_text_loaded,
            message="Timeout waiting for cryptocurrencies text to load",
        )

        all_crypto_currencies_on_page = self._driver.find_elements(*LandingPageLocator.ALL_CRYPTO_CURRENCIES_ON_PAGE)

        # Filter cryptocurrencies that are displayed and have a text.
        return [
            CryptoCurrencyElement(currency, self._driver)
            for currency in all_crypto_currencies_on_page
            if currency.is_displayed() and currency.text.strip()
        ]

    def _track_text_loaded(self, driver: WebDriver):
        """Check if the crypto list text has loaded."""
        return any(
            e.is_displayed() and e.text.strip()
            for e in driver.find_elements(*LandingPageLocator.ALL_CRYPTO_CURRENCIES_ON_PAGE)
        )

class CryptoCurrencyElement(WebComponent):
    """Model a cryptocurrency on the site's landing page."""

    def __init__(self, currency_web_element: WebElement, driver: WebDriver) -> None:
        super().__init__(driver)
        self.currency_web_element = currency_web_element
        self.currency = self._get_crypto_cryptocurrency_data()

    def _get_crypto_cryptocurrency_data(self) -> dict:
        currency_data_columns = self.currency_web_element.find_elements(By.TAG_NAME, "td")

        # Cases where the field does not have a value
        percent_1h = self.extract_value_from_webelement(
            currency_data_columns[5],
            SingleCryptoCurrencyLocator.PERCENT_1h
        )

        percent_24h = self.extract_value_from_webelement(
            currency_data_columns[6],
            SingleCryptoCurrencyLocator.PERCENT_24h
        )

        percent_7d = self.extract_value_from_webelement(
            currency_data_columns[7],
            SingleCryptoCurrencyLocator.PERCENT_7d
        )

        currency_data = {
            "crypto name" : currency_data_columns[2].find_element(*SingleCryptoCurrencyLocator.NAME).text,
            "crypto price" : currency_data_columns[4].find_element(*SingleCryptoCurrencyLocator.PRICE).text,
            "percent 1h" : percent_1h,
            "percent 24h" : percent_24h,
            "percent 7d" : percent_7d,
            "volume 24h" : currency_data_columns[9].find_element(*SingleCryptoCurrencyLocator.VOLUME_24h).text,
            "market cap" : currency_data_columns[10].find_element(*SingleCryptoCurrencyLocator.MARKET_CAP).text,
        }

        return currency_data

    def extract_value_from_webelement(self, field: WebElement, field_locator):
        try:
            value = field.find_element(*field_locator).text
        except NoSuchElementException:
            value = "-"

        return value