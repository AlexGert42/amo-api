from django.contrib import admin
from .models import ApiAmoIntegration, FieldsAllRequest


class ApiAmoIntegrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"title": ("title",)}

admin.site.register(ApiAmoIntegration, ApiAmoIntegrationAdmin)

class FieldsAllRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    list_display_links = ('title', 'url')
    search_fields = ('title', 'url')
    prepopulated_fields = {"title": ("title",)}

admin.site.register(FieldsAllRequest, FieldsAllRequestAdmin)

