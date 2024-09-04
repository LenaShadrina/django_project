from django.urls import path, include
from . import views

app_name = "orders"
urlpatterns = [
    path('cart/', views.view_cart, name="view-cart"),
    path('add-product/', views.add_product_to_cart_view, name="add-product-to-cart"),
    path('evaluate/', views.evaluate_cart, name="evaluate-cart"),
    path('create-order/', views.CreateOrderView.as_view(), name="view-order-create"),
    path('view-order/', views.OrderView.as_view(), name="view-order"),
    path('created/', views.OrderCreateView.as_view(), name="created-page"),
]