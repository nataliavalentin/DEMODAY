from django.contrib import admin
from django.urls import path, include
from user import views

app_name = 'user'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('reg/', views.registerUser, name='reg'),
    path('dashboard/', views.registerUser, name='dashboard'),
]
