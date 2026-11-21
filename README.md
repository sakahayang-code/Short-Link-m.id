# Replika Landing Page s.id (https://home.s.id/lo/id)

Proyek ini adalah replika presisi tinggi, modern, responsif, dan interaktif dari platform **s.id** — platform pemendek tautan, bio link microsite, dan QR Code dinamis terlengkap di Indonesia.

---

## 🚀 Fitur Interaktif Utama

1. **Alat Pemendek Link (URL Shortener)**
   - Input tautan panjang (misal WhatsApp, Shopee, Google Form, YouTube).
   - Opsi kustomisasi alias menjadi format `https://m.id/custom` (contoh: `m.id/custom`, `m.id/promo-kopi`).
   - Hasil link instan dengan tombol **Salin Link** (animasi toast clipboard).
   - Tombol **+1 Klik** untuk menguji simulasi analitik klik pengunjung.
   - Panel statistik real-time: kota teratas (Jakarta, Surabaya, Bandung), distribusi perangkat (Android/iOS/Desktop), dan sumber trafik.

2. **Generator QR Code Dinamis & Kustom**
   - Live rendering QR Code berbasis canvas/SVG.
   - Pilihan warna QR Code (Brand Crimson `#cc3333`, Midnight Black, Royal Blue, Forest Green).
   - Tombol **Unduh Gambar (PNG)** langsung ke perangkat lokal.
   - Pratinjau modal popup QR resolusi tinggi.

3. **Pratinjau Pembuat Microsite (Bio Link)**
   - Klaim custom username `s.id/[nama-kamu]`.
   - Pemilih tema warna: *Sunset Coral*, *Midnight Dark*, dan *Matcha Green*.
   - Simulasi mockup smartphone interaktif dengan daftar tautan media sosial dan katalog jualan.

4. **Showcase 7 Alat s.id (Bento Grid)**
   - *Microsite & bio link tanpa coding*
   - *Link pendek yang gampang diingat* (dengan data klik interaktif)
   - *QR Code dinamis yang bisa diganti link tujuannya*
   - *s.id Shop* untuk produk digital (e-book, template, preset)
   - *Tahu siapa yang klik* (Dashboard metrik & analitik)
   - *Tinggal minta ke AgentS* (AI assistant s.id)
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
   - 10 pertanyaan dan jawaban resmi seputar s.id, PANDI, legalitas, perbandingan dengan Linktree, dan keamanan SSL/TLS.
   - Filter pencarian cepat untuk menemukan jawaban secara instan.

9. **Alasan Alih Bahasa (ID ⟷ EN)**
   - Tombol alih bahasa di header dan footer yang mengubah seluruh konten halaman secara real-time antara Bahasa Indonesia dan Bahasa Inggris.

10. **Chatbot Mengambang AgentS AI**
    - Tombol chat di sudut kanan bawah untuk berinteraksi langsung dengan AgentS AI.
    - Dilengkapi pertanyaan cepat (prompt chips) dan respons cerdas simulasi AI s.id.

11. **Modal Masuk & Daftar Akun**
    - Formulir otentikasi interaktif (Login, Register, simulasi Google Sign-in).

---

## 📁 Struktur Direktori

```
/home/antigravity/
├── index.html            # Aplikasi web landing page s.id lengkap
├── assets/               # Aset media lokal (fallback ke CDN resmi s.id)
│   ├── partners/         # Logo resmi PANDI, EID, SIDEX
│   ├── featured/         # Logo media: Detik, Antara, Tempo, Kumparan, dll.
│   ├── testimonials/     # Foto avatar pengguna terverifikasi
│   ├── bento/            # Tangkapan layar fitur bento mockup
│   ├── slides/           # Mockup solusi per peran pengguna
│   └── qrcode.min.js     # Library rendering QR code lokal
└── README.md             # Dokumentasi proyek
```

---

## 💻 Cara Menjalankan Secara Mandiri

Aplikasi ini bersifat *zero-dependency* di sisi backend (HTML5 murni, Tailwind CSS via CDN, dan JavaScript native). Anda dapat menjalankannya dengan server HTTP apa pun:

```bash
# Menggunakan Python:
python3 -m http.server 3000

# Atau menggunakan Node.js npx:
npx serve .
```

Kemudian buka browser di `http://localhost:3000`.
