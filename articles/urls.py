from django.urls import path
from . import views

# We create app name to prevent making misstake in case of having 2 same name in two urls files
app_name = 'articles'
urlpatterns = [
# '' or '/' is root page (home) and here our home page is (www.mosihere/articles)
    path('', views.articles_list, name='list'),
    path('<slug>', views.article_detail, name='detail'),
    # Here when sth type after home( here home is articles/ ) will know as slug and will add after articles/
]
