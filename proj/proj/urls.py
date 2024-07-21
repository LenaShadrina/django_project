"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main_refs import views as main_refs_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre-list-cbv/', main_refs_views.GenreList.as_view()),
    path('genre-detail-cbv/<int:pk>/', main_refs_views.GenreDetail.as_view()),
    path('genre-create-cbv/', main_refs_views.GenreCreate.as_view()),
    path('genre-update-cbv/<int:pk>/', main_refs_views.GenreUpdate.as_view()),
    path('genre-delete-cbv/<int:pk>/', main_refs_views.GenreDelete.as_view()),
    path('author-list-cbv/', main_refs_views.AuthorList.as_view()),
    path('author-detail-cbv/<int:pk>/', main_refs_views.AuthorDetail.as_view()),
    path('author-create-cbv/', main_refs_views.AuthorCreate.as_view()),
    path('author-update-cbv/<int:pk>/', main_refs_views.AuthorUpdate.as_view()),
    path('author-delete-cbv/<int:pk>/', main_refs_views.AuthorDelete.as_view()),
]
