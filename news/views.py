from django.shortcuts import render
from .models import News
from .forms import NewsForms
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'brand'
