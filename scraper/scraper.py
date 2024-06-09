import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class CoinMarketCapScraper:
    def __init__(self, coin):
        self.coin = coin
        self.base_url = f"https://coinmarketcap.com/currencies/{coin}/"
        self.data = {}

    def get_page(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(self.base_url)

    def scrape_data(self):
        self.get_page()
        
        try:
            self.data['price'] = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div').text
            self.data['price_change'] = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/span').text
            # Add more fields as necessary
        except Exception as e:
            print(f"Error scraping data for {self.coin}: {e}")

        self.driver.quit()

    def get_data(self):
        self.scrape_data()
        return self.data
