"""bullscows URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game.urls')),
    path('users/', include('users.urls'))
]
