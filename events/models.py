from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from users.models import CustomUser

class Event(models.Model):
    name         = models.CharField(max_length=200, null=True)
    owner        = models.ForeignKey(get_user_model(),
                                     on_delete=models.CASCADE,
                                     related_name='owner_of',
                                     null=True)
    region       = models.CharField(max_length=200, null=True)
    description  = models.TextField(null=True)
    event_pw     = models.CharField(max_length=50, null=True, blank=True)
    member       = models.ManyToManyField(get_user_model())
    

    def __str__(self):
        return self.name
    
    def set_owner(self, CustomUser):
        self.owner = CustomUser
        self.save()


class Note(models.Model):
    first_name   = models.CharField(max_length=100, null=True)
    last_name    = models.CharField(max_length=100, null=True)
    content      = models.TextField()
    author       = models.CharField(max_length=200, default="Anon")
    event        = models.ForeignKey(Event, null=True, on_delete=models.CASCADE)
    num_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content
