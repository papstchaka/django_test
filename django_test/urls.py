from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^$', views.home, name = 'home'),
    url(r'^subsite/$', views.subsite, name="subsite"),
    url(r'^subsite/(?P<pk>[a-zA-Z]+)/$', views.subsite, name='subsite'),
    url(r'^graph/$', views.graph, name = 'graph'),
    url(r'^graph/(?P<pk>[a-zA-Z]+)/$', views.graph, name = 'graph'),
    url(r'^picture/$', views.picture, name = 'picture'),
    url(r'^picture/(?P<pk>[a-zA-Z]+)/$', views.picture, name = 'picture'),
]
