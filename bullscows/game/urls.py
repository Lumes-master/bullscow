from django.urls import path
from .views import *
app_name = 'game'
urlpatterns = [
    path('', index, name = 'home'),
    path('bullscows/', bullscows, name = 'bullscows'),

]