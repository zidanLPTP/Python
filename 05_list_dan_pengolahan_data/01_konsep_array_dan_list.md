# 01. Membongkar Konsep Array vs List di Python

> Bayangkan sebuah aplikasi seperti **Spotify** yang harus menyimpan ribuan lagu dalam sebuah playlist, atau sebuah game yang harus mencatat jutaan skor pemain. Tentu akan sangat tidak praktis jika setiap data disimpan dalam variabel terpisah seperti:
>
> ```python
> lagu1
> lagu2
> lagu3
> ...
> lagu1000000
> ```
>
> Untuk mengatasi masalah tersebut, pemrogram menggunakan **Struktur Data (Data Structure)**, yaitu cara khusus untuk menyimpan dan mengelola sekumpulan data secara efisien.

---

# Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan mampu:

- Memahami apa itu struktur data.
- Membedakan struktur data linear dan non-linear.
- Menjelaskan perbedaan Array dan List.
- Memahami konsep indeks, elemen, dan panjang data.
- Mengetahui mengapa Python menggunakan List sebagai pengganti Array.

---

# 1. Apa Itu Struktur Data?

**Struktur Data (Data Structure)** adalah cara mengatur, menyimpan, dan mengelola sekumpulan data di dalam memori komputer agar data tersebut dapat diakses dan diproses dengan lebih efisien.

Tanpa struktur data, program akan sulit berkembang ketika jumlah data menjadi banyak.

Misalnya, sebuah aplikasi harus menyimpan:

- Daftar mahasiswa
- Nilai ujian
- Riwayat transaksi
- Playlist lagu
- Daftar produk

Semua data tersebut membutuhkan wadah yang mampu menyimpan banyak elemen sekaligus.

---

# Mengapa Struktur Data Penting?

Bayangkan kita ingin menyimpan nilai lima mahasiswa.

Tanpa struktur data:

```python
nilai1 = 90
nilai2 = 85
nilai3 = 78
nilai4 = 88
nilai5 = 92
```

Cara ini masih bisa digunakan jika hanya terdapat lima data.

Namun bagaimana jika jumlahnya mencapai:

- 1.000 mahasiswa?
- 100.000 pelanggan?
- 10 juta pengguna?

Pendekatan tersebut menjadi tidak efisien.

Karena itulah struktur data digunakan.

---

# 2. Jenis Struktur Data

Secara umum, struktur data dibagi menjadi dua kelompok besar.

```
Struktur Data
│
├── Linear
│
└── Non-Linear
```

---

# A. Struktur Data Linear

Pada struktur data linear, setiap elemen tersusun secara berurutan.

Visualisasinya:

```text
[Data1] → [Data2] → [Data3] → [Data4]
```

Setiap elemen memiliki urutan yang jelas.

Contoh struktur data linear:

- Array
- List
- Stack
- Queue

---

# Analogi

Bayangkan antrean di kasir.

```
Orang 1
   │
   ▼
Orang 2
   │
   ▼
Orang 3
   │
   ▼
Orang 4
```

Setiap orang memiliki posisi tertentu dalam antrean.

Begitu pula struktur data linear.

---

# B. Struktur Data Non-Linear

Pada struktur data non-linear, hubungan antar data tidak selalu berurutan.

Visualisasinya:

```text
        A
      /   \
     B     C
    / \     \
   D   E     F
```

Contoh struktur data non-linear:

- Tree
- Graph

Struktur ini sering digunakan pada:

- Sistem navigasi
- Media sosial
- Mesin pencari
- Struktur folder komputer

---

# 3. Apa Itu Array?

Array adalah struktur data yang digunakan untuk menyimpan banyak data dalam satu wadah.

Misalnya:

```text
Nilai Mahasiswa

90
85
78
88
92
```

Daripada membuat lima variabel berbeda, seluruh data dapat disimpan dalam satu kelompok.

Pada banyak bahasa pemrograman seperti:

- C
- C++
- Java

Array merupakan struktur data yang sangat penting.

---

# 4. Apa Itu List?

Di Python, struktur data yang paling sering digunakan adalah **List**.

Contohnya:

```python
nilai = [
    90,
    85,
    78,
    88,
    92
]
```

List mampu menyimpan banyak data sekaligus.

Secara konsep, List sering digunakan sebagai pengganti Array.

---

# 5. Perbedaan Array dan List

Walaupun terlihat mirip, terdapat beberapa perbedaan penting.

| Fitur | Array Tradisional | List Python |
|--------|-------------------|-------------|
| Tipe Data | Homogen | Heterogen |
| Ukuran | Tetap (Static) | Dinamis (Dynamic) |
| Penambahan Data | Sulit | Sangat mudah |
| Fleksibilitas | Rendah | Sangat tinggi |

---

# A. Keseragaman Tipe Data

Array tradisional hanya dapat menyimpan satu jenis tipe data.

Contoh pada C atau C++:

```text
[10][20][30][40]
```

Semuanya harus bertipe Integer.

Tidak boleh seperti ini:

```text
[10]["Python"][3.14]
```

Karena tipe datanya berbeda.

---

Sedangkan List Python jauh lebih fleksibel.

```python
data = [
    "Zidan",
    21,
    3.89,
    True
]
```

Output

```text
['Zidan', 21, 3.89, True]
```

Satu List dapat menyimpan berbagai tipe data sekaligus.

---

# B. Ukuran Penyimpanan

Array memiliki ukuran tetap.

Misalnya sebuah Array dibuat dengan kapasitas lima elemen.

