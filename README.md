# Short Link m.id (https://m.id)

Proyek ini adalah replika presisi tinggi, modern, responsif, dan interaktif dari platform **m.id** — platform pemendek tautan, bio link microsite, dan QR Code dinamis terlengkap di Indonesia dengan domain terpendek `m.id`.

Proyek ini dilengkapi dengan **mesin pengalihan langsung (Live Redirection Engine)** sehingga short link yang dibuat benar-benar dapat diakses dan langsung mengalihkan pengunjung ke URL tujuan asli melalui HTTP 302 Found.

---

## 🚀 Fitur Interaktif Utama

1. **Alat Pemendek Link (URL Shortener & Live Redirection)**
   - Input tautan panjang (misal WhatsApp, Shopee, Google Form, YouTube).
   - Opsi kustomisasi alias menjadi format `https://m.id/custom` (contoh: `m.id/custom`, `m.id/promo-kopi`, `m.id/myrepo`).
   - Tombol **Buka Tautan ↗ (Test Redirect)**: Menguji langsung pengalihan link ke URL target asli.
   - Tombol **Salin Link** (animasi toast clipboard).
   - Tombol **+1 Klik** untuk menguji simulasi analitik klik pengunjung.
   - Panel statistik real-time: kota teratas (Jakarta, Surabaya, Bandung), distribusi perangkat (Android/iOS/Desktop), dan sumber trafik.

2. **Generator QR Code Dinamis & Kustom**
   - Live rendering QR Code berbasis canvas/SVG dari alamat short link `m.id`.
   - Pilihan warna QR Code (Brand Crimson `#cc3333`, Midnight Black, Royal Blue, Forest Green).
   - Tombol **Unduh Gambar (PNG)** langsung ke perangkat lokal.
   - Pratinjau modal popup QR resolusi tinggi.

3. **Pratinjau Pembuat Microsite (Bio Link)**
   - Klaim custom username `m.id/[nama-kamu]`.
   - Pemilih tema warna: *Sunset Coral*, *Midnight Dark*, dan *Matcha Green*.
   - Simulasi mockup smartphone interaktif dengan daftar tautan media sosial dan katalog jualan.

4. **Showcase 7 Alat m.id (Bento Grid)**
   - *Microsite & bio link tanpa coding*
   - *Link pendek yang gampang diingat* (dengan data klik interaktif)
   - *QR Code dinamis yang bisa diganti link tujuannya*
   - *m.id Shop* untuk produk digital (e-book, template, preset)
   - *Tahu siapa yang klik* (Dashboard metrik & analitik)
   - *Tinggal minta ke AgentS* (AI assistant m.id)
   - *Formulir yang langsung rapi* (Integrasi tabel respons spreadsheet)

5. **Solusi Peran Pengguna (Segmented Control)**
   - `01` Kreator Konten
   - `02` UMKM & Penjual Online
   - `03` Tim Marketing
   - `04` Agensi & Freelancer
   - Transisi visual dan studi kasus dinamis.

6. **Bukti Sosial & Testimoni Terverifikasi**
   - Counter metrik: 1,9 juta+ pengguna terdaftar, 191 negara, 150 juta+ kunjungan/bulan.
   - Testimoni dari Rina Dewi Setya (Kreator), Andi Pratama (Digital Marketing), dan Mega Putri (Owner Resto).

7. **Daftar Paket Harga (Pricing Tiers)**
   - Switcher periode tagihan: **Per Bulan** vs **Ditagih Tahunan (Hemat 20%)**.
   - 5 paket: *Gratis*, *Starter*, *Pro (Paling Populer)*, *Bisnis*, dan *Ultimate*.
   - Modal **Bandingkan Tabel Fitur Lengkap** yang menampilkan matriks perbandingan mendalam.

8. **FAQ Interaktif dengan Pencarian**
   - 10 pertanyaan dan jawaban resmi seputar m.id, PANDI, legalitas, perbandingan dengan Linktree, dan keamanan SSL/TLS.
   - Filter pencarian cepat untuk menemukan jawaban secara instan.

9. **Alasan Alih Bahasa (ID ⟷ EN)**
   - Tombol alih bahasa di header dan footer yang mengubah seluruh konten halaman secara real-time antara Bahasa Indonesia dan Bahasa Inggris.

10. **Chatbot Mengambang AgentS AI**
    - Tombol chat di sudut kanan bawah untuk berinteraksi langsung dengan AgentS AI.
    - Dilengkapi pertanyaan cepat (prompt chips) dan respons cerdas simulasi AI m.id.

11. **Modal Masuk & Daftar Akun**
    - Formulir otentikasi interaktif (Login, Register, simulasi Google Sign-in).

