# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.views.generic.list import ListView

from django_interview.apps.main.models import Theme


class IndexView(TemplateView):
    template_name = 'main/index.html'


class PopularThemesView(ListView):
    template_name = "main/popular_themes.html"
    context_object_name = 'all_themes'

    def get_queryset(self):
        all_themes = sorted(Theme.objects.all(),
                            key=lambda m: m.theme_score, reverse=True)
        return all_themes
