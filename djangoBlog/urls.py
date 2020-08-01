"""djangoBlog URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
# when we create a new app,we have to create a urls.py file for that
# also we have to use include funtion to say to mail urls.py(means here)
# look at that urls.py like urls :) we have to import include module :)



# we import views here
from . import views
# We import bellow modile for static files such as html-css-js
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Here we import setting.py
from django.conf import settings


# With this we can access URL
from django.conf.urls.static import static


from articles.views import articles_list
# here we must use "path" and pass two parameters to that :)
# first parameter is our url for example www.mosihere.com/about
# second parameter is our Function that we Define in  File "Views.py"
# Tip --> '/' is our root ( Home ) and also we can use ' ' and if we connect
# to http:127.0.0.1:8000 we will see this page :)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    # for import a url from another app urls.py we have to use path like example bellow:
    path('articles/', include('articles.urls')),
    # it means if user wanna check articles page, include articles.urls
    # Tip --> (it means urls.py file of articles App)

    path('accounts/', include('accounts.urls')),
    path('', articles_list),

]

# Some urls will add to our main urls :)
urlpatterns += staticfiles_urlpatterns()

# This will add this url to the folder that our medias keeping there
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
