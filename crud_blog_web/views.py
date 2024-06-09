from django.shortcuts import render
from django.http import HttpResponse
from crud_blog_web.models import Article
from django.core import serializers

def index(request):
    return HttpResponse("Witaj świecie")

def indexArticle(request):
    title = "Lista artykułów"
    articles = Article.objects.all()
    return render(request, 'crud_blog_web/articles.html', {
        "articles": articles,
        "title": title
    })

def indexArticleJson(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type="application/json")