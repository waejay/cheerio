from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Event, Note

def list_events(request):

    list_of_events = Event.objects.filter(member=request.user)

    template = 'events/list_of_events.html'
    context = locals()

    return render(request, template, context)

def event_id(request, event_id):

    current_event = Event.objects.get(id=event_id)
    list_of_notes = Note.objects.filter(event=current_event)
    
    template = 'events/event_id.html'
    context = locals()

    return render(request, template, context)

@login_required
def join_event(request):

    event_code = request.POST['event-code']
    events = Event.objects.filter(name=event_code)

    if not events:
        return redirect('/events')

    event_to_join = Event.objects.get(name=event_code)
    event_to_join.member.add(request.user)


    return redirect('/events')
