from django.shortcuts import render

from .models import Event, Note

def list_events(request):

    list_of_events = Event.objects.filter(member=request.user)

    template = 'events/list_of_events.html'
    context = locals()

    return render(request, template, context)

    
