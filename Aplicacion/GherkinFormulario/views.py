from django.views.generic import ListView
from django.shortcuts import render
from .models import CasoPrueba

# Create your views here.

class CasoPruebaListView(ListView):
    model = CasoPrueba
    template_name = "Index.html"

