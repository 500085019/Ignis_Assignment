# scraper/utils.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class CoinMarketCapScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def get_coin_data(self, coin):
        url = f"https://coinmarketcap.com/currencies/{coin}/"
        self.driver.get(url)
        time.sleep(5)  # Let the page load

        data = {}
        try:
            data['price'] = self.driver.find_element(By.CSS_SELECTOR, '.priceValue').text
            data['price_change'] = self.driver.find_element(By.CSS_SELECTOR, '.sc-15yy2pl-0 .sc-1v2ivon-0').text
            data['market_cap'] = self.driver.find_element(By.CSS_SELECTOR, '[data-currency-market-cap]').text
            data['market_cap_rank'] = self.driver.find_element(By.CSS_SELECTOR, '.namePill.primaryPill').text.split('#')[1]
            data['volume'] = self.driver.find_element(By.CSS_SELECTOR, '[data-currency-volume]').text
            data['volume_rank'] = self.driver.find_element(By.CSS_SELECTOR, '[data-currency-volume-rank]').text.split('#')[1]
            data['volume_change'] = self.driver.find_element(By.CSS_SELECTOR, '[data-currency-volume-change]').text
            data['circulating_supply'] = self.driver.find_element(By.CSS_SELECTOR, '[data-currency-supply]').text
            data['total_supply'] = self.driver.find_element(By.CSS_SELECTOR, '[data-currency-max-supply]').text
            data['diluted_market_cap'] = self.driver.find_element(By.CSS_SELECTOR, '[data-currency-diluted-market-cap]').text
            # Scrape contracts, official_links, and socials if present
            data['contracts'] = [{'name': 'solana', 'address': 'example_address'}]  # Dummy example
            data['official_links'] = [{'name': 'website', 'link': 'example_link'}]  # Dummy example
            data['socials'] = [{'name': 'twitter', 'url': 'example_url'}]  # Dummy example
        except Exception as e:
            data['error'] = str(e)

        return data

    def close(self):
        self.driver.quit()
