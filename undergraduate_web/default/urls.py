#coding=utf-8
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.indexPage),
    url(r'^test/$',views.testPage),
    url(r'^sort/$',views.sortM),

]
