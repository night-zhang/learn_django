from django.shortcuts import render
import datetime
# Create your views here.
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context


def hello(request):
    return HttpResponse("Hello world ! ")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def current_datetime2(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    # 等同于上面的写法
    return render(request, 'current_datetime.html', {'current_date': now})
    # render_to_response不需要传request参数，但是已经弃用了
    # return render_to_response('current_datetime.html', {'current_date': now})
