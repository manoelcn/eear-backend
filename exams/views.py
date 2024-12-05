from .models import Exam
from django.views.generic import ListView


class ExamListView(ListView):
    model = Exam
    template_name = 'exam_list.html'
    context_object_name = 'exam'
    paginate_by = 3