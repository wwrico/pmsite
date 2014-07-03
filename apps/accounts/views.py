#!usr/bin/env python
#coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def auth_login(request):
	'''登陆核心方法'''
	ret = False
	username = request.POST.get('username',None)
	password = request.POST.get('password',None)
	user = authenticate(username=username,password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
			ret = True
		else:
			txt = u'用户没有激活'
		#   messages.add_message(request, messages.INFO, _(u'用户没有激活'))
	else:
		txt = "sdafdfas"
	# messages.add_message(request, messages.INFO, _(u'用户不存在'))
	return HttpResponse("you're logged in")


#return render_to_response('accounts/login.html')


def auth_logout(request):
	'''注销视图'''
	logout(request)
	#reverse 利用名字反转解释成URL
	return redirect(reverse('home'))


@login_required
def welcome(request):
	return render_to_response('accounts/welcome.html',locals())
