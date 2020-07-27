from django.urls import path
from . import views

urlpatterns = [
# '' or '/' is root page (home) and here our home page is (www.mosihere/articles)
    path('', views.articles_list)
]
