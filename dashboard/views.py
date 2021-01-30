from django.http import HttpResponse
from django.shortcuts import render, redirect

def booksListPage(request):
    if not request.user.is_authenticated:
        return redirect('/users')

    return render(request, 'dashboard/booksListPage.html')

