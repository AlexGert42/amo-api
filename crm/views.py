import json
import requests
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from crm.scripts.getAPI import getAPI




class ApiView(APIView):

    def get(self, request):
        result = getAPI()
        permission_classes = [IsAuthenticated]

        def get(self, request):
            result = getAPI()

            return Response({
                'API': json.loads(result.content.decode('utf-8'))
            })






class TestApi(APIView):
   pass


def auth(request):
    return render(request, 'auth.html')
