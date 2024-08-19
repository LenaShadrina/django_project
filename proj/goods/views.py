from django.shortcuts import render
from django.views import generic as generic_views
from django.http import HttpResponseRedirect
from . import models, forms
from django.urls import reverse, reverse_lazy
# Create your views here.


class ProductCreate(generic_views.CreateView):
    model = models.Product
    fields = ['title', 'cover']
    permission_required = [
        "goods.view_product",
        "goods.add_product",
        "goods.change_product"
    ]


class ProductDetail(generic_views.DetailView):
    model = models.Product
    permission_required = [
        "goods.view_product"
    ]


class BookList(generic_views.ListView):
    model = models.Book
    permission_required = [
        "goods.view_book"
    ]


class BookDetail(generic_views.DetailView):
    model = models.Book
    permission_required = [
        "goods.view_book"
    ]


class BookCreate(generic_views.CreateView):
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
    permission_required = [
        "goods.add_book",
        "goods.view_book",
        "goods.change_book"
    ]


class BookUpdate(generic_views.UpdateView):
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
    permission_required = [
        "goods.add_book",
        "goods.view_book",
        "goods.change_book"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Create a new book"
        return context


class BookDelete(generic_views.DeleteView):
    model = models.Book
    success_url = reverse_lazy("goods:book-list")
    permission_required = [
        "goods.delite_book",
        "goods.view_book",
    ]

