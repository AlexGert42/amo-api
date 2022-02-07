from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from crm.views import ApiView, auth, AuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', ApiView.as_view()),
    path('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
    path('token-auth/', AuthToken.as_view())
]
