from django.shortcuts import render
from exams.models import Exam
from news.models import News


def home(request):
    exams = Exam.objects.order_by('-date_publication')[:2]
    news = News.objects.order_by('-date_publication')[:2]
    news_card = News.objects.all()

    context = {
        'exams': exams,
        'news': news,
        'news_card': news_card
    }
    return render(request, 'home.html', context)
