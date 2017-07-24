# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^get_popular_themes/$', views.PopularThemesView.as_view(),
        name='get_popular_themes'),
]
