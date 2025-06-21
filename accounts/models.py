from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('mitra', 'Mitra'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    no_hp = models.CharField(max_length=20, blank=True)
    alamat = models.TextField(blank=True)
    nik = models.CharField("Nomor KTP", max_length=20, blank=True)
    foto_ktp = models.ImageField(upload_to='ktp/', blank=True, null=True)
    selfie_ktp = models.ImageField(upload_to='selfie_ktp/', blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def clean(self):
        # Validasi khusus mitra
        if self.role == 'mitra':
            if not self.nik:
                raise ValidationError({'nik': 'NIK wajib diisi untuk mitra.'})
            if not self.foto_ktp:
                raise ValidationError({'foto_ktp': 'Foto KTP wajib diunggah untuk mitra.'})
            if not self.selfie_ktp:
                raise ValidationError({'selfie_ktp': 'Selfie dengan KTP wajib diunggah untuk mitra.'})
            if not self.tanggal_lahir:
                raise ValidationError({'tanggal_lahir': 'Tanggal lahir wajib diisi untuk mitra.'})

    def __str__(self):
        return f"{self.username} ({self.role})"
