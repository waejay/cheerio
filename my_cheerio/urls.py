from django.urls import path, include

from . import views
from users import views as users_views
from events import views as events_views

urlpatterns = [
    path('', views.index, name="my_cheerio-index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', users_views.signup, name="signup"),
    path('events/', events_views.list_events, name="list_events"),
    path('events/<int:event_id>/', events_views.event_id, name="event_id"),
    path('events/join/', events_views.join_event, name="join_event"),
    path('events/create/', events_views.create_event, name="create_event"),
    path('events/create/submit', events_views.submit_created_event, name="submit-event"),
    path('events/<int:event_id>/notes/create', events_views.create_note, name="create-note"),
    path('events/<int:event_id>/notes/delete/<int:note_id>/', events_views.delete_note, name="delete_note"),
    
]