---

## ⚡ Mesin Pengalihan Short Link (Live Redirection Engine)

Aplikasi ini menyertakan backend server `server.py` yang menangani pengalihan HTTP 302 Found secara real-time:

- Mengakses `http://localhost:3000/<alias>` (misal `http://localhost:3000/custom`) langsung mengembalikan:
  ```http
  HTTP/1.0 302 Found
  Location: https://shopee.co.id/toko-kopi-nusantara/promo-spesial-diskon-50
  ```
- Endpoint REST API:
  - `POST /api/shorten`: Menambahkan link baru ke basis data `links.json`.
  - `POST /api/click`: Menambah hitungan klik analitik untuk alias tertentu.
  - `GET /api/links`: Mengambil semua daftar link aktif.

---

## 📁 Struktur Direktori

```
/home/antigravity/
├── index.html            # Aplikasi web landing page m.id lengkap & interaktif
├── .htaccess             # Aturan Rewrite Apache untuk cPanel hosting
├── redirect.php          # Engine pengalihan HTTP 302 native PHP untuk cPanel
├── api.php               # REST API native PHP untuk pemendek link di cPanel
├── server.py             # HTTP server Python lokal dengan live 302 redirection & API
├── links.json            # Basis data short link yang aktif
├── favicon.svg           # Logo icon m.id untuk favicon browser
├── .cpanel.yml           # Konfigurasi deployment Git cPanel ke /public_html/shortlink
├── assets/               # Aset media lokal m.id
│   ├── logo.svg          # Logo resmi m.id (vector)
│   ├── logo-white.svg    # Logo putih m.id untuk footer
│   ├── partners/         # Logo resmi mitra PANDI, EID, MIDEX
│   ├── featured/         # Logo media: Detik, Antara, Tempo, Kumparan, dll.
│   ├── testimonials/     # Foto avatar pengguna terverifikasi
│   ├── bento/            # Mockup bento grid fitur
│   ├── slides/           # Mockup solusi per peran pengguna
│   └── qrcode.min.js     # Library rendering QR code lokal
└── README.md             # Dokumentasi proyek
```

---

## 🌐 Menghubungkan `m.id/linkCustom` ke Hosting `multimediatama.com`

Agar saat seseorang mengetik `m.id/linkCustom` di browser dapat sampai ke hosting Anda di `multimediatama.com` dan langsung dialihkan ke link asli:

### Metode 1: Menggunakan Domain Alias di cPanel (Jika Anda Memiliki Domain `m.id`)
1. **Arahkan DNS**: Di penyedia domain `m.id`, arahkan **A Record** `m.id` ke alamat IP server hosting `multimediatama.com`.
2. **Tambah Alias di cPanel**:
   - Masuk ke cPanel `multimediatama.com`.
   - Buka menu **Domains** atau **Aliases (Parked Domains)**.
   - Tambahkan `m.id` dengan **Document Root** mengarah ke folder instalasi aplikasi: `/home/mulw1713/public_html/shortlink`.
3. **Hasilnya**: Setiap permintaan ke `https://m.id/linkCustom` akan otomatis diproses oleh `.htaccess` dan `redirect.php`, lalu dialihkan (302 Found) ke link tujuan asli!

---

### Metode 2: Menggunakan Subdomain Pendek Gratis (`m.multimediatama.com`)
Jika domain 2-huruf `m.id` bukan milik Anda (karena registry PANDI / premium):
1. Masuk ke cPanel `multimediatama.com`.
2. Buka menu **Subdomains**, buat subdomain baru: `m.multimediatama.com`.
3. Atur Document Root-nya ke: `/public_html/shortlink`.
4. **Hasilnya**: Anda memiliki pemendek link super singkat `m.multimediatama.com/linkCustom` yang 100% gratis, resmi milik Anda, dan langsung bekerja di seluruh dunia!

---

### Metode 3: URL Langsung Hosting (`multimediatama.com/shortlink/linkCustom`)
Aplikasi ini sudah dilengkapi `.htaccess` dan `redirect.php`:
- Mengakses `https://multimediatama.com/shortlink/custom` langsung mengalihkan ke target URL via HTTP 302.
- Mengakses `https://multimediatama.com/shortlink/?m=custom` juga langsung mengalihkan secara instan via browser resolver.

---

## 💻 Cara Menjalankan Secara Lokal

Jalankan server python lokal:

```bash
python3 server.py
```

Buka browser di:
- **Landing Page**: `http://localhost:3000`
- **Uji Short Link**: `http://localhost:3000/custom` (langsung mengalihkan ke halaman target)
- **Cek Alias via Curl**: `curl -I http://localhost:3000/custom`

