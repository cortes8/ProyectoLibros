from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

class Genero(models.Model):
#modelo representando genero del libro Al finalde la clase, 
#hemos declarado el método __str__(), que simplemente devuelve el nombre de un
#género definido por un registro en particular.
    name = models.CharField(max_length=200)
#El modelo tiene un único campo (name), de tipo CharField, que usaremos para describir el
#género literario
    def __str__(self):
        return self.name


class Book(models.Model):
    
	titulo = models.CharField(max_length=200)
	autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
	descripcion = models.TextField(max_length=1000, help_text='Pequeña descripcion del libro')
	genero = models.ManyToManyField(Genero)
    
	def __str__(self):
		return self.titulo
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('galeria', args=[str(self.id)])




#copias del libro esta disponible o no, fecha para que sea devuelto, imprenta,id unico
class Estado_libro(models.Model):
#UUIDField es usado para establecer el campo id como una primary_key para este modelo. 
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identificación única para este libro en particular en toda la biblioteca')
#DateField es usado para la fecha due_back  este valor puede ser blank o null   
	book = models.ForeignKey('book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)
#status es un CharField que define una lista de elección/selección
	LOAN_STATUS = (
		('d', 'Disponible'),
		('a', 'Agotado'),
		
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='d',
		help_text='Estado de libro',
	)

	class Meta:
		ordering = ['due_back']
#El patrón __str__() representa el objeto Estado de libro usando una combinación de su id
#único y el título del Book asociado.
	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.book.titulo})'



#Todos los campos/métodos ahora deben ser familiares. El modelo define a un autor que tiene
#un primer nombre, apellido, fecha de nacimiento, y (opcional) fecha de fallecimiento.
#Especifica que de forma predeterminada el __str__() retorna el nombre en el orden
#apellido, primer nombre. El método get_absolute_url() invierte el mapeo URL author-detail para
#obtener el URL para mostrar un autor individual.
class Autor(models.Model):
	"""Model representing an author."""
	primer_nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	año_nacimiento = models.DateField(null=True, blank=True)
	año_defuncion = models.DateField('defuncion', null=True, blank=True)

	class Meta:
		ordering = ['apellido', 'primer_nombre']

	def get_absolute_url(self):
		return reverse('autor-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.apellido}, {self.primer_nombre}'
