from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

class Cadastro(TemplateView):
    template_name = 'cadastro.html'
