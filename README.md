# 🏢 Koperasi Pintar - Sistem Manajemen Anggota

Aplikasi Koperasi Pintar adalah program berbasis antarmuka web (Client-Server) sederhana yang dirancang khusus untuk memenuhi kebutuhan administrasi dan manajemen data keanggotaan pada sebuah koperasi. Program ini mulanya dibangun di sisi klien secara statis, lalu dielevasi menggunakan backend Python guna menyimpan data secara asinkron (real-time) dan persisten ke dalam satu titik pusat (Database SQLite).

Proyek ini sangat ringan dan sangat cocok untuk lingkungan **pembelajaran** maupun prototipe bisnis mikro.

---

## ✨ Fitur Utama

- **Pendaftaran Interaktif & Cerdas**:
  Kolom pendaftaran yang dilengkapi kalkulasi Umur secara otomatis dari sistem berdasarkan tanggal lagir yang dipilih pengguna. Form ini juga mengaplikasikan "mode sesi" yang menjaga keamanan riwayat tampilan pendaftaran.
- **Tabel Data Asinkron (SPA View)**:
  Tampilan Master Data disuguhkan secara penuh tanpa reload menggunakan fungsi *Fetch API*, memperlihatkan status anggota secara seketika (*Tunggu*, *Success*, dan *Gagal*). 
- **Pop-Up Manajemen Data Universal**:
  Pembaruan/Pengeditan data dan eksekusi penghapusan (Delete) berada dalam satu jendela modal yang efisien di atas tabel data.
- **Pencarian In-Memory**:
  Mencari nama spesifik di kumpulan tabel yang panjang secara instan tanpa terhambat *delay* jaringan.
- **Sistem Laporan ke Excel**:
  Data anggota koperasi yang sedang Anda filter atau lihat dapat diubah dan diunduh seketika sebagai *spreadsheet* Excel (.xlsx).

---

## 🛠️ Teknologi yang Digunakan

Aplikasi ini tidak memerlukan instalasi framework frontend yang rumit (seperti React/Nodejs), melainkan dibentuk dengan arsitektur klasik namun powerful:

* **Sisi Backend (Server)**: [Python FastAPI](https://fastapi.tiangolo.com/) + Pydantic
* **Sisi Database**: SQLite (Bawaan Python standar, ringan tanpa instalasi)
* **Sisi Frontend / View**: Vanilla HTML5, CSS + JS
* **Sisi Desain Antarmuka**: [Tailwind CSS](https://tailwindcss.com/) (menggunakan CDN)
* **Plugin Klien**: SheetJS (untuk fungsionalitas cetak Excel)

---

## 🚀 Panduan Instalasi Cepat

Berikut cara menjalankan layanan server untuk Koperasi Pintar di komputer lokal Anda:

### 1. Persiapan
Pastikan Anda sudah memiliki instalasi **Python V.3.8++** di komputer Anda.

### 2. Menginstal *Library* Python Terkait
Buka Terminal / Command Prompt pada folder proyek tempat file `main.py` berada, kemudian unduh seluruh komponen server dengan satu ketikan:
```bash
pip install -r requirements.txt
```

### 3. Memulai Server
Untuk mulai mengaktifkan server pengolah data SQLite dan melayani antarmuka penggunanya, ketikkan perintah berikut:
```bash
uvicorn main:app --reload
```

### 4. Mulai Menggunakan
Anda dapat memantau atau mengelola aplikasi pada web browser dengan mengakses URL berikut:
👉 **[http://localhost:8000](http://localhost:8000)**  *(Secara otomatis akan ditujukan ke modul input data).*

---

## 📖 Ingin Panduan yang Lebih Rinci?

Di dalam aplikasi, kami telah menyertakan integrasi "Buku Panduan Web" (Bisa Anda klik pada bilah *Sidebar Menu* di bagian kiri) yang memuat berbagai metode cara menghidupkan server hingga tata cara menggunakan seluruh fitur yang tersedia per halamannya.

*Dikembangkan untuk edukasi dan kemudahan aksesibilitas tanpa kerumitan instalasi skala raksasa.*
