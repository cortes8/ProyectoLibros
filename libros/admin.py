from django.contrib import admin

# Register your models here.

from . models import Autor, Genero, Book, Estado_libro ,Clientes

admin.site.register(Clientes)
admin.site.register(Book)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Estado_libro)