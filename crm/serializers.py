from django.contrib.auth.models import User
from rest_framework import serializers




class IntegrationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    key_subdomain = serializers.CharField(max_length=255)
    key_client_id = serializers.CharField(max_length=255)
    key_client_secret = serializers.CharField(max_length=255)
    key_redirect_url = serializers.CharField(max_length=255)
    key_code = serializers.CharField(max_length=2000)
    key_link = serializers.CharField(max_length=255)
    class Meta:
        fields = '__all__'
