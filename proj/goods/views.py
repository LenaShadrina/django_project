from django.shortcuts import render
from django.views import generic as generic_views
from . import models
# Create your views here.


class ProductCreate(generic_views.CreateView):
    model = models.Product
    fields = ['title', 'cover']

class ProductDetail(generic_views.DetailView):
    model = models.Product

#class BookList(generic.ListView):
    #model = models.Book