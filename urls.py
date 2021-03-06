from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'ads.views.default'),
    #(r'^video/(?P<format>\w+)/?', 'jobslist.views.serve_video_list'),
    (r'^video/$', 'ads.views.serve_video_list'),
    (r'^video/(?P<imei>\d+)/(?P<lat>[\d.]+)/(?P<lon>[\d.]+)', 'ads.views.get_video_list'),
    # Examples:
    # url(r'^$', 'icad.views.home', name='home'),
    # url(r'^icad/', include('icad.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
