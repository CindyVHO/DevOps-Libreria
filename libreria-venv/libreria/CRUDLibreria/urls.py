from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listarLibros, name='listaLibros'),
    url(r'^add/$', views.agregarLibros, name='agregarLibros'),
    url(r'^(?P<libroid>\d+)/', views.actualizarLibros, name='actualizarLibros'),
    url(r'^(?P<libroid>\d+)/delete/', views.eliminarLibros, name='eliminarLibros'),

]
