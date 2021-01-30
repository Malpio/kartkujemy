from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template, Context
from datetime import date
from django.contrib import messages
from .forms import LoginForm, RegistryForm
from .models import User
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_form_data = form.cleaned_data
            email = login_form_data.get('email')
            password = login_form_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard/')
            else:
                messages.warning(request, 'Nieprawidłowe dane logowania')
        else:
            messages.warning(request, 'Nieprawidłowe dane logowania')
    form = LoginForm()
    return render(request, 'loginPage.html', {'form': form})


def registryPage(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == 'POST':
        form = RegistryForm(request.POST)
        if form.is_valid():
            registry_form_cleaned_data = form.cleaned_data
            first_name = registry_form_cleaned_data.get('first_name')
            last_name = registry_form_cleaned_data.get('first_name')
            email = registry_form_cleaned_data.get('email')
            password = registry_form_cleaned_data.get('password')
            user, created = User.objects.get_or_create(email=email, first_name=first_name, last_name=last_name)
            if not created:
                messages.warning(request, 'Użytkownik o tym adresie email już istnieje!')
            else:
                user.set_password(password)
                user.save()
                return redirect('login')
        else:
            messages.warning(request, 'Nieprawidłowe dane rejestracji')
    form = RegistryForm()
    return render(request, 'registryPage.html', {'form': form})


def logoutPage(request):
    logout(request)
    return redirect('/users/')
