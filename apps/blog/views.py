from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
import random
from django.conf import settings

from .tasks import mytest_task


class BlogHome(TemplateView):
    template_name = 'blog/index.html'


def my_task(request):
    # import pdb; pdb.set_trace()
    mylist = [random.randint(1, 100) for i in range(10)]
    result = mytest_task.delay(mylist)
    
    messages.success(request, "Profile details updated.")
    return render(request, 'blog/index.html')
