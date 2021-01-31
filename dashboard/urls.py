from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('books/details/<uuid:pk>', views.detailsPage, name='book_view'),
    path('books/my_list', views.myBooksList, name='my_books'),
]