from django.shortcuts import render



def news_list(request):
    return render(request, 'news_list.html')


def news_detail(request):
    return render(request, 'news_detail.html')