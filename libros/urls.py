from django.urls import path
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('books/', views.BookListView.as_view(), name='books'),
	path('galeria', views.galeria, name='galeria'),
    path('formulario', views.formulario, name='formulario'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('autor/<int:pk>', views.AutorDetailView.as_view(), name='autor-detail'),
]

urlpatterns += [
    path('autor/create/', views.AutorCreate.as_view(), name='autor_create'),
    path('autor/<int:pk>/update/', views.AutorUpdate.as_view(), name='autor_update'),
    path('autor/<int:pk>/delete/', views.AutorDelete.as_view(), name='autor_delete'),
]

