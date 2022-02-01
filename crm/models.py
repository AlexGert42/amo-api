from amocrm.v2 import Lead
from django.db import models

class ApiLeads(models.Model):

    class Meta:
        verbose_name = 'Комментарий'

    title = models.CharField(max_length=255)