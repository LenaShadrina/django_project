from django.urls import path, include
from . import views


app_name = "accounts"
urlpatterns = [
    path('login/', views.MyLoginView.as_view()),
    path('profile/', views.CustomerProfileDetail.as_view(), name="profile-detail"),
    path('profile-create/', views.CustomerProfileCreate.as_view(), name="profile-create"),
]