from django.urls import path
from .views import NumberDetailsAPIView, PopularQueriesListAPIView


urlpatterns = [
    path('number-details/<int:number>/', NumberDetailsAPIView.as_view(), name='number-details'),
    path('popular-queries/', PopularQueriesListAPIView.as_view(), name='popular-queries')
]