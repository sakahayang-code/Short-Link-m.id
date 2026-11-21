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
├── server.py             # HTTP server dengan live 302 redirection engine & API
├── links.json            # Basis data short link yang aktif
├── favicon.svg           # Logo icon m.id untuk favicon browser
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

## 💻 Cara Menjalankan

Jalankan server python yang sudah dilengkapi mesin pengalihan:

```bash
python3 server.py
```

Buka browser di:
- **Landing Page**: `http://localhost:3000`
- **Uji Short Link**: `http://localhost:3000/custom` (langsung mengalihkan ke halaman target)
- **Cek Alias via Curl**: `curl -I http://localhost:3000/custom`
