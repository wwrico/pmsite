__author__ = 'rico'
# coding: utf-8

from django.views.generic import ListView, DetailView
from models import Publisher, Book, Author
from django.utils import timezone

class PublisherList(ListView):
	model = Publisher
	#自定义个名称，不然就是object_list
	context_object_name = 'my_favorite_publishers'
	template_name = "books/publisher_list.html"


class PublisherDetail(DetailView):
	context_object_name = 'publisher'
	model = Publisher
	#可以用queryset = Publisher.objects.all()来代替,后者更灵活

	#在context中附加一些book_list列表
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(PublisherDetail, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['book_list'] = Book.objects.all()
		return context

'''
	增加一个功能，最后访问，打开的时间
'''
class AuthorDetailView(DetailView):
	queryset = Author.objects.all()
	context_object_name = 'wwobject'
	#增加一个功能，最后访问，每次打开都要重新保存时间

	def get_object(self):
		# Call the superclass
		object = super(AuthorDetailView, self).get_object()
		# Record the last accessed date
		object.last_accessed = timezone.now()
		object.save()

		# Return the object
		return object