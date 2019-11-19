from django.db import models
from django.urls import reverse 
import uuid 

class Genero(models.Model):

    name = models.CharField(max_length=200)

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





class Estado_libro(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identificación única para este libro en particular en toda la biblioteca')
 
	book = models.ForeignKey('book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

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

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.book.titulo})'


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


class Clientes(models.Model):
	"""Model representing an Clientes."""
	primer_nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	año_nacimiento = models.DateField(null=True, blank=True)
	direccion = models.CharField(max_length=100)

	class Meta:
		ordering = ['apellido', 'primer_nombre']

	

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.apellido}, {self.primer_nombre}'
