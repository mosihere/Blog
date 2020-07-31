from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def articles_list(request):
    # it means save all Article(articles all are object) and save them here
    articles = models.Articles.objects.all().order_by('-date') # This date is our date in models.py

    # we have to use path for render --> articles folder and articles_list.html File
    # The third arguement is a dict that let us use our articles in our template(html file)
    return render(request, 'articles/articleslist.html', {'articles':articles})


# This slug arguement is come from urls.py(articles)
def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Articles.objects.get(slug=slug) # first slug is arguement of func and second is models.py slug

    # we will send and render these articles that we get above and send them to article_detail.html
    return render(request, 'articles/article_detail.html', {'article':article})



# it's a decorator in python and django
@login_required(login_url = '/accounts/login')
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit = False) # Don't save this form in Database
            instance.author = request.user # Find the user from login of him/her
            instance.save() # Now save the form with user name
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create_articles.html', {'form':form})
