from django.shortcuts import render
from .models import Libro
# Create your views here.
def listarLibros(request):
    lista_libros = Libro.objects.all()
    context = {'lista_libros': lista_libros}
    return render(request, 'index.html', context)

