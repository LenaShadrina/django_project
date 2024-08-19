from django.urls import path, include
from . import views

app_name = "orders"
urlpatterns = [
    path('cart/', views.view_cart, name="view-cart"),
    path('add-product/', views.add_product_to_cart_view, name="add-product-to-cart"),
    path('evaluate/', views.evaluate_cart, name="evaluate-cart"),
]