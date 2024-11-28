from django.urls import path
from . import views


urlpatterns = [
    path('exams/list/', views.NewsListView.as_view(), name='exams-list'),
    path('exams/<int:pk>/detail', views.NewsDetailView.as_view(), name='exams-detail'),
]
