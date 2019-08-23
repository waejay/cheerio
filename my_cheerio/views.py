from django.shortcuts import render

def index(request):

    template = 'my_cheerio/index.html'
    context = locals()

    return render(request, template, context)
