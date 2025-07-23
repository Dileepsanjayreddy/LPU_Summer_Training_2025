from msilib.schema import ListView

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, CreateView, UpdateView

from librarymgnt.models import Book


# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'librarymgnt/listallbooks.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'librarymgnt/displaylbook.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'librarymgnt/addnewbook.html'
    fields = '__all__'
    success_url = reverse_lazy('listallbooks')

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'librarymgnt/modifybookdetails.html'
    fields = '__all__'
    success_url = reverse_lazy('listallbooks')