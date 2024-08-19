from os import walk
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from . import models



class GenreList(generic.ListView):
    model = models.Genre
    permission_required = [
        "main_refs.view_genre"
    ]


class GenreDetail(generic.DetailView):
    model = models.Genre
    permission_required = [
        "main_refs.view_genre"
    ]

class GenreCreate(generic.CreateView):
    model = models.Genre
    fields = ['name', 'description']
    permission_required = [
        "main_refs.add_genre",
        "main_refs.view_genre"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Greate a new Genre"
        return context


class GenreUpdate(generic.UpdateView):
    model = models.Genre
    fields = ['name', 'description']
    permission_required = [
        "main_refs.change_genre"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Create a new Genre"
        return context


class GenreDelete(generic.DeleteView):
    model = models.Genre
    success_url = reverse_lazy("main_references:genre-list")
    permission_required = [
        "main_refs.delite_genre"
    ]


class AuthorList(generic.ListView):
    model = models.Author
    permission_required = [
        "main_refs.view_authors",
        "sessions.add_session"
    ]


class AuthorDetail(generic.DetailView):
    model = models.Author
    permission_required = [
        "main_refs.view_authors"
    ]


class AuthorCreate(PermissionRequiredMixin, generic.CreateView):
    model = models.Author
    login_url = '/login/'
    permission_required = [
        "main_refs.add_authors",
        "main_refs.view_authors",
        "sessions.add_session"
    ]
    fields = ['author', 'genre', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Greate a new Author"
        return context


class AuthorUpdate(PermissionRequiredMixin, generic.UpdateView):
    model = models.Author
    fields = ['author', 'genre', 'description']
    permission_required = [
        "main_refs.change_authors",
        "sessions.add_session"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Greate a new Author"
        return context


class AuthorDelete(PermissionRequiredMixin, generic.DeleteView):
    model = models.Author
    success_url = reverse_lazy("main_references:author-list")
    permission_required = [
        "main_refs.delite_authors",
        "sessions.add_session"
    ]
