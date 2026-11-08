NADARAYA FEST - PROJECT FLASK + JINJA2
========================================

STUDI KASUS:
Website demo pemesanan tiket festival musik fiktif bernama NadaRaya Fest.
Terinspirasi suasana festival musik multi-genre, bukan situs resmi Pestapora.
Tidak ada transaksi, pembayaran, atau tiket sungguhan.

CARA MENJALANKAN (Windows):
1. Extract ZIP.
2. Buka folder NadaRaya_Fest_Jinja2 di VS Code.
3. Buka Terminal.
4. (Opsional) python -m venv venv
5. Aktivasi:
   PowerShell: .\venv\Scripts\Activate.ps1
   CMD: venv\Scripts\activate.bat
6. Install: python -m pip install -r requirements.txt
7. Jalankan: python app.py
8. Buka http://127.0.0.1:5000

PENGUJIAN:
- / : Beranda
- /tentang : Tentang festival
- /tiket : Katalog tiket (Jinja2 for + filter)
- /tiket/1 : Detail tiket
- /tiket/99 : Custom 404
- /cek : Form conditional tiga kondisi
  * abc = tidak valid
  * raka = sudah dipakai
  * musikfest = tersedia
- /pesan : Form pemesanan demo; submit akan redirect ke konfirmasi
- /kontak : Informasi

EMPAT KONSEP JINJA2:
1. base.html berisi navbar/footer dan block; halaman memakai extends.
2. cek.html memakai if/elif/elif untuk 3 kondisi username.
3. tiket.html memakai for dan filter title, upper, length.
4. Link internal menggunakan url_for().

Catatan: data tiket, kuota, dan username hanyalah data contoh untuk latihan.
