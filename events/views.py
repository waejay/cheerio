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
    events = Event.objects.filter(event_code=event_code)

    if not events:
        print(f"event {event_code} does not exist")
        return redirect('/events')

    event_to_join = Event.objects.get(event_code=event_code)
    event_to_join.member.add(request.user)


    return redirect('/events')

@login_required
def create_event(request):
    
    template = 'events/create_event.html'
    context = locals()

    return render(request, template, context)

@login_required
def submit_created_event(request):

   event_to_create = Event.objects.create(name        = request.POST['project-name'],
                                          owner       = request.user,
                                          region      = request.POST['region'],
                                          description = request.POST['description'],
                                          event_code  = request.POST['event-code'],
                                          )

   event_to_create.member.add(request.user)

   event_to_create.save()

   return redirect('/events/')

@login_required
def create_note(request, event_id):

    current_event = Event.objects.get(id=event_id)

    note_to_create = Note.objects.create(first_name     = request.POST['first-name'],
                                         last_name      = request.POST['last-name'],
                                         content        = request.POST['content'],
                                         event          = current_event,
                                         owner          = request.user)

    note_to_create.save()

    return redirect('/events/' + str(event_id))


def delete_note(requet, event_id, note_id):

    note_to_delete = Note.objects.get(id=note_id)

    note_to_delete.delete()

    return redirect('/events/' + str(event_id))
