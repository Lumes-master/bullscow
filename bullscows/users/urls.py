from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path('login_user/', login_user, name='login'),
    path('registration/', Register.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),

]
