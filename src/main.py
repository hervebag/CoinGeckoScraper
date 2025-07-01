import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from src.coingecko.pages import LandingPage

BASE_URL = "https://www.coingecko.com/"

if __name__ == '__main__':
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(BASE_URL)

    page = LandingPage(driver)
    Crypto_currencies_on_first_page = page.get_cryptocurrencies_on_first_page()
    number_of_cryptoCurrency_obtained = len(Crypto_currencies_on_first_page.available_cryptocurrencies)
    print("Obtained", number_of_cryptoCurrency_obtained, " crypto currency data list on page ", 1)

    # Get cryptocurrency data lists from the next 4 pages
    for index in range(4):
        Crypto_currencies_on_next_page = page.get_cryptocurrencies_on_next_page()
        number_of_cryptoCurrency_obtained = len(Crypto_currencies_on_next_page.available_cryptocurrencies)
        print("Obtained", number_of_cryptoCurrency_obtained, " crypto currency data list on page ", index + 2)
        time.sleep(2)

    driver.quit()
