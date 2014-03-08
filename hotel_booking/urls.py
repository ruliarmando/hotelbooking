from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from frontend import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search_hotel, name='hotel'),
    url(r'^admin/', include(admin.site.urls)),
)