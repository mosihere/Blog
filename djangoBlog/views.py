# we import 2 module here
from django.shortcuts import render
# http respose module will catch http requests and print sth in that URL
# if that url is called
from django.shortcuts import HttpResponse


# This request is just for django and it not like python
def about(request):
    # return HttpResponse('Hi there!')
    return render(request, 'about.html')
    # render will Rend to request the Special Page that we introduce
    # render will take 2 parameters/ first is request same as function
    # second is our file that we want to connect with urls :) here is home.html



# This is our Home and root page :)
def home(request):
    # return HttpResponse('This is our Home :)')
    return render(request, 'home.html')
