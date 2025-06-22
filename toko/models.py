from django.db import models
from django.conf import settings

# Impor library yang diperlukan untuk optimasi gambar
from PIL import Image
import io
import os
from django.core.files.base import ContentFile

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

    # +++ METHOD BARU UNTUK OPTIMASI GAMBAR +++
    def save(self, *args, **kwargs):
        # Cek jika ada file gambar baru yang di-upload
        if self.foto_produk and hasattr(self.foto_produk.file, 'content_type'):
            try:
                # Buka gambar menggunakan Pillow
                img = Image.open(self.foto_produk)

                # Atur ukuran maksimal untuk foto produk, misal 800x800 piksel
                max_size = (800, 800)
                img.thumbnail(max_size)

                # Buat buffer untuk menyimpan gambar baru
                buffer = io.BytesIO()
                
                # Simpan ke buffer dengan format WebP dan kualitas 85%
                img.save(buffer, format='WEBP', quality=85)

                # Ganti nama file dengan ekstensi .webp
                nama_file_asli, _ = os.path.splitext(self.foto_produk.name)
                nama_file_webp = nama_file_asli + '.webp'
                
                # Simpan file dari buffer ke field 'foto_produk' tanpa menyimpan ke DB dulu
                self.foto_produk.save(nama_file_webp, ContentFile(buffer.getvalue()), save=False)

            except Exception as e:
                # Jika gagal (misal file bukan gambar), lewati proses optimasi
                print(f"Gagal mengoptimasi gambar produk: {e}")

        # Panggil method save() asli untuk menyimpan semua perubahan
        super().save(*args, **kwargs)


class KomentarToko(models.Model):
    toko = models.ForeignKey(Toko, on_delete=models.CASCADE, related_name='komentar')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isi = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)  # 1–5 bintang
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.toko} ({self.rating})"
