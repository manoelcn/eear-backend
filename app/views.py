from django.core.paginator import Paginator
from django.shortcuts import render
from exams.models import Exam
from news.models import News

def home(request):
    exams = Exam.objects.order_by('-date_publication')[:2]
    news = News.objects.order_by('-date_publication')[:2]

    # Adicionando paginação para news_card
    news_card_list = News.objects.all()
    paginator = Paginator(news_card_list, 3)  # 3 itens por página
    page_number = request.GET.get('page')  # Captura o número da página atual
    news_card = paginator.get_page(page_number)  # Obtém a página atual

    context = {
        'exams': exams,
        'news': news,
        'news_card': news_card,  # Passa apenas a página atual
    }
    return render(request, 'home.html', context)
