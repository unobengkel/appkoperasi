# **Dokumentasi Sistem Manajemen Anggota Koperasi**

Dokumen ini berisi informasi teknis dan panduan penggunaan untuk aplikasi **Input Data Anggota** dan **Daftar Anggota Koperasi**.

## **1\. Struktur Data (Schema)**

Meskipun aplikasi ini berjalan di sisi klien (Client-side) menggunakan JavaScript, data dikelola dengan struktur objek JSON sebagai berikut:

| Nama Field | Tipe Data | Deskripsi |
| :---- | :---- | :---- |
| no | Number | ID unik anggota (auto-increment/generated) |
| nama | String | Nama lengkap anggota |
| tglLahir | Date/String | Tanggal lahir (format: YYYY-MM-DD) |
| umur | String | Hasil kalkulasi otomatis (contoh: "25 Tahun") |
| alamat | String | Alamat lengkap domisili anggota |
| telp | String | Nomor telepon aktif |
| status | String | Status verifikasi (Tunggu, Success, Gagal) |

## **2\. Informasi Form**

### **A. Form Input Data (Halaman Input)**

Form ini digunakan untuk mendaftarkan anggota baru ke dalam sistem.

* **Kalkulasi Otomatis**: Input "Umur" tidak dapat diisi manual; sistem akan menghitung umur berdasarkan "Tanggal Lahir" yang dipilih.  
* **Mode Interaktif**: Form ini memiliki dua mode:  
  1. **Mode Tambah**: Tombol "Simpan" & "Clear".  
  2. **Mode Edit**: Tombol "Update", "Reset", dan "Cancel".

### **B. Form Detail & Aksi (Modal Daftar)**

Muncul saat baris pada tabel daftar anggota diklik. Form ini memungkinkan pengguna untuk melihat detail lengkap serta melakukan perubahan atau penghapusan data.

## **3\. Tutorial Penggunaan**

### **Panduan Halaman Input Anggota**

1. **Mengisi Data**: Masukkan Nama, Alamat, dan Nomor Telepon.  
2. **Memilih Tanggal Lahir**: Klik pada kolom tanggal lahir. Setelah dipilih, kolom **Umur** akan terisi secara otomatis.  
3. **Menyimpan Data**: Klik tombol **Simpan**. Data akan muncul di tabel bagian bawah.  
4. **Mengedit Data via Tabel**:  
   * Klik pada baris data di tabel bawah.  
   * Pilih opsi **Edit** pada pop-up yang muncul.  
   * Data akan naik kembali ke form atas. Tekan **Update** untuk menyimpan perubahan.  
5. **Membatalkan Simpanan**: Klik baris tabel, lalu pilih **Batalkan Penyimpanan** untuk menghapus data.

### **Panduan Halaman Daftar Anggota**

1. **Mencari Anggota**:  
   * Ketik nama anggota pada kolom pencarian yang lebar di panel atas.  
   * Klik tombol **Cari**. Tabel akan memfilter data sesuai nama.  
2. **Menampilkan Semua Data**: Klik tombol **Semua** untuk mereset filter pencarian.  
3. **Mencetak ke Excel**:  
   * Klik tombol **Cetak Excel** (warna hijau) di dalam panel aksi.  
   * File .xlsx akan terunduh secara otomatis berisi data yang saat ini tampil di tabel.  
4. **Navigasi Data (Pagination)**:  
   * Gunakan tombol **Sebelumnya** dan **Selanjutnya** di bawah tabel jika data anggota lebih dari 10 orang.  
   * Gunakan *scroll bar* pada tabel jika tampilan data sangat panjang.  
5. **Manajemen Anggota via Modal**:  
   * Klik pada baris anggota di tabel.  
   * Akan muncul modal (pop-up) dengan informasi lengkap.  
   * **Edit**: Ubah data langsung di dalam modal lalu tekan tombol "Edit".  
   * **Delete**: Tekan tombol "Delete" untuk menghapus permanen.  
   * **Reset**: Mengembalikan isian modal ke data asli sebelum diubah.  
   * **Batal**: Menutup modal tanpa menyimpan perubahan.

## **4\. Teknologi yang Digunakan**

* **HTML5 & Tailwind CSS**: Untuk struktur dan desain responsif.  
* **Vanilla JavaScript**: Untuk logika aplikasi, kalkulasi umur, dan manajemen data.  
* **SheetJS (XLSX)**: Untuk fungsi ekspor data ke format Excel.