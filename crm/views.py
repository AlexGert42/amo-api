import json

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from crm.models import ApiAmoIntegration
from crm.scripts.getAPI import getAPI
from crm.serializers import IntegrationSerializer


class ApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        select = request.query_params
        currentIntegration = ApiAmoIntegration.objects.get(title=select['title'])

        result = getAPI(IntegrationSerializer(currentIntegration).data, select['data'])

        return Response({
            select['data']: json.loads(result.content.decode('utf-8'))
        })


def auth(request):
    return render(request, 'auth.html')
