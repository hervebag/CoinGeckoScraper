from selenium.webdriver.common.by import By


"""
Locators are among the most fragile parts of web automation because they tend to change frequently.
To manage this more effectively, it's a good idea to keep them in a separate file.
"""
class LandingPageLocator:
    ALL_CRYPTO_CURRENCIES_ON_PAGE = (By.CSS_SELECTOR, "table tbody tr")

class CryptoCurrencyListLocator:
    ITEM = (By.TAG_NAME, "td")
    PAGINATION_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="next"]') # "Next" button

class SingleCryptoCurrencyLocator:
    NAME = (By.CSS_SELECTOR, "a div div")
    PRICE = (By.TAG_NAME, "span")
    PERCENT_1h = (By.TAG_NAME, "span")
    PERCENT_24h = (By.TAG_NAME, "span")
    PERCENT_7d = (By.TAG_NAME, "span")
    VOLUME_24h = (By.TAG_NAME, "span")
    MARKET_CAP = (By.TAG_NAME, "span")
