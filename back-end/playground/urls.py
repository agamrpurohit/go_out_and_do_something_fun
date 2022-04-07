#map urls to view functions
from django.urls import path

from . import views # from current folder

# Url Conf
urlpatterns = [
    path('say_hi/', views.say_hello),
    path('say_hello/', views.say_big_hello)
]

#urlpatterns is what django looks for
