from django.urls import path
from .views import BlogHome, my_task


urlpatterns = [
    path('', BlogHome.as_view(), name='blog-home'),
    path('call/', my_task, name='blog-call'),
    path('set-name/', my_task, name='set-name'),
    path('get-name/', my_task, name='get-name'),
    path('clear-cache/', my_task, name='clear-cache')
]