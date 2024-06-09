from rest_framework import serializers

class CoinSerializer(serializers.Serializer):
    coin = serializers.CharField(max_length=10)

