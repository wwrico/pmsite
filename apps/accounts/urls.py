#coding=utf-8

from django.conf.urls import patterns,url
from django.contrib.auth.views import login,logout

urlpatterns = patterns('',url(r'^login/$',login,{'template_name':'accounts/login.html'},name='login'),
                       url(r'^logout/$',logout,{'template_name':'accounts/logout.html'},name='logout'),
                       url(r'^logout2/$','apps.accounts.views.auth_logout',name='auth_logout'),
                       url(r'^welcome/$','apps.accounts.views.welcome',name='welcome'),)
