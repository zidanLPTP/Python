# 01. Memahami Alur Sekuensial & Cara Kerja Interpreter

> Ketika mulai belajar Python, program yang kita buat mungkin hanya terdiri dari beberapa baris kode. Namun, aplikasi nyata dapat memiliki ribuan bahkan jutaan baris kode. Lalu, bagaimana komputer mengetahui urutan menjalankan semua instruksi tersebut?
>
> Jawabannya terletak pada konsep **alur sekuensial (sequential execution)** dan cara kerja **interpreter** yang digunakan oleh Python.

---

# Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan mampu:

- Memahami konsep alur sekuensial dalam pemrograman.
- Menjelaskan bagaimana Python mengeksekusi kode.
- Memahami perbedaan Compiler dan Interpreter.
- Mengenal aturan dasar sintaks Python seperti indentasi dan *case sensitivity*.

---

# 1. Apa Itu Alur Sekuensial?

Alur **Sekuensial (Sequential Execution)** adalah proses menjalankan instruksi **secara berurutan**, dimulai dari baris pertama hingga baris terakhir.

Secara sederhana, Python akan membaca kode dari **atas ke bawah** sesuai urutan penulisannya.

Visualisasinya dapat digambarkan seperti berikut.

```text
Baris 1
   │
   ▼
Baris 2
   │
   ▼
Baris 3
   │
   ▼
Baris 4
   │
   ▼
Selesai
```

Selama tidak ada percabangan (`if`) atau perulangan (`for`, `while`), Python akan selalu mengikuti urutan tersebut.

---

# Analogi: Membuat Es Kopi Susu

Bayangkan kamu sedang mengikuti resep membuat es kopi susu.

Urutan yang benar:

1. Rebus air.
2. Seduh kopi.
3. Tambahkan susu.
4. Masukkan es batu.
5. Sajikan.

Jika ditulis dalam bentuk diagram:

```text
Rebus Air
    │
    ▼
Seduh Kopi
    │
    ▼
Tambah Susu
    │
    ▼
Masukkan Es
    │
    ▼
Selesai
```

Urutan tersebut menghasilkan minuman yang benar.

---

## Bagaimana Jika Urutannya Diacak?

Misalnya menjadi seperti ini.

1. Tuangkan sirup ke meja.
2. Masukkan es ke panci panas.
3. Rebus susu hingga habis.
4. Baru membeli kopi.

Hasilnya tentu tidak sesuai harapan.

Begitu pula dalam pemrograman.

Jika urutan instruksi diubah secara sembarangan, maka hasil program juga dapat berubah, bahkan bisa menyebabkan **error**.

---

# Contoh Program Sekuensial

```python
print("Langkah 1")
print("Langkah 2")
print("Langkah 3")
```

Output

```text
Langkah 1
Langkah 2
Langkah 3
```

Python menjalankan setiap baris sesuai urutan penulisannya.

---

# Apakah Semua Urutan Selalu Berpengaruh?

Tidak selalu.

Misalnya:

```python
print("Halo")
print("Python")
```

Ditukar menjadi:

```python
print("Python")
print("Halo")
```

Program tetap berjalan tanpa error.

Hanya saja, urutan output yang dihasilkan menjadi berbeda.

Namun pada kasus lain, urutan sangat menentukan.

Contoh:

```python
nama = "Zidan"

print(nama)
```

Program berjalan dengan baik.

Tetapi jika ditukar menjadi:

```python
print(nama)

nama = "Zidan"
```

Python akan menghasilkan error karena variabel `nama` belum dibuat saat dipanggil.

Hal ini menunjukkan bahwa urutan eksekusi merupakan bagian penting dalam pemrograman.

---

# 2. Bagaimana Komputer Menjalankan Program?

Komputer sebenarnya tidak memahami bahasa Python.

Komputer hanya memahami **bahasa mesin (Machine Code)** yang terdiri dari angka biner.

```text
0
1
0
1
1
0
```

Karena itu, diperlukan sebuah penerjemah yang mengubah kode Python menjadi bahasa yang dapat dipahami komputer.

Secara umum terdapat dua jenis penerjemah.

- Compiler
- Interpreter

---

# A. Compiler

Compiler menerjemahkan **seluruh program** terlebih dahulu sebelum dijalankan.

Alur kerjanya:

```text
Kode Program
      │
      ▼
Compiler
      │
      ▼
File Program Baru
      │
      ▼
Dijalankan
```

Jika terdapat kesalahan pada kode, program biasanya tidak dapat dijalankan sampai seluruh error diperbaiki.

---

## Analogi Compiler

Bayangkan kamu memiliki sebuah novel berbahasa Inggris.

Sebelum diberikan kepada pembaca Indonesia, novel tersebut diterjemahkan seluruhnya terlebih dahulu.

Setelah selesai diterjemahkan, barulah dicetak menjadi buku baru.

Baru kemudian buku tersebut dibaca.

Compiler bekerja dengan cara yang mirip.

---

## Bahasa yang Menggunakan Compiler

Beberapa bahasa pemrograman yang menggunakan Compiler antara lain:

- C
- C++
- Go
- Rust

Bahasa seperti Java juga menggunakan proses kompilasi ke **Bytecode**, kemudian dijalankan oleh **Java Virtual Machine (JVM)**.

---

# B. Interpreter

Interpreter bekerja dengan cara yang berbeda.

Interpreter membaca program **baris demi baris**, kemudian langsung menjalankannya.

Visualisasinya:

```text
Baris 1
   │
   ▼
Jalankan
   │
   ▼
Baris 2
   │
   ▼
Jalankan
   │
   ▼
Baris 3
```

