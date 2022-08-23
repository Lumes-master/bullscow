from django.urls import path, include
from django.contrib.auth import urls
from .views import *
app_name = 'users'

urlpatterns = [
    path('login_user/', login_user, name='login'),
    path('registration/', Register.as_view(), name = 'registration')
    # path('login/', login, name = 'login'),
    # path('logout/', logout, name = 'logout'),
    # path('users/', users, name = 'users'),

]