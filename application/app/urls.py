from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^panel/$', login_required(panel),name="panel"),

]
