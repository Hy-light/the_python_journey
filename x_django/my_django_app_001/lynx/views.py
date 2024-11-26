from django.shortcuts import render
from django.http import HttpResponse

from . models import Article

# Create your views here.

def home(request):
    # return HttpResponse("Hello world!")

    articles = Article.objects.all()

    # create a context whose key we will pass in our html page
    context = {'articles': articles}

    return render(request, 'lynx/index.html', context=context)


def singular_article(request, pk):

    article = Article.objects.get(id=pk)

    context = {'article':article}

    return render(request, 'lynx/article.html', context=context)
