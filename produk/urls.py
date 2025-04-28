from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_produk_view, name='daftar_produk'),
    path('<int:id_produk>/', views.detail_produk, name='detail_produk'),
]