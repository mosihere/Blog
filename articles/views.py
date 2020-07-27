from django.shortcuts import render
from . import models



# Create your views here.

def articles_list(request):
    # it means save all Article(articles all are object) and save them here
    articles = models.Articles.objects.all().order_by('date') # This date is our date in models.py

    # we have to use path for render --> articles folder and articles_list.html File
    # The third arguement is a dict that let us use our articles in our template(html file)
    return render(request, 'articles/articleslist.html', {'articles':articles})
