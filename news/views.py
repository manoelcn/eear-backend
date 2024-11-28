from .models import News
from django.views.generic import ListView, DetailView


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'brand'
