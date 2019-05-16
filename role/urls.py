from django.contrib import admin
from django.urls import path, include
from role import views

app_name = 'role'

urlpatterns = [
    path('register/', views.user_interests, name='user_interests'),
]
