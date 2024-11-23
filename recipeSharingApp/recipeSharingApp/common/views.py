from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class HomeView(TemplateView):
    template_name = 'common/home-page.html'
