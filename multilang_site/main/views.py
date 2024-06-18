from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.utils.translation import gettext as _

def article_list(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'main/article_list.html', {'articles': articles})

def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)