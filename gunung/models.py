from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.contrib.auth import get_user_model

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

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)  # Simpan dulu agar dapat ID

        # Jika objek baru dan slug belum di-set
        if is_new and not self.slug:
            self.slug = f"{self.pk}-{slugify(self.nama)}"
            super().save(update_fields=["slug"])

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