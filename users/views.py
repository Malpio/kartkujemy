from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from datetime import date
from django.contrib import messages
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("qwe")
