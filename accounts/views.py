from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

# Here we say, if the method was POST, get info from user and if that info is valid, save them in DB
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('articles:list')




# Else --> ( if method was get ) show a empty list to user
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form':form})



# Function to login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            # if it was valid -->
            user = form.get_user()
            login(request, user)

            # here we mean if there is a 'next' in our request.POST: do this:
            if 'next' in request.POST:
                return redirect(request.POST.get('next')) # This 'next' is the name of input value in login.html 

            else:
                return redirect('articles:list')


    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})




# Logout Function
def logout_view(request):
    if request.method == 'POST':
        logout(request)

        return redirect('articles:list')
