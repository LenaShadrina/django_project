from django.urls import path, include
from . import views

app_name = "goods"
urlpatterns = [
    path('product-create/', views.ProductCreate.as_view(), name="product-create"),
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name="product-detail"),
    path('book-list-cbv/', views.BookList.as_view(), name="book-list"),
    path('book-detail-cbv/<int:pk>/', views.BookDetail.as_view(), name="book-detail"),
    path('book-create-cvb/', views.BookCreate.as_view(), name="book-create"),
    path('book-update-cvb/<int:pk>/',views.BookUpdate.as_view(), name="book-update"),
    path('book-delete-cbv/<int:pk>/', views.BookDelete.as_view(), name="book-delete"),
]