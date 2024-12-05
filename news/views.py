from .models import News
from django.views.generic import ListView, DetailView


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 3


    def get_queryset(self):
        queryset = News.objects.all()

        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(title_icontains=search_query)
        
        order_by = self.request.GET.get('order_by', 'recent')
        if order_by == 'old':
            queryset = queryset.order_by('date_publication')
        else:
            queryset = queryset.order_by('-date_publication')

        return queryset


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'
