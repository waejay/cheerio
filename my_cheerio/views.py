from django.shortcuts import render
from django.contrib.auth import get_user_model

user = get_user_model()

def index(request):

    template = 'my_cheerio/index.html'
    context = locals()

    return render(request, template, context)
