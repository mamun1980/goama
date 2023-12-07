from celery import shared_task
from .models import BlogCount

from django.conf import settings

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def mytest_task(numbers):
    result = sum(numbers)
    # import pdb; pdb.set_trace()
    bc = BlogCount.objects.create(
        count=result
    )
    