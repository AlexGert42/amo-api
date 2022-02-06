import json
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from crm.scripts.getAPI import getAPI


class ApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        select = request.query_params
        result = getAPI(select['data'])

        return Response({
            'API': json.loads(result.content.decode('utf-8')),
        })


def auth(request):
    return render(request, 'auth.html')
