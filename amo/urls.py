
from django.contrib import admin
from django.urls import path

from crm.views import ApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', ApiView.as_view())
]
