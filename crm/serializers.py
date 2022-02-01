
from amocrm.v2 import Lead
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class ApiSerializer(serializers.Serializer):
    class Meta:
        model = Lead
        fields = '__all__'