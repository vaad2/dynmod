from django.conf.urls import patterns, include, url
from frontend.views import ViewIndex

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ViewIndex.as_view(), name='ViewIndex'),

)