Jika terjadi error pada suatu baris, maka proses akan berhenti tepat pada baris tersebut.

Baris sebelumnya tetap sudah dijalankan.

---

## Analogi Interpreter

Bayangkan seorang penerjemah saat konferensi internasional.

Pembicara berbicara satu kalimat.

Interpreter langsung menerjemahkan saat itu juga.

Kemudian pembicara melanjutkan kalimat berikutnya.

Proses ini berlangsung secara langsung (*real-time*).

Begitulah cara kerja Interpreter.

---

# Python Menggunakan Interpreter

Python merupakan bahasa yang dijalankan menggunakan Interpreter.

Keuntungannya antara lain:

- Dapat langsung mencoba kode tanpa perlu proses kompilasi.
- Sangat cocok untuk belajar dan bereksperimen.
- Memudahkan proses debugging.

Contoh sederhana dapat dilakukan melalui Python Interactive Shell (REPL).

```python
>>> 5 + 3
8

>>> print("Halo")
Halo
```

Hasil langsung muncul tanpa perlu membuat file program terlebih dahulu.

---

# Apa yang Terjadi Jika Ada Error?

Perhatikan contoh berikut.

```python
print("Baris 1")

print("Baris 2")

print(x)

print("Baris 4")
```

Python akan menghasilkan output:

```text
Baris 1
Baris 2
```

Kemudian muncul error.

Baris keempat tidak akan dijalankan karena Interpreter berhenti saat menemukan kesalahan.

---

# 3. Aturan Dasar Sintaks Python

Python terkenal memiliki sintaks yang sederhana dan mudah dibaca.

Hal ini sesuai dengan filosofi Python yang diperkenalkan oleh penciptanya, **Guido van Rossum**:

> *"Code is read much more often than it is written."*

Artinya, kode yang baik bukan hanya mudah ditulis, tetapi juga mudah dipahami oleh orang lain.

---

# A. Indentasi

Berbeda dengan banyak bahasa pemrograman lain yang menggunakan kurung kurawal (`{}`), Python menggunakan **indentasi** untuk menunjukkan blok kode.

Indentasi biasanya menggunakan **4 spasi**.

Contoh:

```python
if True:
    print("Halo")
```

Perhatikan bahwa baris kedua berada sedikit menjorok ke kanan.

Itulah yang disebut **indentasi**.

---

## Mengapa Indentasi Penting?

Jika indentasi salah, Python akan menghasilkan error.

Contoh:

```python
if True:
print("Halo")
```

Program di atas akan menghasilkan:

```text
IndentationError
```

Karena Python menganggap baris kedua bukan bagian dari blok `if`.

---

# Standar Indentasi

Rekomendasi yang digunakan oleh komunitas Python adalah:

- Gunakan **4 spasi**.
- Hindari mencampur Tab dan Spasi.
- Gunakan indentasi secara konsisten.

Sebagian besar editor modern seperti Visual Studio Code akan membantu mengatur indentasi secara otomatis.

---

# B. Case Sensitivity

Python membedakan huruf besar dan huruf kecil.

Artinya:

```python
nama
```

berbeda dengan

```python
Nama
```

dan berbeda pula dengan

```python
NAMA
```

Ketiga variabel tersebut dianggap sebagai variabel yang berbeda.

Contoh:

```python
nama = "Zidan"

Nama = "Python"

print(nama)

print(Nama)
```

Output

```text
Zidan
Python
```

---

# Mengapa Hal Ini Penting?

Karena kesalahan penulisan huruf kapital sering menjadi penyebab error yang sulit ditemukan.

Misalnya:

```python
Nama = "Python"

print(nama)
```

Program akan menghasilkan:

```text
NameError
```

Karena variabel `nama` belum pernah dibuat.

---

# Ringkasan Perbedaan Compiler dan Interpreter

| Compiler | Interpreter |
|-----------|-------------|
| Menerjemahkan seluruh program terlebih dahulu | Menerjemahkan satu per satu saat program berjalan |
| Error diperiksa sebelum program dijalankan | Error muncul ketika mencapai baris tersebut |
| Biasanya menghasilkan file hasil kompilasi | Tidak menghasilkan file program baru |
| Eksekusi umumnya lebih cepat | Eksekusi relatif lebih lambat namun fleksibel |

---

# Ringkasan Aturan Dasar Python

| Aturan | Penjelasan |
|---------|------------|
| Sekuensial | Program dijalankan dari atas ke bawah |
| Interpreter | Kode diterjemahkan dan dijalankan baris demi baris |
| Indentasi | Menentukan blok kode menggunakan spasi |
| Case Sensitivity | Huruf besar dan kecil dianggap berbeda |

---

# Kesimpulan

Pada materi ini kita telah mempelajari bahwa:

- Python menjalankan program secara **sekuensial**, yaitu dari baris pertama hingga baris terakhir.
- Urutan penulisan kode sangat memengaruhi hasil program.
- Python menggunakan **Interpreter**, sehingga kode diterjemahkan dan dijalankan secara bertahap.
- Jika Interpreter menemukan error, proses eksekusi akan berhenti pada baris tersebut.
- Python menggunakan **indentasi** untuk menentukan blok kode, bukan kurung kurawal.
- Python juga bersifat **case sensitive**, sehingga perbedaan huruf besar dan kecil harus diperhatikan.

Memahami cara kerja alur sekuensial dan Interpreter akan memudahkanmu dalam membaca, menulis, serta melakukan proses *debugging* ketika program mulai berkembang menjadi lebih besar dan kompleks.