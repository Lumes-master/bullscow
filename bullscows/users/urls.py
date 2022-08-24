from django.urls import path, include
from django.contrib.auth import urls
from .views import *
app_name = 'users'

urlpatterns = [
    path('login_user/', login_user, name='login'),
    path('registration/', Register.as_view(), name = 'registration'),
    path('logout/', logout_user, name = 'logout'),
    # path('login/', login, name = 'login'),

    # path('users/', users, name = 'users'),

]