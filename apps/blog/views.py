from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
import random
from django.core.cache import cache
from django.conf import settings

from .tasks import mytest_task


class BlogHome(TemplateView):
    template_name = 'blog/index.html'


def set_name(request):
    # import pdb; pdb.set_trace()
    cache.set('name', 'Khondoker Md Mamunur Rashid')
    context = {
        "name": "None"
    }
    return render(request, 'blog/index.html', context)

def set_name(request):
    # import pdb; pdb.set_trace()
    name = cache.get('name')
    context = {
        "name": name
    }
    return render(request, 'blog/index.html', context)


def clear_cache(request):
    # import pdb; pdb.set_trace()
    cache.clear()
    context = {
        "name": "None"
    }
    return render(request, 'blog/index.html', context)


def my_task(request):
    # import pdb; pdb.set_trace()
    mylist = [random.randint(1, 100) for i in range(10)]
    result = mytest_task.delay(mylist)
    
    messages.success(request, "Profile details updated.")
    return render(request, 'blog/index.html')
