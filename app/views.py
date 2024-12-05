from django.core.paginator import Paginator
from django.shortcuts import render
from exams.models import Exam
from news.models import News

def home(request):
    filter_option = request.GET.get('filter', 'recent')

    if filter_option == 'old':
        news_card_list = News.objects.all().order_by('date_publication')
    else:
        news_card_list = News.objects.all().order_by('-date_publication')

    paginator = Paginator(news_card_list, 3)
    page_number = request.GET.get('page')
    news_card = paginator.get_page(page_number)

    exams = Exam.objects.order_by('-date_publication')[:2]
    news = News.objects.order_by('-date_publication')[:2]

    context = {
        'exams': exams,
        'news': news,
        'news_card': news_card,
        'filter_option': filter_option,
    }
    return render(request, 'home.html', context)
