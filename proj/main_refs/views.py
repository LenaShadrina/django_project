from os import walk
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.conf import settings
from . import models


class GenreList(generic.ListView):
    model = models.Genre


class GenreDetail(generic.DetailView):
    model = models.Genre


class GenreCreate(generic.CreateView):
    model = models.Genre
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Greate a new Genre"
        return context


class GenreUpdate(generic.UpdateView):
    model = models.Genre
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Greate a new Genre"
        return context


class GenreDelete(generic.DeleteView):
    model = models.Genre
    success_url = "/genre-list-cbv/"


class AuthorList(generic.ListView):
    model = models.Author


class AuthorDetail(generic.DetailView):
    model = models.Author


class AuthorCreate(generic.CreateView):
    model = models.Author
    fields = ['author', 'genre', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Greate a new Author"
        return context


class AuthorUpdate(generic.UpdateView):
    model = models.Author
    fields = ['author', 'genre', 'description']


class AuthorDelete(generic.DeleteView):
    model = models.Author
    success_url = "/author-list-cbv/"
