from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Book, Category


class BookListView(ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'bookinfo/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context_data = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = Book.objects.all()
        categories = Category.objects.all()
        context_data['books'] = books
        context_data['categories'] = categories

        return context_data


class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = "id"
    template_name = 'bookinfo/details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context_data = super(BookDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        categories = Category.objects.all()
        context_data['categories'] = categories

        return context_data


class CategoryListView(ListView):
    model = Book
    template_name = 'bookinfo/category.html'
    context_object_name = 'books'

    def get_queryset(self):
        if self.kwargs['c_slug']:
            return self.model.objects.filter(categories__c_slug=self.kwargs['c_slug'])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context_data = super(CategoryListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        categories = Category.objects.all()
        context_data['categories'] = categories

        return context_data


class BookSearch(View):

    def post(self, request):
        search_text = request.POST.get('search')
        categories = []
        if search_text:
            books = Book.objects.filter(
                title__icontains=search_text).distinct()
        else:
            books = ['No Items found']

        return render(request, 'bookinfo/search.html', {'books': books, 'categories': categories})
