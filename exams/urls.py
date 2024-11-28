from django.urls import path
from . import views


urlpatterns = [
    path('exams/list/', views.ExamListView.as_view(), name='exams-list'),
]
