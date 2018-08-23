from django.db import models

# Create your models here.

class Libro(models.Model):
    nombre = models.CharField('nombre', max_length=100)
    autor = models.CharField('autor', max_length=100)
    isbn = models.CharField('isbn', max_length=100)
    urlImagen = models.CharField('urlImg', max_length=100)
    editorial = models.CharField('editorial', max_length=100)
    anioPublicacion = models.CharField('anioPublicacion', max_length=100)

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'
        ordering = ['nombre']

    def __unicode__(self):
        return '%s %s %s' % (self.nombre, self.autor, self.isbn)