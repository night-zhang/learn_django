from django.shortcuts import render
import datetime
# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
