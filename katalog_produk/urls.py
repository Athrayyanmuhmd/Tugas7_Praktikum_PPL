from django.contrib import admin
from django.urls import path, include
from produk.views import home, kontak, tentang_kami

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('produk/', include('produk.urls')),
    path('tentang/', tentang_kami, name='tentang_kami'),
    path('kontak/', kontak, name='kontak'),
]