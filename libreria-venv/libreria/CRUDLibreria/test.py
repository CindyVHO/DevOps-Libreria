from unittest import TestCase

from .models import Libro

class LibroTest (TestCase):
    def setUp(self):
        a1 = Libro.objects.create(nombre="J.K. Rowling")
        a2 = Libro.objects.create(nombre="Miguel de Carvantes")
        Libro.objects.create(titulo="Harry Potter", autor=a1, resumen="Resumen del libro")
        Libro.objects.create(titulo="El Quijote", autor=a2, resumen="Resumen del libro")
    def test_libros_autor(self):
        libro1 = Libro.objects.get(titulo="Harry Potter")
        self.assertEqual(libro1.autor.nombre, "J.K. Rowling")
    def test_libros_puntuacion(self):
        libro2 = Libro.objects.get(titulo="El Quijote")
        self.assertEqual(libro2.get_puntuacion_media(), 0)
