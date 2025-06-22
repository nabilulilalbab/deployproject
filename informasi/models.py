from django.db import models
from django.utils.text import slugify

# Model untuk halaman statis seperti "Tentang Kami", "Kebijakan Privasi"
class Page(models.Model):
    title = models.CharField(max_length=200, help_text="Judul halaman, contoh: 'Tentang Kami'")
    slug = models.SlugField(max_length=200, unique=True, blank=True, help_text="URL unik (contoh: tentang-kami). Biarkan kosong agar terisi otomatis.")
    content = models.TextField(help_text="Isi utama dari halaman. Anda bisa menggunakan HTML di sini.")
    header_image = models.ImageField(upload_to='informasi/headers/', blank=True, null=True, help_text="Gambar banner opsional untuk bagian atas halaman.")
    is_published = models.BooleanField(default=True, help_text="Centang untuk menampilkan halaman ini di situs.")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# Model untuk anggota tim di halaman "Tentang Kami"
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, help_text="Contoh: Founder & CEO")
    bio = models.TextField(blank=True, help_text="Deskripsi singkat tentang anggota tim.")
    photo = models.ImageField(upload_to='team/', help_text="Foto profil anggota tim.")
    order = models.PositiveIntegerField(default=0, help_text="Urutan tampil (0 akan tampil pertama).")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

# Model untuk menampung pesan dari form kontak
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Pesan dari {self.name} - {self.subject}"
