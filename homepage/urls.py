from django.conf.urls import patterns, url
from homepage import views

urlpatterns = patterns('',
    url(r'^$', views.homepage, name = 'index'),
)
