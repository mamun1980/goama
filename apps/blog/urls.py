from django.urls import path
from .views import BlogHome, my_task


urlpatterns = [
    path('', BlogHome.as_view(), name='blog-home'),
    path('call/', my_task, name='blog-call')
]