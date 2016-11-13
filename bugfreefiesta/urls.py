"""bugfreefiesta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import task_submit, task_detail, test_detail, pin_test_detail, submission_detail, result_detail, pin_result_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^task/(?P<slug>\w+)/submit/$', task_submit, name="task_submit"),
    url(r'^task/(?P<slug>\w+)/$', task_detail, name="task_detail"),
    url(r'^test/(?P<pk>\d+)/$', test_detail, name="test_detail"),
    url(r'^test/p(?P<pk>\d+)/$', pin_test_detail, name="pin_test_detail"),
    url(r'^submission/(?P<pk>\d+)/$', submission_detail, name="submission_detail"),
    url(r'^result/(?P<pk>\d+)/$', result_detail, name="result_detail"),
    url(r'^result/p(?P<pk>\d+)/$', pin_result_detail, name="pin_result_detail"),
    url(r'^$', task_list, name="task_list"),
]
