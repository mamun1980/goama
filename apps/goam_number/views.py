from django.shortcuts import render
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from core.utils import Utils


from .models import NumberQueryLogs
from .serializers import PopularQueriesSerializer



class NumberDetailsAPIView(APIView):

    def get(self, request, number, format=None):
        query_number, created = NumberQueryLogs.objects.get_or_create(queried_number=number)
        
        if created:
            query_number.count = 1
        else:
            query_number.count = query_number.count + 1
        
        query_number.save()

        is_prime = cache.get(number)
        if is_prime is None:
            is_prime = Utils.is_prime(number)
            cache.set(number, is_prime)
            

        num_details = {
            "is_prime": is_prime,
            "is_positive": True if number >= 0 else False,
            "is_even": True if number % 2 == 0 else False,
            "factors": Utils.get_factors(number),
            "query_count": query_number.count,
            "last_queried": query_number.last_queried_at,
        }
        return Response(num_details)



class PopularQueriesListAPIView(generics.ListAPIView):
    serializer_class = PopularQueriesSerializer

    def get_queryset(self):
        qs = NumberQueryLogs.objects.all().order_by('-count')[:5]
        return qs

