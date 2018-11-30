from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    queryset = Book.objects.all()
    template_name = 'bookinfo/home.html'
    
class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = "id"
    template_name = 'bookinfo/details.html'

class CategoryListView(ListView):
    model = Book
    template_name = 'bookinfo/category.html'
    context_object_name = 'books'
    def get_queryset(self):
        if self.kwargs['c_slug']:
            return self.model.objects.filter(categories__c_slug=self.kwargs['c_slug'])