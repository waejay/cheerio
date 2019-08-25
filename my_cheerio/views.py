from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

user = get_user_model()

def index(request):

    if not user.is_authenticated:
        return redirect('signup')

    template = 'my_cheerio/index.html'
    context = locals()

    return render(request, template, context)