```
[ ][ ][ ][ ][ ]
```

Maka kapasitasnya tidak dapat bertambah begitu saja.

Jika ingin menambah data, biasanya harus membuat Array baru.

---

List Python berbeda.

Ukurannya bersifat dinamis.

Misalnya:

```python
angka = [1, 2, 3]
```

Kemudian ditambah:

```python
angka.append(4)
```

Sekarang List menjadi:

```python
[1, 2, 3, 4]
```

Python secara otomatis mengatur kapasitas memorinya.

---

# C. Performa

Karena memiliki ukuran tetap dan tipe data yang seragam, Array tradisional biasanya lebih cepat.

List Python sedikit lebih lambat karena:

- ukurannya dapat berubah,
- dapat menyimpan berbagai tipe data,
- memiliki banyak fitur bawaan.

Namun, sebagai gantinya List jauh lebih mudah digunakan.

---

# Mengapa Python Menggunakan List?

Python sebenarnya juga memiliki **Array**, tetapi penggunaannya tidak seumum List.

Dalam pembelajaran dasar Python, hampir seluruh contoh menggunakan List karena:

- lebih fleksibel,
- lebih mudah dipelajari,
- memiliki banyak method bawaan,
- mampu menggantikan sebagian besar fungsi Array tradisional.

Oleh karena itu, pada materi-materi berikutnya kita akan menggunakan **List sebagai representasi Array**.

---

# 6. Komponen Penting pada Array dan List

Ada tiga istilah yang wajib dipahami.

- Indeks (Index)
- Elemen (Element)
- Panjang Data (Length)

---

# A. Indeks (Index)

Indeks adalah nomor posisi setiap elemen.

Python menggunakan **zero-based indexing**, artinya indeks dimulai dari angka **0**.

Contoh:

```python
buah = [
    "Apel",
    "Mangga",
    "Jeruk",
    "Anggur"
]
```

Visualisasinya:

| Indeks | Nilai |
|---------|--------|
| 0 | Apel |
| 1 | Mangga |
| 2 | Jeruk |
| 3 | Anggur |

Perhatikan bahwa elemen pertama berada pada indeks **0**, bukan **1**.

---

# Mengakses Data Menggunakan Indeks

Misalnya:

```python
buah = [
    "Apel",
    "Mangga",
    "Jeruk"
]

print(buah[1])
```

Output

```text
Mangga
```

Karena indeks `1` menunjuk ke elemen kedua.

---

# B. Elemen (Element)

Elemen adalah data yang tersimpan di dalam Array atau List.

Misalnya:

```python
buah = [
    "Apel",
    "Mangga",
    "Jeruk"
]
```

Elemen-elemen yang tersimpan adalah:

- Apel
- Mangga
- Jeruk

---

# C. Panjang Data (Length)

Length adalah jumlah seluruh elemen yang terdapat di dalam Array atau List.

Untuk mengetahui panjangnya digunakan fungsi:

```python
len()
```

Contoh:

```python
buah = [
    "Apel",
    "Mangga",
    "Jeruk"
]

print(len(buah))
```

Output

```text
3
```

---

# Analogi: Apartemen

Bayangkan sebuah apartemen.

```
Gedung Apartemen
│
├── Lantai 0 → Andi
├── Lantai 1 → Budi
├── Lantai 2 → Citra
├── Lantai 3 → Dimas
└── Lantai 4 → Eka
```

Dalam analogi ini:

- Gedung Apartemen → Variabel List
- Nomor Lantai → Indeks
- Penghuni → Elemen
- Jumlah Lantai → Length

Dengan mengetahui nomor lantainya, kita dapat langsung menemukan penghuni yang berada di posisi tersebut.

Konsep inilah yang digunakan oleh Array dan List.

---

# Ringkasan Perbedaan

| Konsep | Penjelasan |
|---------|------------|
| Struktur Data | Cara mengatur dan menyimpan data |
| Struktur Linear | Data tersusun secara berurutan |
| Struktur Non-Linear | Data memiliki hubungan bercabang |
| Array | Struktur data dengan ukuran tetap dan tipe data seragam |
| List | Struktur data dinamis yang sangat fleksibel |

---

# Ringkasan Istilah Penting

| Istilah | Arti |
|----------|------|
| Indeks | Nomor posisi elemen |
| Elemen | Nilai yang disimpan |
| Length | Jumlah seluruh elemen |

---

# Kesimpulan

Pada materi ini kita telah mempelajari bahwa:

- **Struktur Data** digunakan untuk mengatur dan menyimpan data agar mudah dikelola.
- Struktur data dibedakan menjadi **Linear** dan **Non-Linear**.
- **Array** merupakan struktur data klasik yang memiliki ukuran tetap dan hanya menyimpan tipe data yang seragam.
- **List** adalah struktur data bawaan Python yang lebih fleksibel karena dapat menyimpan berbagai tipe data sekaligus serta memiliki ukuran yang dinamis.
- Dalam pembelajaran Python, **List sering digunakan sebagai representasi Array** karena lebih mudah digunakan dan memiliki banyak fitur bawaan.
- Tiga konsep penting yang harus dipahami adalah **Indeks**, **Elemen**, dan **Length**, karena ketiganya menjadi dasar dalam mengakses dan mengelola data pada List.

Pemahaman mengenai Array dan List akan menjadi fondasi penting sebelum mempelajari operasi pada List, perulangan (`for`), pencarian data (*searching*), pengurutan (*sorting*), hingga struktur data yang lebih kompleks.
