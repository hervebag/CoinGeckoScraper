import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from src.coingecko.pages import LandingPage
from src.excel_export_utils import save_dataframe_to_excel, append_dataframe_to_excel

BASE_URL = "https://www.coingecko.com/"

if __name__ == '__main__':
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(BASE_URL)

    page = LandingPage(driver)
    crypto_currencies_on_first_page = page.get_cryptocurrencies_on_first_page()
    number_of_cryptoCurrency_obtained = len(crypto_currencies_on_first_page.available_cryptocurrencies)
    print("Obtained", number_of_cryptoCurrency_obtained, " crypto currency data list on page ", 1)

    # Save to Excel
    file_path = 'output.xlsx'
    df1 = pd.DataFrame([element.currency for element in crypto_currencies_on_first_page.available_cryptocurrencies])
    save_dataframe_to_excel(df1, file_path)

    # Get cryptocurrency data lists from the next 4 pages
    for index in range(4):
        crypto_currencies_on_next_page = page.get_cryptocurrencies_on_next_page()

        # Save to Excel
        df2 = pd.DataFrame([element.currency for element in crypto_currencies_on_next_page.available_cryptocurrencies])
        append_dataframe_to_excel(df2, file_path)

        number_of_cryptoCurrency_obtained = len(crypto_currencies_on_next_page.available_cryptocurrencies)
        print("Obtained", number_of_cryptoCurrency_obtained, " crypto currency data list on page ", index + 2)
        time.sleep(2)

    driver.quit()
