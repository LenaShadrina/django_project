from os import walk
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from . import models


class GenreList(generic.ListView):
    model = models.Genre


class GenreDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Genre


class GenreCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Genre
    fields = ['name', 'description']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Greate a new Genre"
        return context


class GenreUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Genre
    fields = ['name', 'description']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Create a new Genre"
        return context


class GenreDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Genre
    success_url = reverse_lazy("main_references:genre-list")


class AuthorList(generic.ListView):
    model = models.Author


class AuthorDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Author



class AuthorCreate(LoginRequiredMixin,generic.CreateView):
    model = models.Author
    login_url = '/login/'
    fields = ['author', 'genre', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Greate a new Author"
        return context


class AuthorUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Author
    fields = ['author', 'genre', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Greate a new Author"
        return context


class AuthorDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Author
    success_url = reverse_lazy("main_references:author-list")

