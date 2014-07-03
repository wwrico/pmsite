#coding: utf-8

from django.db import models
from mptt.models import MPTTModel,TreeForeignKey

#部门信息
class Deptment(MPTTModel):
	title = models.CharField(u'部门',max_length=50,unique=True)
	parent = TreeForeignKey('self',null=True,blank=True,related_name='children')
	slug = models.SlugField(verbose_name=u'简写',max_length=20,blank=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.__unicode__()

	class Meta:
		verbose_name = u'部门'
		verbose_name_plural = u'部门'


# 员工信息
class Employee(models.Model):
	#id = models.AutoField(primary_key = True)
	name = models.CharField(u'姓名',max_length=20)
	slug = models.SlugField(u'简写',blank=True)
	position = models.CharField(u'职位',max_length=20,blank=True)
	phone1 = models.CharField(u'电话',max_length=40,blank=True)
	deptment = models.ForeignKey(Deptment,verbose_name=u'所属部门')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'员工'
		verbose_name_plural = u'员工'