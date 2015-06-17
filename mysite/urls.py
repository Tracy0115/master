from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	(r'^admin/', include(admin.site.urls)),
	('^hello/$', hello),
	('^stone/$', stone),
	('^time/$', Current_Time),
	('^date/$', Current_DateTime),
	('^url/$', Current_url_path),
	('^date1/$', Current_DateTime1),
	(r'^time/plus/(\d{1,2})/$',hours_ahead),
	('^meta/$', display_meta),
	('^search-form/$',search_form),
	
	
    # url(r'^admin/', include(admin.site.urls)),
)
