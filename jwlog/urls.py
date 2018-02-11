from django.conf.urls import patterns, include, url

urlpatterns = patterns('jwlog.views',
                       # Examples:
                       # url(r'^$', 'jumpserver.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^list/$', 'jwlog_list', name='jwlog_list'),
                       url(r'^monitor/$', 'monitor_list', name='monitor_list'),
                       url(r'^monitor_hostory/$', 'monitor_hostory_list', name='monitor_hostory_list'),
                       )