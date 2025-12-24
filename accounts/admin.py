from django.contrib import admin
from .models import Credentials

@admin.register(Credentials)
class CredentialsAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'created_at')
    search_fields = ('username',)
