# 🔐 Aplikasi Enkripsi ROT13 & Steganografi LSB  
> 🎓 **Project UAS Kriptografi - Kelompok 2 TI C RPL 22**

## 👥 Anggota Kelompok
| 🧑‍💻 **Anne Rufaedah** | 22104410023 |
| 👩‍💻 **Latifah Habibita Alif** | 22104410019 |
| 👩‍💻 **Heppy Indah Kumalasari** | 21104413004 |

---

## 🧩 Deskripsi Singkat
Aplikasi ini merupakan implementasi gabungan antara **algoritma enkripsi ROT13** dan **metode Steganografi LSB (Least Significant Bit)** berbasis bahasa **Python**.  
Tujuannya adalah untuk **menyembunyikan pesan rahasia di dalam file gambar** dengan terlebih dahulu mengenkripsi pesan tersebut menggunakan ROT13, lalu menampilkannya dalam antarmuka **GUI sederhana berbasis FreeSimpleGUI**.

---

## 🚀 Fitur Utama
✨ Enkripsi teks menggunakan algoritma ROT13 dan penyisipan (embed) pesan rahasia ke dalam gambar menggunakan metode LSB  
🔍 Ekstraksi pesan dari gambar yang sudah disisipi dan Dekripsi otomatis hasil ekstraksi (ROT13 → teks asli)  

---

## 🧱 Struktur Proyek (Contoh)


## ⚙️ Cara Menjalankan Program
Sebelum menjalankan aplikasi, pastikan Python sudah terinstal (minimal versi **3.10**).  

1. Clone repository ini
```bash
git clone https://github.com/username/ROT13-LSB.git
cd ROT13-LSB
```
2. Aktifkan environment
```
python -m venv env
source env/bin/activate      # di Linux/Mac
env\Scripts\activate         # di Windows
```
3. Install requirements / library yang dibutuhkan project ini
```
pip install -r requirements.txt
```
4. Jalankan aplikasi
```
python main.py
```
5. GUI akan terbuka dan menampilkan menu utama seperti berikut 👇
Kemudian, install library yang dibutuhkan dengan perintah berikut:
    - Tampilan awal program
      <img width="701" height="635" alt="image" src="https://github.com/user-attachments/assets/5cbd83ac-b040-4a88-83a0-af92de7e1fcc" />
    - Tampilan menu embed
      <img width="707" height="644" alt="gui embeded" src="https://github.com/user-attachments/assets/4b8b8eac-c43f-4018-b424-ee7dea93edfa" />
    - Tampilan menu ekstrak
      <img width="707" height="643" alt="proses ekstraksi" src="https://github.com/user-attachments/assets/ba175cb6-74a9-4a62-97b3-5dd763742613" />


## 🏁 Lisensi
Proyek ini dibuat untuk tujuan pembelajaran dan tugas akademik.
🔖 UAS Kriptografi - Universitas Islam Balitar (UNISBA)

