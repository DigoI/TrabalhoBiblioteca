from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('books', book_list, name='book_list'),
    path('book/<int:book_id>', book_details, name='book_details'),
    path('create_book', create_book, name='create_book'),
    path('edit_book/<int:book_id>', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>', delete_book, name='delete_book'),
    path('categorias', categorias, name='categorias'),
    path('categoria/<int:id>', categoria, name='categoria')
]