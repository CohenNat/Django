from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.utils.translation import gettext as _

def article_list(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'main/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'main/article_detail.html', {'article': article})

def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)