from django.shortcuts import render

# Create your views here.
from . import forms
from django.contrib.auth import login, authenticate  # add to imports

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate( # Returns NONE if invalid, does not login by itself
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        # Authentication/login.html is a template
        request, 'authentication/login.html', context={'form': form, 'message': message})