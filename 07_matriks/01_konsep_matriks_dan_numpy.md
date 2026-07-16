# 01. Membongkar Konsep Matriks (Array 2 Dimensi)

> Pada materi sebelumnya kita telah mempelajari **List** sebagai representasi **Array 1 Dimensi**, yaitu kumpulan data yang tersusun dalam satu baris. Namun, banyak permasalahan di dunia nyata membutuhkan penyimpanan data yang lebih kompleks, seperti papan catur, tabel nilai siswa, citra digital, hingga peta permainan.
>
> Untuk menyimpan data seperti itu, kita menggunakan **Array 2 Dimensi** atau yang lebih dikenal dengan **Matriks (Matrix)**.

---

# Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan mampu:

- Memahami konsep Matriks (Array 2 Dimensi).
- Membuat Matriks menggunakan **Nested List**.
- Memahami konsep baris dan kolom.
- Mengenal contoh penerapan Matriks dalam kehidupan nyata.
- Mengetahui perbedaan Matriks menggunakan List dan NumPy Array.

---

# 1. Apa Itu Matriks?

Dalam matematika, **Matriks** adalah kumpulan data yang disusun dalam bentuk **baris** (*row*) dan **kolom** (*column*).

Contoh sederhana:

```text
1  2  3
4  5  6
7  8  9
```

Matriks di atas memiliki:

- 3 baris
- 3 kolom

Setiap angka berada pada posisi tertentu yang ditentukan oleh kombinasi **baris** dan **kolom**.

---

# Matriks dalam Python

Di Python, Matriks biasanya dibuat menggunakan **Nested List**, yaitu List yang berisi List lainnya.

Contoh:

```python
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Perhatikan strukturnya.

List paling luar berisi tiga buah List.

Setiap List di dalamnya mewakili satu baris.

Visualisasinya:

```text
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

---

# Analogi: Spreadsheet Excel

Cara paling mudah memahami Matriks adalah membayangkan sebuah spreadsheet seperti Microsoft Excel atau Google Sheets.

```text
        Kolom
      0    1    2

Baris 0  A    B    C

Baris 1  D    E    F

Baris 2  G    H    I
```

Pada spreadsheet:

- Baris tersusun secara horizontal.
- Kolom tersusun secara vertikal.
- Pertemuan antara baris dan kolom menghasilkan sebuah **sel (cell)**.

Matriks bekerja dengan konsep yang sama.

---

# 2. Struktur Matriks

Misalkan terdapat Matriks berikut.

```text
[
 [10, 20, 30],
 [40, 50, 60],
 [70, 80, 90]
]
```

Visualisasinya:

| Baris | Kolom 0 | Kolom 1 | Kolom 2 |
|--------|----------|----------|----------|
| 0 | 10 | 20 | 30 |
| 1 | 40 | 50 | 60 |
| 2 | 70 | 80 | 90 |

Posisi setiap elemen ditentukan oleh:

```
(baris, kolom)
```

Misalnya:

```
50
```

berada pada:

```
(1,1)
```

karena:

- Baris = 1
- Kolom = 1

---

# Mengakses Elemen Matriks

Untuk mengambil data dari Matriks digunakan dua indeks.

Sintaks:

```python
matriks[baris][kolom]
```

Contoh:

```python
matriks = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(matriks[1][1])
```

Output

```text
50
```

Karena:

- Baris ke-1
- Kolom ke-1

berisi angka **50**.

---

# 3. Contoh Penerapan Matriks

Matriks digunakan hampir di semua bidang teknologi.

Berikut beberapa contohnya.

---

# A. Data Sensor

Bayangkan sebuah satelit cuaca yang memantau kelembapan tanah.

Wilayah dibagi menjadi beberapa titik pengamatan.

Setiap titik menyimpan hasil pengukuran.

Contoh Matriks:

```text
65.5   70.2   68.1
58.0   62.4   60.9
72.3   75.1   70.8
```

Dalam Python:

```python
sensor = [
    [65.5,70.2,68.1],
    [58.0,62.4,60.9],
    [72.3,75.1,70.8]
]
```

Setiap angka menunjukkan hasil pembacaan sensor pada koordinat tertentu.

---

# B. Peta Permainan (Tile Map)

Game 2D biasanya menggunakan Matriks untuk menyimpan jenis medan.

Misalnya:

```
0 = Air
1 = Daratan
```

Contoh:

```text
1  1  0
1  0  0
1  1  1
```

Dalam Python:

```python
map_game = [
    [1,1,0],
    [1,0,0],
    [1,1,1]
]
```

Visualisasinya:

🟩 = Daratan

🟦 = Air

```text
🟩 🟩 🟦
🟩 🟦 🟦
🟩 🟩 🟩
```

Game kemudian menggunakan Matriks tersebut untuk menentukan apakah karakter dapat berjalan pada suatu posisi.

---

# C. Nilai Siswa

Misalnya terdapat tiga siswa yang mengikuti tiga mata pelajaran.

```text
85  90  88
78  81  75
92  89  94
```

Dalam Python:

