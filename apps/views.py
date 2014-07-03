__author__ = 'rico'
# coding: utf-8
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext,loader

from django.shortcuts import render

#最原始的写法
def index1(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request,{'latest_question_list':latest_question_list,})
	return HttpResponse(template.render(context))


#利用render简单输出
def index(request):
	latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list}
	return render(request,'polls/index.html',context)


def home(request):
	t = loader.get_template('index.html')
	c = RequestContext(request)
	h = t.render(c)

	return HttpResponse(h)