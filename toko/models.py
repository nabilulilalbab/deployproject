from django.db import models
from django.conf import settings
# Create your models here.

class Toko(models.Model):
    nama = models.CharField(max_length=100)
    kabupaten = models.CharField(max_length=100) 
    alamat = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    def __str__(self):
        return self.nama

class Produk(models.Model):
    toko = models.ForeignKey(Toko, on_delete=models.CASCADE, related_name='produk')
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    foto_produk = models.ImageField(upload_to='produk/', blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.nama

class KomentarToko(models.Model):
    toko = models.ForeignKey(Toko, on_delete=models.CASCADE, related_name='komentar')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isi = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)  # 1–5 bintang
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.toko} ({self.rating})"
