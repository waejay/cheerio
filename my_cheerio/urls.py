from django.urls import path, include

from . import views
from users import views as users_views

urlpatterns = [
    path('', views.index, name="my_cheerio-index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', users_views.signup, name="user_views.signup"),
]
