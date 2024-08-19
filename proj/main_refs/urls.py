from django.urls import path, include
from . import views


app_name = "main_references"
urlpatterns = [
    path('genre-list-cbv/', views.GenreList.as_view(), name="genre-list"),
    path('genre-detail-cbv/<int:pk>/', views.GenreDetail.as_view(), name="genre-detail"),
    path('genre-create-cbv/', views.GenreCreate.as_view(), name="genre-create"),
    path('genre-update-cbv/<int:pk>/', views.GenreUpdate.as_view(), name="genre-update"),
    path('genre-delete-cbv/<int:pk>/', views.GenreDelete.as_view(), name="genre-delete"),
    path('author-list-cbv/', views.AuthorList.as_view(), name="author-list"),
    path('author-detail-cbv/<int:pk>/', views.AuthorDetail.as_view(), name="author-detail"),
    path('author-create-cbv/', views.AuthorCreate.as_view(), name="author-create"),
    path('author-update-cbv/<int:pk>/', views.AuthorUpdate.as_view(), name="author-update"),
    path('author-delete-cbv/<int:pk>/', views.AuthorDelete.as_view(), name="author-delete"),
]