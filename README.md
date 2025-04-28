# 🛍️ TechVision - Katalog Produk Elektronik Premium 🚀

## 📋 Deskripsi Proyek

TechVision adalah website katalog produk elektronik premium yang dibangun menggunakan framework Django. Website ini menampilkan berbagai produk elektronik dengan tampilan modern dan responsif, memudahkan pengguna untuk menjelajahi dan menemukan produk yang sesuai dengan kebutuhan mereka.

## ✨ Fitur

- 🏠 **Homepage** - Menampilkan landing page dengan pengenalan produk dan fitur unggulan
- 📱 **Katalog Produk** - Menampilkan daftar lengkap produk elektronik dengan filter dan pencarian
- 🔍 **Detail Produk** - Informasi lengkap tentang produk tertentu dengan spesifikasi dan fitur
- ℹ️ **Tentang Kami** - Informasi tentang perusahaan, visi & misi, sejarah, dan tim kami
- 📞 **Kontak** - Form kontak, informasi kontak, dan FAQ

## 🛠️ Teknologi yang Digunakan

- **Framework**: Django 5.2
- **Frontend**: HTML, CSS (dengan pendekatan modern)
- **Database**: SQLite (default Django)
- **Font**: Poppins (Google Fonts)
- **Responsif**: Mobile-friendly dengan media queries
- **Icons**: Emoji dan Unicode icons

## 🔧 Instalasi dan Penggunaan

### Prasyarat

- Python 3.x
- pip (Python package manager)

### Langkah Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/Athrayyanmuhmd/Tugas7_Praktikum_PPL.git
   cd katalog_produk
   ```

2. **Buat dan aktifkan virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Jalankan migrasi database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Jalankan server development**
   ```bash
   python manage.py runserver
   ```

6. **Akses website**
   - Buka browser dan akses: `http://127.0.0.1:8000/`

## 📁 Struktur Proyek

```
katalog_produk/
├── katalog_produk/         # Konfigurasi proyek
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py             # URL utama
│   └── wsgi.py
├── produk/                 # Aplikasi produk
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py           # Model data
│   ├── tests.py
│   ├── urls.py             # URL produk
│   └── views.py            # Function-based views
└── manage.py
```

## 📋 Function-Based Views

| URL | View Function | Deskripsi |
|-----|---------------|-----------|
| `/` | `home()` | Halaman utama website |
| `/produk/` | `daftar_produk_view()` | Daftar semua produk |
| `/produk/<id>/` | `detail_produk()` | Detail produk tertentu |
| `/tentang/` | `tentang_kami()` | Informasi tentang perusahaan |
| `/kontak/` | `kontak()` | Formulir kontak dan informasi |

## 📄 Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail.

## 🙏 Acknowledgments

- Django Team untuk framework yang luar biasa
- Google Fonts untuk font Poppins
- Placeholder.com untuk gambar placeholder

---
