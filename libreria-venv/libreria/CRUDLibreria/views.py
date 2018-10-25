from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from .models import Libro
from .forms import LibroForm

# Create your views here.
def listarLibros(request):
    lista_libros = Libro.objects.all()
    context = {'lista_libros': lista_libros}
    return render(request, 'listar.html', context)

def agregarLibros(request):
    form = LibroForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The post has been saved!")
            return HttpResponseRedirect("/CRUDLibreria/")

    return render(request, 'agregarForm.html', {'form': form})


def actualizarLibros(request, libroid):
    instance = get_object_or_404(Libro, id=libroid)
    form = LibroForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El libro ha sido actualizado")
            return HttpResponseRedirect("/CRUDLibreria/")

    return render(request, 'agregarForm.html', {'form': form})


def eliminarLibros(request, libroid):
    instance = get_object_or_404(Libro, id=libroid)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "El libro con id %s ha sido eliminado!" % libroid)
    return HttpResponseRedirect("/CRUDLibreria/")