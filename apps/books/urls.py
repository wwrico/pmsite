__author__ = 'rico'
# coding: utf-8

from django.conf.urls import url
from views import *

urlpatterns = [url(r'^list/$',PublisherList.as_view()),
               url(r'^authors/(?P<pk>[0-9]+)/$',AuthorDetailView.as_view(),name='author-detail'),]