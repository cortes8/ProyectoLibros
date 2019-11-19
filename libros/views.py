from django.shortcuts import render
from .models import Book, Autor, Estado_libro, Genero
from django.views import generic
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_libros=Book.objects.all().count()
    num_instancias=Estado_libro.objects.all().count()
    # Libros disponibles (status = 'd')
    num_libros_d=Estado_libro.objects.filter(status__exact='d').count()
    num_autors=Autor.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_libros':num_libros,'num_instancias':num_instancias,'num_libros_d':num_libros_d,'num_autors':num_autors},
    )
    
def galeria(request):
    return render(request,'galeria.html')  

def formulario(request):
    return render(request,'formulario.html') 
    
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
class BookDetailView(generic.DetailView):
    model = Book



from django.views import generic

class AutorDetailView(generic.DetailView):
    """Generic class-based detail view for an autor."""
    model = Autor


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Autor

class AutorCreate(CreateView):
    model = Autor
    fields = '__all__'
    initial={'fecha_de_muerte':'05/01/2018',}

