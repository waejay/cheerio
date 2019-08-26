from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

user = get_user_model()

def index(request):

    if not request.user.is_authenticated:
        print("User is not logged in")
        return redirect('/accounts/login')
    else:
        print("User is not logged in")
        return redirect('/events')

    print("user is logged in")
    template = 'my_cheerio/index.html'
    context = locals()

    return render(request, template, context)
