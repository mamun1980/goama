from django.contrib import admin
from .models import NumberQueryLogs


@admin.register(NumberQueryLogs)
class NumberQueryLogsAdmin(admin.ModelAdmin):
    list_display = ['queried_number', 'count', 'created_at', 'last_queried_at']
    ordering = ['-count']
