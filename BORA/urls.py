"""BORA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from home.views import Home
from userInterests.views import UsuarioInter
from login.views import Login
from login.views import logout_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home ),
    path('usuario_interesses/', UsuarioInter),
    path('entrar/', Login, name='login'),
    path('logout/', logout_request, name='logout'),
]
