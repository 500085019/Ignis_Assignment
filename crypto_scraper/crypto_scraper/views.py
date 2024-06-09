# scraper/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StartScrapingView(APIView):
    def post(self, request, *args, **kwargs):
        # Logic to start the scraping job
        return Response({"message": "Scraping job started"}, status=status.HTTP_200_OK)

class ScrapingStatusView(APIView):
    def get(self, request, job_id, *args, **kwargs):
        # Logic to get the status of the scraping job
        return Response({"message": f"Status of job {job_id}"}, status=status.HTTP_200_OK)
