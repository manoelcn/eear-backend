from django.urls import path
from . import views


urlpatterns = [
    path('news/list/', views.news_list, name='news-list'),
    path('news/detail/', views.news_detail, name='new-detail'),
]