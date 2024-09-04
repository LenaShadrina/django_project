from django.shortcuts import render, get_object_or_404
from django.views import generic as generic_views
from django.http import HttpResponseRedirect
from . import models, forms
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProductCreate(LoginRequiredMixin, generic_views.CreateView):
    model = models.Product
    fields = ['title', 'cover']


class ProductDetail(LoginRequiredMixin, generic_views.DetailView):
    model = models.Product


class BookList(generic_views.ListView):
    model = models.Book

    def book_list(request):
        books = objects.filter(available=True)
        return render(request, 'goods/book_list.html', {'books': books})



class BookDetail(LoginRequiredMixin, generic_views.DetailView):
    model = models.Book

    def book_detail(request):
        book = get_object_or_404(id=id, available=True)
        return render(request, 'goods/book_detail.html', {'book': book})


class BookCreate(LoginRequiredMixin, generic_views.CreateView):
    model = models.Book
    fields = [
        'name_book',
        'image_cover',
        'price',
        'authors',
        'series',
        'genres',
        'publication_date',
        'pages',
        'binding',
        'format',
        'isbn',
        'weight',
        'age_restriction',
        'publishing_house',
        'available',
        'description'
    ]


class BookUpdate(LoginRequiredMixin, generic_views.UpdateView):
    model = models.Book
    fields = [
        'name_book',
        'image_cover',
        'price',
        'authors',
        'series',
        'genres',
        'publication_date',
        'pages',
        'binding',
        'format',
        'isbn',
        'weight',
        'age_restriction',
        'publishing_house',
        'available',
        'description'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Create a new book"
        return context


class BookDelete(LoginRequiredMixin, generic_views.DeleteView):
    model = models.Book
    success_url = reverse_lazy("goods:book-list")


