from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('BuckIt.home.views',
    # Examples:
    # url(r'^$', 'BuckIt.views.home', name='home'),
    # url(r'^BuckIt/', include('BuckIt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'login'),
    url(r'^login/$', 'login'),
    url(r'^home/$', 'home'),
)

urlpatterns += patterns('BuckIt.BuckItList.views',
    url(r'^list/(?P<title>\w+)/$', 'list'),
    )