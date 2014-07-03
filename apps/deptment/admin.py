#!/usr/bin/env python
#coding=utf-8

from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from apps.deptment.models import *


class DeptmentAdmin(DjangoMpttAdmin):
	tree_auto_open = 0
	pass


admin.site.register(Deptment,DeptmentAdmin)
#admin.site.register(Deptment, MPTTModelAdmin)
admin.site.register(Employee)
