from .models import Exam
from django.views.generic import ListView, DetailView


class ExamListView(ListView):
    model = Exam
    template_name = 'exam_list.html'
    context_object_name = 'exam'


class ExamDetailView(DetailView):
    model = Exam
    template_name = 'exam_detail.html'
    context_object_name = 'exam'
