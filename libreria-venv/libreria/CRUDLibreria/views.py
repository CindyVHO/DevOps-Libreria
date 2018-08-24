from django.shortcuts import render, HttpResponse
from rest_framework import serializers
from .models import Libro

# Create your views here.
def listarLibros(request):
    lista_libros = Libro.objects.all()
    context = {'lista_libros': lista_libros}
    return HttpResponse(se)

