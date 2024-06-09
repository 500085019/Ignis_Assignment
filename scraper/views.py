from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
from .tasks import scrape_coin_data

class StartScraping(APIView):
    def post(self, request):
        coins = request.data.get('coins', [])
        job = []
        for coin in coins:
            result = scrape_coin_data.delay(coin)
            job.append(result.id)
        return Response({'job_id': job}, status=status.HTTP_202_ACCEPTED)

class ScrapingStatus(APIView):
    def get(self, request, job_id):
        result = AsyncResult(job_id)
        if result.state == 'SUCCESS':
            return Response(result.result, status=status.HTTP_200_OK)
        else:
            return Response({'status': result.state}, status=status.HTTP_200_OK)

