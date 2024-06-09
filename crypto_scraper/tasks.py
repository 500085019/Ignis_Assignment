# scraper/tasks.py

from celery import shared_task
from .utils import CoinMarketCapScraper
from celery.result import AsyncResult

@shared_task(bind=True)
def scrape_coin_data(self, coin, job_id):
    scraper = CoinMarketCapScraper()
    data = scraper.get_coin_data(coin)
    scraper.close()
    
    if not self.request.id:
        self.request.id = job_id

    current_result = AsyncResult(self.request.id).result or []
    current_result.append({"coin": coin, "output": data})
    return current_result
