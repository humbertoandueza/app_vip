from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^panel/$', panel,name="panel"),

]
