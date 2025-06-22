from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Impor library yang diperlukan untuk optimasi gambar
from PIL import Image
import io
import os
from django.core.files.base import ContentFile

User = get_user_model()

KATEGORI_CHOICES = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
]

class Gunung(models.Model):
    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    deskripsi = RichTextUploadingField()
    foto = models.ImageField(upload_to='foto_gunung/')
    kategori = models.CharField(max_length=10, choices=KATEGORI_CHOICES)
    template_file = models.FileField(upload_to='template_gunung/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    # Override method save() untuk optimasi gambar dan pembuatan slug
    def save(self, *args, **kwargs):
        # 1. GENERATE SLUG (jika belum ada)
        # Cara ini lebih sederhana dan tidak memerlukan save dua kali.
        if not self.slug:
            self.slug = slugify(self.nama)
            # Opsional: Tambahkan logika untuk memastikan slug unik jika ada nama gunung yang sama
            # Misalnya dengan menambahkan ID setelah disimpan, atau menambahkan string acak.
            # Tapi untuk sekarang, ini sudah cukup.

        # 2. PROSES OPTIMASI GAMBAR
        # Cek jika field 'foto' memiliki file baru yang di-upload
        # `hasattr(self.foto, 'file')` memastikan ini hanya berjalan saat ada file baru
        if self.foto and hasattr(self.foto.file, 'content_type'):
            try:
                # Buka gambar menggunakan Pillow
                img = Image.open(self.foto)

                # Atur ukuran maksimal, misal 1280x1280 piksel
                max_size = (1280, 1280)
                img.thumbnail(max_size)

                # Buat buffer untuk menyimpan gambar baru
                buffer = io.BytesIO()
                
                # Simpan ke buffer dengan format WebP dan kualitas 85%
                img.save(buffer, format='WEBP', quality=85)

                # Ganti nama file dengan ekstensi .webp
                nama_file_asli, _ = os.path.splitext(self.foto.name)
                nama_file_webp = nama_file_asli + '.webp'
                
                # Simpan file dari buffer ke field 'foto'
                # Ini akan menimpa file asli yang di-upload dengan versi teroptimasi
                self.foto.save(nama_file_webp, ContentFile(buffer.getvalue()), save=False)

            except Exception as e:
                # Jika terjadi error saat proses gambar (misal file bukan gambar valid),
                # lewati saja proses optimasi.
                print(f"Error optimizing image: {e}")

        # 3. SIMPAN SEMUANYA KE DATABASE
        # Panggil method save() asli untuk menyimpan semua perubahan (slug & gambar baru)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama


class Komentar(models.Model):
    gunung = models.ForeignKey('Gunung', on_delete=models.CASCADE, related_name='komentar')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isi = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.gunung.nama}"
