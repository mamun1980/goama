from rest_framework import serializers
from .models import NumberQueryLogs


class PopularQueriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberQueryLogs
        fields = ['queried_number', 'count']