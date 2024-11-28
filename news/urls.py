from django.urls import path
from . import views


urlpatterns = [
    path('news/list/', views.NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/detail', views.NewsDetailView.as_view(), name='new-detail'),
]