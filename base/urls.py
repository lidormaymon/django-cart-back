
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('prods', views.ProductViewSet.as_view()),
    path('prods/<pk>', views.ProductViewSet.as_view()),
    path('orders', views.OrderViewSet.as_view()),
    path('orders/<pk>', views.OrderViewSet.as_view()),
    path('deliveries', views.DeliveriesViewSet.as_view()),
    path('deliveries/<pk>', views.DeliveriesViewSet.as_view()),
    path('register/', views.register),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('about', views.about),
    path('add-cart', views.CartView.as_view())


]