```python
nilai = [
    [85,90,88],
    [78,81,75],
    [92,89,94]
]
```

Setiap:

- Baris → Siswa
- Kolom → Mata Pelajaran

---

# D. Gambar Digital

Sebuah gambar sebenarnya merupakan kumpulan jutaan piksel.

Setiap piksel memiliki nilai warna tertentu.

Sebagai ilustrasi sederhana:

```text
255 120  30
100 255  50
 80  60 255
```

Seluruh gambar dapat dianggap sebagai Matriks yang sangat besar.

---

# 4. Matriks Menggunakan List Python

Python secara bawaan menggunakan **Nested List** untuk membuat Matriks.

Contoh:

```python
matriks = [
    [1,2],
    [3,4]
]
```

Keuntungan:

- Mudah dipahami.
- Tidak membutuhkan library tambahan.
- Cocok untuk pembelajaran.

Namun terdapat kelemahan.

---

# Mengapa List Kurang Efisien?

List Python dirancang agar sangat fleksibel.

List dapat menyimpan:

- Integer
- Float
- String
- Boolean
- Object

Karena fleksibilitas tersebut, setiap elemen sebenarnya berupa **referensi (pointer)** menuju objek lain di memori.

Visualisasi sederhananya:

```text
List

│
├──► Objek Integer
├──► Objek String
├──► Objek Float
└──► Objek Boolean
```

Akibatnya:

- penggunaan memori lebih besar,
- akses data sedikit lebih lambat,
- kurang optimal untuk data numerik berukuran besar.

---

# 5. NumPy Array

Untuk kebutuhan komputasi numerik, programmer biasanya menggunakan **NumPy (Numerical Python)**.

NumPy menyediakan struktur data bernama **ndarray (N-Dimensional Array)**.

Contoh:

```python
import numpy as np

matriks = np.array([
    [1,2,3],
    [4,5,6]
])
```

Sekilas bentuknya mirip dengan Nested List.

Namun cara penyimpanannya sangat berbeda.

---

# Mengapa NumPy Lebih Cepat?

NumPy menyimpan data secara **bersebelahan di memori (contiguous memory)**.

Visualisasinya:

```text
1 | 2 | 3 | 4 | 5 | 6
```

Karena seluruh data tersusun secara berurutan, komputer dapat membacanya jauh lebih cepat.

Selain itu, seluruh elemen memiliki tipe data yang sama (**homogen**), sehingga penggunaan memori menjadi lebih efisien.

---

# Perbandingan List dan NumPy

| List Python | NumPy Array |
|--------------|-------------|
| Fleksibel | Sangat cepat |
| Dapat menyimpan berbagai tipe data | Tipe data homogen |
| Lebih mudah digunakan | Lebih hemat memori |
| Cocok untuk pembelajaran | Cocok untuk komputasi numerik dan data besar |

---

# 6. Instalasi NumPy

Sebelum menggunakan NumPy, pastikan library tersebut telah terpasang.

## Mengecek Instalasi

```bash
pip show numpy
```

Jika informasi NumPy muncul, berarti library sudah tersedia.

---

## Menginstal NumPy

Jika belum terpasang, jalankan perintah berikut.

```bash
pip install numpy
```

Setelah proses instalasi selesai, NumPy siap digunakan pada program Python.

---

# Kapan Menggunakan List dan NumPy?

Gunakan **List** apabila:

- Sedang belajar Python.
- Data tidak terlalu besar.
- Membutuhkan fleksibilitas tipe data.

Gunakan **NumPy** apabila:

- Mengolah Matriks berukuran besar.
- Melakukan komputasi numerik.
- Mengolah citra digital.
- Machine Learning.
- Data Science.
- Artificial Intelligence.

---

# Ringkasan Istilah Penting

| Istilah | Penjelasan |
|----------|------------|
| Matriks | Array dua dimensi |
| Baris (Row) | Susunan data horizontal |
| Kolom (Column) | Susunan data vertikal |
| Cell | Pertemuan antara baris dan kolom |
| Nested List | List yang berisi List lainnya |
| NumPy | Library Python untuk komputasi numerik |

---

# Kesimpulan

Pada materi ini kita telah mempelajari bahwa:

- **Matriks** adalah kumpulan data yang disusun dalam bentuk **baris** dan **kolom**.
- Di Python, Matriks umumnya dibuat menggunakan **Nested List**, yaitu List yang berisi List lainnya.
- Setiap elemen Matriks memiliki posisi yang ditentukan oleh **baris** dan **kolom**.
- Matriks banyak digunakan pada berbagai bidang seperti pengolahan citra, game, spreadsheet, sensor, hingga analisis data.
- Untuk kebutuhan komputasi numerik yang besar, **NumPy Array** menjadi pilihan yang lebih efisien dibandingkan Nested List karena memiliki performa yang lebih tinggi dan penggunaan memori yang lebih hemat.

Materi ini akan menjadi dasar sebelum mempelajari operasi Matriks, iterasi menggunakan **nested loop**, manipulasi data dua dimensi, hingga pengolahan data menggunakan **NumPy** pada bidang Data Science dan Artificial Intelligence.