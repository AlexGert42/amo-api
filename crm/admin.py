from django.contrib import admin
from .models import ApiAmoIntegration

class ApiAmoIntegrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"title": ("title",)}

admin.site.register(ApiAmoIntegration, ApiAmoIntegrationAdmin)
