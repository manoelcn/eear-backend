from django.shortcuts import render
from exams.models import Exam
from news.models import News


def home(request):
    exams = Exam.objects.all()
    news = News.objects.all()

    context = {
        'exams': exams,
        'news': news
    }
    return render(request, 'home.html', context)
