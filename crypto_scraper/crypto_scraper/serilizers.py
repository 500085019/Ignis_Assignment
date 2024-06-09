# scraper/serializers.py

from rest_framework import serializers

class ScrapingTaskSerializer(serializers.Serializer):
    coin = serializers.CharField(max_length=100)
    output = serializers.JSONField()
