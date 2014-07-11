__author__ = 'rico'
# coding: utf-8

from django.contrib import admin
from apps.books.models import *

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)