from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

# Here we say, if the method was POST, get info from user and if that info is valid, save them in DB
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: Users Login
            return redirect('articles:list')


# Else --> ( if method was get ) show a empty list to user
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form':form})
