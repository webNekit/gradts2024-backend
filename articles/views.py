from django.shortcuts import render, get_object_or_404

from articles.models import Article


# Create your views here.
def index(request):
    articles = Article.objects.filter(is_active=True).order_by('-id')
    return render(request, 'articles/index.html', {
        'articles': articles,
        'title': 'Статьи и новости'
    })

def detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_active=True)
    return render(request, 'articles/detail.html', {
        'article': article,
        'title': article.title,
        'meta_title': article.title,
        'meta_description': article.short_text,
        'meta_keywords': article.short_text,
        'meta_image': article.image.url
    })