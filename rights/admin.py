from django.contrib import admin
from .models import License


@admin.register(License)
class RightAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'valid_upto', 'created_at')
