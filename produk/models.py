
from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField(default=0)
    gambar = models.CharField(max_length=200, default='default.jpg')
    
    def __str__(self):
        return self.nama