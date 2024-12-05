from .models import Exam
from django.views.generic import ListView


class ExamListView(ListView):
    model = Exam
    template_name = 'exam_list.html'
    context_object_name = 'exam'
    paginate_by = 3

    
    def get_queryset(self):
        queryset = Exam.objects.all()

        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        order_by = self.request.GET.get('order_by', 'recent')
        if order_by == 'old':
            queryset = queryset.order_by('date_publication')
        else:
            queryset = queryset.order_by('-date_publication')

        return queryset