from django.contrib import admin
from .models import Right


@admin.register(Right)
class RightAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'valid_upto', 'created_at')
