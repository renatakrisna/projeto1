from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name= 'home'),
    path('cadastro/', Cadastro.as_view(), name= 'cadastro'),
    path('login/', Login.as_view(), name= 'login' ),
]