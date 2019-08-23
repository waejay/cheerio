from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="my_cheerio-index"),
]
