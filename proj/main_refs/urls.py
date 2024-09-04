from django.urls import path, include
from . import views


app_name = "main_references"
urlpatterns = [
    path('genre-list-cbv/', views.GenreList.as_view(), name="genre-list"),
    path('genre-detail/<int:pk>/', views.GenreDetail.as_view(), name="genre-detail"),
    path('genre-create/', views.GenreCreate.as_view(), name="genre-create"),
    path('genre-update/<int:pk>/', views.GenreUpdate.as_view(), name="genre-update"),
    path('genre-delete/<int:pk>/', views.GenreDelete.as_view(), name="genre-delete"),
    path('author-list/', views.AuthorList.as_view(), name="author-list"),
    path('author-detail/<int:pk>/', views.AuthorDetail.as_view(), name="author-detail"),
    path('author-create/', views.AuthorCreate.as_view(), name="author-create"),
    path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name="author-update"),
    path('author-delete/<int:pk>/', views.AuthorDelete.as_view(), name="author-delete"),
]