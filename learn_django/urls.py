"""learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app1 import views
from app2 import views as views2

# from app1.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    # # -----------app1-----------
    path('hello/', views.hello),
    # path('hello/', hello),
    path('time/', views.current_datetime),
    path('time2/', views.current_datetime2),
    # path('time/plus/<int:offset>/', views.hours_ahead),
    # django1.7的写法
    re_path('^time/plus/(\d{1,2})/$', views.hours_ahead),
    # -----------app2-----------
    path('hello2/', views2.hello),
]
