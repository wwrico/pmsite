from django.conf.urls import include,patterns,url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView


urlpatterns = [# Examples:
               # url(r'^$', 'pmsite.views.home', name='home'),
               # url(r'^blog/', include('blog.urls')),

               url(r'^admin/',include(admin.site.urls)),
               url(r'^go-to-django/$',RedirectView.as_view(url='http://djangoproject.com'),name='go-to-django'),
               url(r'^$','apps.views.home',name='home'),url(r'^account/',include('apps.accounts.urls')),
               url(r'^deptment/',include('apps.deptment.urls')),]


# for development only
# This will only work if DEBUG is True.
if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',(r'^(?i)accounts/',include('apps.accounts.urls')),)