from django.shortcuts import render, redirect
from django.views.generic import ListView
from dashboard.models import Book, BooksOfUsers
from dashboard.forms import RatingForm, StatusForm


class BookList(ListView):
    model = Book


def detailsPage(request, pk):
    if not request.user.is_authenticated:
        return redirect('/users')

    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        rating_form = RatingForm(request.POST)
        status_form = StatusForm(request.POST)
        if rating_form.is_valid():
            rating_form_clean_data = rating_form.cleaned_data
            rating = rating_form_clean_data.get('rating')
            book_of_user, created = BooksOfUsers.objects.get_or_create(user=request.user, book=book)
            book_of_user.rating = rating
            book_of_user.save()
            book_general_rating = book.general_rating
            book_rating_count = book.rating_count
            book_general_rating = ((book_general_rating * book_rating_count) + rating) / (book_rating_count + 1)
            book_rating_count += 1
            book.general_rating = int(book_general_rating)
            book.rating_count = int(book_rating_count)
            book.save()
        if status_form.is_valid():
            status_form_data = status_form.cleaned_data
            status = status_form_data.get('status')
            book_of_user, created = BooksOfUsers.objects.get_or_create(user=request.user, book=book)
            book_of_user.status = status
            book_of_user.save()

    try:
        book_of_user = BooksOfUsers.objects.get(user=request.user, book=book)
    except:
        book_of_user = None
    rating_form = RatingForm()
    status_form = StatusForm()

    return render(request, 'dashboard/book_details.html',
                  {'book': book, 'rating_form': rating_form, 'book_of_user': book_of_user, 'status_form': status_form})


def myBooksList(request):
    books_of_user = BooksOfUsers.objects.filter(user=request.user)
    books_of_user = [book for book in books_of_user if book.status != 'Nie wybrano']
    books_ids = [book.book.id for book in books_of_user]
    books = Book.objects.all()
    books = [book for book in books if book.id in books_ids]

    return render(request, 'dashboard/book_list.html', {'object_list': books})