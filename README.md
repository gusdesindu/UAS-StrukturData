# DSS Relasi Sosial Media Berbasis Graph

## Nama Anggota Kelompok

- I Nyoman Gede Gata Atmaja - 
- I Komang Galang Prabawa - 
- I.B.Gede Ambara Sindu Negara - 

---

link Video Demo
https://youtu.be/OrjZbKisZbU?si=pYFR5cjkIrnZrRvp
---

## Deskripsi Project

DSS (Decision Support System) Relasi Sosial Media merupakan sistem pendukung keputusan yang memanfaatkan struktur data Graph untuk merepresentasikan hubungan antar pengguna media sosial.

Pada sistem ini, setiap pengguna direpresentasikan sebagai node (vertex), sedangkan hubungan pertemanan atau follow direpresentasikan sebagai edge. Sistem menggunakan algoritma Breadth First Search (BFS) untuk melakukan pencarian jalur hubungan antar pengguna dan memberikan rekomendasi koneksi berdasarkan relasi yang dimiliki.

Project ini dibuat sebagai implementasi nyata materi Struktur Data khususnya Graph pada studi kasus relasi sosial media.

---

## Tujuan Project

- Mengimplementasikan struktur data Graph pada kasus dunia nyata.
- Menerapkan algoritma Breadth First Search (BFS).
- Menganalisis hubungan antar pengguna media sosial.
- Menampilkan visualisasi graph secara interaktif.
- Memberikan rekomendasi koneksi berdasarkan hubungan yang ada.
- Mendukung proses pengambilan keputusan berbasis relasi sosial.

---

## Features 💡

### 👤 Kelola User
- Menambahkan pengguna baru.
- Menghapus pengguna.
- Menampilkan daftar pengguna.

### 🔗 Kelola Relasi
- Menambahkan hubungan antar pengguna.
- Menghapus hubungan.
- Menampilkan daftar relasi.

### 📊 Visualisasi Graph
- Menampilkan graph relasi sosial.
- Menampilkan node dan edge secara visual.
- Menampilkan hubungan antar pengguna.

### 🧠 Analisis Hubungan (BFS)
- Mencari jalur hubungan antar pengguna.
- Menampilkan proses BFS.
- Menampilkan node yang dikunjungi.
- Menampilkan jalur yang ditemukan.

### ⭐ Rekomendasi Teman
- Memberikan rekomendasi koneksi baru.
- Berdasarkan hubungan teman dari teman (Friend Recommendation).
- Membantu pengguna menemukan relasi potensial.

### 📈 Analisis User Populer
- Menampilkan pengguna dengan koneksi terbanyak.
- Menghitung tingkat popularitas berdasarkan jumlah hubungan.

---

## Teknologi 🕹️

- Python
- Streamlit
- NetworkX
- Matplotlib
- JSON

---

## Struktur Data Graph

### Jenis Graph

Directed Graph (Graf Berarah)

### Representasi Graph

Adjacency List

### Dataset Awal

```json
{
  "ronaldo": ["messi", "neymar"],
  "messi": ["ronaldo", "mbappe", "Miawaug"],
  "neymar": ["ronaldo"],
  "mbappe": ["messi", "Miawaug"],
  "Miawaug": ["mbappe"],
  "atmaja": ["ronaldo"],
  "gusde": ["Miawaug"],
  "Halaand": ["Miawaug"]
}
```

### Node

- ronaldo
- messi
- neymar
- mbappe
- Miawaug
- atmaja
- gusde
- Halaand

### Edge

```text
ronaldo → messi
ronaldo → neymar

messi → ronaldo
messi → mbappe
messi → Miawaug

neymar → ronaldo

mbappe → messi
mbappe → Miawaug

Miawaug → mbappe

atmaja → ronaldo

gusde → Miawaug

Halaand → Miawaug
```

---

## Algoritma yang Digunakan

### Breadth First Search (BFS)

Breadth First Search digunakan untuk:

- Mencari jalur hubungan antar pengguna.
- Menemukan koneksi terdekat.
- Menampilkan proses traversal graph.
- Mendukung sistem rekomendasi teman.

### Kompleksitas Algoritma

```text
O(V + E)
```

Keterangan:

- V = jumlah node
- E = jumlah edge

---

## Cara Kerja Sistem

### Input

Pengguna dapat:

- Menambahkan user baru.
- Menambahkan relasi.
- Memilih user asal dan tujuan.
- Menjalankan analisis BFS.

### Proses

1. Data disimpan dalam bentuk Directed Graph.
2. BFS melakukan penelusuran node secara bertingkat.
3. Sistem mencari jalur hubungan antar pengguna.
4. Sistem menampilkan node yang dikunjungi.
5. Sistem memberikan rekomendasi berdasarkan hubungan yang ada.

### Output

- Visualisasi Graph
- Jalur Hubungan
- Node yang Dikunjungi
- User Populer
- Rekomendasi Teman

---

## Contoh Pencarian Jalur

Mencari jalur dari:

```text
atmaja
```

ke:

```text
Miawaug
```

Hasil BFS:

```text
atmaja
↓
ronaldo
↓
messi
↓
Miawaug
```

Panjang Jalur:

```text
3 Hop
```

---

## Installation ⚙️

Install dependency:

```bash
pip install -r requirements.txt
```

---

## Menjalankan Program 🚀

```bash
streamlit run app.py
```

Aplikasi akan berjalan pada:

```text
http://localhost:8501
```

---

## Kesimpulan

Project DSS Relasi Sosial Media menunjukkan bahwa struktur data Graph dapat digunakan untuk merepresentasikan hubungan sosial secara efektif. Dengan algoritma Breadth First Search (BFS), sistem mampu mencari jalur hubungan antar pengguna, menganalisis konektivitas jaringan sosial, serta memberikan rekomendasi koneksi sebagai bentuk implementasi Decision Support System (DSS).
