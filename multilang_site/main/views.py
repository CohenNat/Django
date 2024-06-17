from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'main/article_list.html', {'articles': articles})
