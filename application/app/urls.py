from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^panel/$', login_required(panel),name="panel"),
    url(r'^panel/muestra$', login_required(muestra_1),name="muestra_1"),
    url(r'^panel/muestra_2$', login_required(muestra_2),name="muestra_2"),


]
