from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# Create your models here.
class Genre(models.Model):
#modelo representando genero del libro Al finalde la clase, 
#hemos declarado el método __str__(), que simplemente devuelve el nombre de un
#género definido por un registro en particular.
    name = models.CharField(max_length=200)
#El modelo tiene un único campo (name), de tipo CharField, que usaremos para describir el
#género literario
    def __str__(self):
        return self.name



class Book(models.Model):
    
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
	isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre)
    
	def __str__(self):
		return self.title
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('book-detail', args=[str(self.id)])




#copias del libro esta disponible o no, fecha para que sea devuelto, imprenta,id unico
class BookInstance(models.Model):
#UUIDField es usado para establecer el campo id como una primary_key para este modelo. 
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
#DateField es usado para la fecha due_back  este valor puede ser blank o null   
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)
#status es un CharField que define una lista de elección/selección
	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Book availability',
	)

	class Meta:
		ordering = ['due_back']
#El patrón __str__() representa el objeto BookInstance usando una combinación de su id
#único y el título del Book asociado.
	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.book.title})'



#Todos los campos/métodos ahora deben ser familiares. El modelo define a un autor que tiene
#un primer nombre, apellido, fecha de nacimiento, y (opcional) fecha de fallecimiento.
#Especifica que de forma predeterminada el __str__() retorna el nombre en el orden
#apellido, primer nombre. El método get_absolute_url() invierte el mapeo URL author-detail para
#obtener el URL para mostrar un autor individual.
class Author(models.Model):
	"""Model representing an author."""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.last_name}, {self.first_name}'
