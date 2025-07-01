## Web Scraper: Data Extractor

This Python-based web scraper uses `Selenium` to extract structured data from a paginated website and export it into an Excel file.
The data extracted is from https://www.coingecko.com/. The scraper gets the cryptocurrency data from the first 5 pages.
To run the code you need to have the Firefox browser. You also need to set up the GeckoDriver for Firefox.
---

## 📌 Features

- Scrapes data across multiple pages
- Parses HTML content using `Selenium`
- Saves extracted data to an Excel file
- Lightweight with minimal dependencies

---

## 🧰 Technologies Used

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://pypi.org/project/openpyxl/)

---

## 🚀 Getting Started
Steps for running the script:
* 
* Install dependencies: pip install -r requirements.txt
* Run the scraper: python main.py