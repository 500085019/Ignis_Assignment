from celery import shared_task
from .scraper import CoinMarketCapScraper

@shared_task
def scrape_coin_data(coin):
    scraper = CoinMarketCapScraper(coin)
    data = scraper.get_data()
    return {coin: data}


