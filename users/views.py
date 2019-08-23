from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm

def signup(request):

    if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('my_cheerio-index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
