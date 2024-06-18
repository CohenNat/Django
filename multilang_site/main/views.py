from django.shortcuts import render
from .models import Article
from django.utils.translation import gettext as _

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': _('Blog Articles'),
    }
    return render(request, 'main/article_list.html', context)
