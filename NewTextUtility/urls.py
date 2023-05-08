"""NewTextUtility URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index ,  name='Index'),
    path('uppercase', views.uppercase, name='UPPERCASE'),
    path('lowercase', views.lowercase, name='lowercase'),
    path('remove', views.remove, name='remove'),
    path('removepunc', views.removepunc, name='removepunc'),
    path('extraspaces', views.extraspaces, name='extraspace'),
    path('wordcount', views.wordscount, name='wordscount'),
    path('replace', views.replace, name='replace'),
    path('about', views.about, name='about'),
    


    path('UPPERCASE', views.an_uppercase, name='UPPERCASE'),
    path('LOWERCASE', views.an_lowercase, name='LOWERCASE'),
    path('REMOVE', views.an_remove, name='REMOVE'),
    path('REMOVEPUNC', views.an_removepunc, name='REMOVEPUNC'),
    path('EXTRASPACES', views.an_extraspaces, name='EXTRASPACES'),
    path('WORDSCOUNT', views.an_wordscount, name='WORDSCOUNT'),
    path('REPLACE', views.an_replace, name='REPLACE'),
]
