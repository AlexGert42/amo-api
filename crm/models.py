from django.contrib.auth.models import User
from django.db import models

class ApiAmoIntegration(models.Model):
    title = models.CharField(max_length=255)
    key_subdomain = models.CharField(max_length=255)
    key_client_id = models.CharField(max_length=255)
    key_client_secret = models.CharField(max_length=255)
    key_redirect_url = models.CharField(max_length=255)
    key_code = models.TextField(max_length=2000)
    key_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'KeyIntegration'
        verbose_name_plural = 'KeyIntegration'
        ordering = ['pk']







