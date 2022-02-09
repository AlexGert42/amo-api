import json

from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
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

        fields = ['leads', 'contacts', 'leads/pipelines', 'companies', 'tasks', 'events', 'users', 'templates']

        def allResponse(i):
            return {
                i: json.loads(getAPI(IntegrationSerializer(currentIntegration).data, i).content.decode('utf-8'))
            }

        if select['data'] == 'all':
            return Response({
                "all": map(lambda item: allResponse(item), fields)
            })

        result = getAPI(IntegrationSerializer(currentIntegration).data, select['data'])



        return Response({
            select['data']: json.loads(result.content.decode('utf-8'))
        })


class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': f"Token {token.key}"
        })


def auth(request):
    return render(request, 'auth.html')
