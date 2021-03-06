# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^create/$', views.image_create, name='create'),
	url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.image_detail, name='detail'),
	url(r'^list/$', views.image_list, name='list'),
	url(r'^ranking/$', views.image_ranking, name='image_ranking'),
]