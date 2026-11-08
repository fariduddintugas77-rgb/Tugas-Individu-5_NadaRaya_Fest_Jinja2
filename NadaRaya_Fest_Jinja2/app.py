from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Data contoh festival dan tiket (bukan transaksi/pembayaran sungguhan)
TIKET = [
    {"id": 1, "nama": "Early Bird", "kategori": "Festival Pass", "harga": 175000, "kuota": 500,
     "deskripsi": "Akses festival satu hari dengan harga presale."},
    {"id": 2, "nama": "Regular Pass", "kategori": "Festival Pass", "harga": 250000, "kuota": 1200,
     "deskripsi": "Akses festival satu hari untuk menikmati seluruh panggung."},
    {"id": 3, "nama": "Weekend Pass", "kategori": "2-Day Pass", "harga": 425000, "kuota": 600,
     "deskripsi": "Akses dua hari festival dengan satu tiket."},
    {"id": 4, "nama": "VIP Experience", "kategori": "VIP", "harga": 650000, "kuota": 150,
     "deskripsi": "Area menonton khusus dan jalur masuk prioritas."}
]
USERNAME_TERDAFTAR = ["farid", "andhika", "kholil"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tentang")
def tentang():
    return render_template("tentang.html")

@app.route("/tiket")
def tiket():
    return render_template("tiket.html", tiket=TIKET)

@app.route("/tiket/<int:id>")
def detail_tiket(id):
    item = next((t for t in TIKET if t["id"] == id), None)
    if item is None:
        return render_template("404.html"), 404
    return render_template("detail_tiket.html", item=item)

@app.route("/kontak")
def kontak():
    return render_template("kontak.html")

@app.route("/cek", methods=["GET", "POST"])
def cek_username():
    username = ""
    hasil = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if not re.fullmatch(r"[A-Za-z0-9_]{4,20}", username):
            hasil = "tidak_valid"
        elif username.lower() in USERNAME_TERDAFTAR:
            hasil = "dipakai"
        else:
            hasil = "tersedia"
    return render_template("cek.html", username=username, hasil=hasil)

@app.route("/pesan", methods=["GET", "POST"])
def pesan():
    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        jenis_tiket = request.form.get("jenis_tiket", "").strip()
        jumlah = request.form.get("jumlah", "1")
        if not nama or not jumlah.isdigit() or int(jumlah) < 1:
            return render_template("pesan.html", error="Lengkapi nama dan jumlah tiket dengan benar.")
        return redirect(url_for("konfirmasi", nama=nama, jenis_tiket=jenis_tiket, jumlah=int(jumlah)))
    return render_template("pesan.html", error=None)

@app.route("/konfirmasi/<nama>/<jenis_tiket>/<int:jumlah>")
def konfirmasi(nama, jenis_tiket, jumlah):
    return render_template("konfirmasi.html", nama=nama, jenis_tiket=jenis_tiket, jumlah=jumlah)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
