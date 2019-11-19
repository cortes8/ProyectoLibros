from django.urls import path
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('books/', views.BookListView.as_view(), name='books'),
	path('galeria', views.galeria, name='galeria'),
    path('formulario', views.formulario, name='formulario'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]



