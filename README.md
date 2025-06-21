# 🏔️ Mount Project

Proyek Django untuk manajemen dan eksplorasi informasi gunung. Termasuk fitur komentar, rating, penghitungan pengunjung, serta pengelompokan berdasarkan kategori kesulitan.

Django project for mountain information management and exploration. Includes features for comments, ratings, visitor counting, and difficulty-based categorization.

## 🎯 Fitur Utama / Main Features

### 🏔 Informasi Gunung / Mountain Information
- Daftar gunung dengan kategori kesulitan (Easy, Medium, Hard)
- Deskripsi gunung dengan dukungan gambar
- Template/checklist pendakian yang dapat diunduh
- Pencarian dan filter gunung berdasarkan nama dan tingkat kesulitan
- Penghitung pengunjung halaman gunung
- Sistem komentar dan rating
- Tampilan komentar dengan paginasi

### 👥 Manajemen Pengguna / User Management
- Model pengguna kustom dengan akses berbasis peran
- Tiga peran pengguna: User, Mitra (Partner), dan Admin
- Profil pengguna dengan nomor telepon dan alamat
- Sistem autentikasi dengan login/logout

### 🏪 Sistem Toko / Shop System
- Daftar toko dengan data lokasi (latitude/longitude)
- Manajemen produk
- Dashboard pemilik toko (Mitra)
- Kategorisasi dan harga produk

### ➕ Fitur Tambahan / Additional Features
- Manajemen layanan rental
- Sistem feedback
- Rich text editing dengan integrasi CKEditor
- Manajemen file static dan media
- UI yang responsif

## 📁 Struktur Folder / Directory Structure

```

myproject/
├── accounts/           # Manajemen user
├── gunung/             # Fitur utama (data gunung, komentar, rating)
├── rental/             # (opsional) penyewaan peralatan
├── toko/               # (opsional) toko atau marketplace
├── feedback/           # (opsional) masukan dan testimoni
├── media/              # File upload (foto, template, dsb)
├── static/             # Static files (CSS, JS, gambar)
├── templates/          # Template HTML
├── db.sqlite3          # Database lokal (ignored in Git)
├── manage.py           # Entrypoint Django

````

---

## 🚀 Cara Menjalankan Proyek

### 1. Clone Repositori

```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
````

### 2. Buat dan Aktifkan Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Jika belum ada `requirements.txt`, kamu bisa buat dengan:
>
> ```bash
> pip freeze > requirements.txt
> ```

### 4. Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Buat Superuser

```bash
python manage.py createsuperuser
```

### 6. Jalankan Server

```bash
python manage.py runserver
```

Buka di browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Peran Pengguna / User Roles

### 1. User (Pendaki / Climber)
- Lihat informasi gunung / View mountain information
- Posting komentar dan rating / Post comments and ratings
- Akses layanan rental / Access rental services
- Lihat daftar toko / View shop listings

### 2. Mitra (Partner)
- Semua fitur User / All User features
- Kelola toko mereka / Manage their shop
- Tambah/edit produk / Add/edit products
- Kelola item rental / Manage rental items

### 3. Admin
- Akses penuh ke admin interface / Full access to admin interface
- Kelola semua konten dan pengguna / Manage all content and users
- Akses ke semua fitur / Access to all features

## 💻 Tech Stack

- Python 3.x
- Django 4.2.3
- SQLite Database
- django-ckeditor 6.7.3
- Pillow 11.2.1
- Whitenoise 6.9.0
- HTML/CSS/JavaScript

## 📦 Media & Static Files

Struktur folder media / Media folder structure:
```
media/
├── foto_gunung/       # Foto gunung / Mountain photos
├── template_gunung/   # Template pendakian / Climbing templates
└── uploads/           # Upload CKEditor / CKEditor uploads
```

Konfigurasi di settings.py / Settings.py configuration:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# CKEditor configuration
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_ALLOW_NONIMAGE_FILES = False
```

Dan di urls.py utama / And in main urls.py:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧪 Testing

Menjalankan test suite / Run the test suite:
```bash
python manage.py test
```

## 🔄 Development Workflow

1. Fork repositori / Fork the repository
2. Buat branch fitur / Create feature branch
3. Commit perubahan / Commit changes
4. Push ke branch / Push to branch
5. Buat Pull Request / Create Pull Request

## ✅ TODO (Pengembangan Lanjutan / Future Development)

### Frontend
* [ ] Implementasi PWA / PWA implementation
* [ ] Dark mode toggle / Dark mode toggle
* [ ] Optimasi gambar / Image optimization
* [ ] Peta interaktif / Interactive maps

### Backend
* [ ] Cache system dengan Redis / Redis cache system
* [ ] API endpoints untuk mobile app / API endpoints for mobile app
* [ ] Integrasi pembayaran / Payment integration
* [ ] Export data ke PDF / PDF data export

### Keamanan / Security
* [ ] Rate limiting
* [ ] OAuth integration
* [ ] HTTPS enforcement
* [ ] Security headers

## 🤝 Kontribusi / Contributing

Kami sangat menghargai kontribusi Anda! / We greatly appreciate your contributions!

1. Fork repositori / Fork the repository
2. Buat branch (`git checkout -b fitur-keren`)
3. Commit perubahan (`git commit -am 'Menambah fitur keren'`)
4. Push ke branch (`git push origin fitur-keren`)
5. Buat Pull Request

## 📄 Lisensi / License

MIT License – Bebas digunakan dan dimodifikasi / Free to use and modify

Copyright © 2025



