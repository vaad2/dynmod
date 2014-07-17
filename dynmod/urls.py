from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dynmod.views.home', name='home'),
    url(r'', include('frontend.urls', namespace='frontend')),

    url(r'^admin/', include(admin.site.urls)),
)
