# 01. Memahami Data & Rahasia Variabel di Python

> Sebelum belajar logika pemrograman, percabangan, atau perulangan, kita harus memahami satu hal paling mendasar: **data** dan **variabel**. Seluruh program yang kita buat pada akhirnya hanyalah proses mengolah data.

---

# Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan mampu:

- Memahami konsep data dalam pemrograman.
- Menjelaskan apa itu abstraksi data.
- Memahami cara kerja variabel di Python.
- Mengenal berbagai tipe data bawaan Python.
- Melakukan konversi antar tipe data (*type casting*).

---

# 1. Data: Dasar dari Semua Program

Setiap aplikasi yang kita gunakan setiap hari sebenarnya bekerja dengan **data**.

Misalnya:

- Nama pengguna
- Umur
- Nilai ujian
- Harga barang
- Status login
- Daftar teman

Komputer tidak memahami arti dari data tersebut seperti manusia. Yang dipahami komputer hanyalah representasi digital berupa angka biner (0 dan 1).

Karena itu, kita harus memberi **makna** terhadap data agar komputer mengetahui bagaimana data tersebut diproses.

---

# 2. Abstraksi Data

Bayangkan kamu melihat angka berikut.

```text
75
```

Apa artinya?

Bisa saja:

- Nilai ujian
- Berat badan
- Kecepatan kendaraan
- Jumlah pemain
- Umur seseorang

Komputer juga mengalami "kebingungan" yang sama jika tidak diberi konteks.

Sekarang perhatikan.

```text
75 kg
```

atau

```text
Nilai = 75
```

Sekarang maknanya jauh lebih jelas.

Inilah yang disebut **Abstraksi Data**.

> **Abstraksi Data** adalah proses memberikan makna atau konteks terhadap suatu data sehingga komputer mengetahui bagaimana data tersebut harus diperlakukan.

Dalam pemrograman, konteks tersebut diberikan melalui **tipe data (data type).**

---

# 3. Apa Itu Variabel?

Variabel adalah tempat untuk menyimpan data.

Bayangkan variabel seperti sebuah **kotak yang memiliki nama**.

Misalnya kita memiliki kotak bernama:

```
umur
```

Lalu kita memasukkan angka:

```
21
```

Maka dapat digambarkan seperti:

```
+--------+
| umur   |
+--------+
|   21   |
+--------+
```

Di Python, kita cukup menulis:

```python
umur = 21
```

Artinya:

- buat variabel bernama `umur`
- simpan nilai `21`

---

# 4. Python Menggunakan Dynamic Typing

Jika pernah belajar C atau C++, mungkin kamu pernah melihat kode seperti berikut.

```cpp
int umur = 21;
float tinggi = 170.5;
```

Sebelum membuat variabel, kita harus menentukan tipe datanya terlebih dahulu.

Python berbeda.

Python menggunakan **Dynamic Typing**, artinya Python akan menentukan tipe data secara otomatis berdasarkan nilai yang diberikan.

Contoh:

```python
umur = 21
```

Python langsung mengetahui bahwa:

```
umur → int
```

Contoh lainnya:

```python
nama = "Zidan"
```

Python langsung mengetahui bahwa:

```
nama → string
```

---

## Dynamic Typing

Karena tipe data ditentukan secara otomatis, tipe sebuah variabel bahkan dapat berubah.

```python
data = 10

print(data)
```

Kemudian:

```python
data = "Halo Python"

print(data)
```

Variabel yang sama sekarang berubah dari:

```
int
```

menjadi

```
str
```

Hal ini disebut **Dynamic Typing**.

---

# 5. Tipe Data di Python

Secara umum tipe data Python dibagi menjadi dua kelompok besar.

```
Tipe Data
│
├── Primitif
│
└── Collection
```

---

# A. Tipe Data Primitif

Tipe data primitif menyimpan **satu buah nilai**.

---

## Integer (int)

Integer adalah bilangan bulat.

Contoh:

```python
umur = 21
jumlah = 150
hutang = -5
```

Output:

```
21
150
-5
```

---

## Float

Float digunakan untuk menyimpan bilangan desimal.

Contoh:

```python
ipk = 3.89
phi = 3.14159
```

Output:

```
3.89
3.14159
```

---

## Complex

Python juga mendukung bilangan kompleks.

Contoh:

```python
bilangan = 2 + 3j
```

Hasil:

```
(2+3j)
```

Bilangan kompleks biasanya digunakan pada:

- matematika
- fisika
- machine learning tertentu
- simulasi ilmiah

Untuk pemrograman sehari-hari, tipe ini cukup jarang digunakan.

---

## Boolean

Boolean hanya memiliki dua nilai.

```python
True
False
```

Contoh:

```python
login = True
```

atau

```python
lulus = False
```

Boolean biasanya digunakan pada:

- percabangan (`if`)
- perulangan (`while`)
- validasi

Contoh:

```python
if login:
    print("Selamat datang")
```

---

### Truthy dan Falsy

Python memiliki konsep **Truthy** dan **Falsy**.

Beberapa nilai dianggap sebagai `False`.

Contohnya:

```python
0
```

```python
""
```

```python
[]
```

```python
{}
```

```python
None
```

Sedangkan nilai lainnya umumnya dianggap sebagai `True`.

---

## String

String adalah kumpulan karakter.

Contoh:

```python
nama = "Zidan"
```

atau

```python
kampus = 'Universitas Riau'
```

Python menerima petik satu maupun petik dua.

---

### String Multi-line

Untuk membuat teks panjang gunakan tiga tanda petik.

```python
teks = """
Belajar Python
itu menyenangkan.
"""
```

---

### String Bersifat Immutable

String tidak bisa diubah sebagian isinya.

Misalnya:

```python
nama = "Python"
```

Kemudian mencoba:

```python
nama[0] = "J"
```

akan menghasilkan error.

Karena string bersifat **Immutable**.

Jika ingin mengubah isi string, Python akan membuat objek string baru.

---

# Immutable

Beberapa tipe data di Python bersifat immutable.

Artinya nilainya tidak bisa diubah secara langsung.

Contoh:

- int
- float
- bool
- string
- tuple

Sedangkan tipe seperti List dan Dictionary bersifat mutable.

---

# B. Tipe Data Collection

Collection digunakan untuk menyimpan banyak data sekaligus.

---

## List

List adalah kumpulan data yang:

- berurutan
- boleh duplikat
- dapat diubah (mutable)

Contoh:

```python
buah = [
    "Apel",
    "Mangga",
    "Jeruk"
]
```

Output:

```
['Apel', 'Mangga', 'Jeruk']
```

---

## Tuple

Tuple hampir sama seperti List.

Perbedaannya:

- tidak dapat diubah
- lebih ringan
- lebih cepat

Contoh:

```python
koordinat = (
    -0.507,
    101.447
)
```

Biasanya digunakan untuk:

- koordinat
- data tetap
- konfigurasi

---

## Set

Set adalah kumpulan data unik.

Tidak ada indeks.

Tidak ada duplikat.

Contoh:

```python
angka = {
    1,
    2,
    3,
    3,
    2
}
```

Hasil:

```python
{1,2,3}
```

Duplikat otomatis dihapus.

---

## Dictionary

Dictionary menyimpan pasangan:

```
Key → Value
```

Contoh:

```python
mahasiswa = {
    "nama": "Zidan",
    "umur": 21,
    "kampus": "UNRI"
}
```

Visualisasinya:

```
nama    → Zidan
umur    → 21
kampus  → UNRI
```

Dictionary sangat sering digunakan karena cocok untuk menyimpan data objek.

---

# Ringkasan Collection

| Tipe | Simbol | Berurutan | Duplikat | Mutable |
|-------|---------|-----------|-----------|----------|
| List | `[]` | ✅ | ✅ | ✅ |
| Tuple | `()` | ✅ | ✅ | ❌ |
| Set | `{}` | ❌ | ❌ | ✅ |
| Dictionary | `{key:value}` | Berdasarkan key | Key unik | ✅ |

---

# 6. Mengetahui Tipe Data

Gunakan fungsi:

```python
type()
```

Contoh:

```python
umur = 21

print(type(umur))
```

Output:

```python
<class 'int'>
```

Contoh lainnya:

```python
print(type(3.14))
```

Output:

```python
<class 'float'>
```

---

# 7. Type Casting (Konversi Tipe Data)

Kadang kita perlu mengubah tipe data.

Python menyediakan berbagai fungsi bawaan.

---

## Mengubah String menjadi Integer

```python
angka = int("25")
```

Hasil:

```
25
```

---

## Mengubah Integer menjadi String

```python
teks = str(100)
```

Hasil:

```
"100"
```

---

## Mengubah Tuple menjadi List

```python
data = list((1,2,3))
```

Hasil:

```python
[1,2,3]
```

---

## Mengubah List menjadi Tuple

```python
data = tuple([1,2,3])
```

Hasil:

```python
(1,2,3)
```

---

## Mengubah List Berpasangan menjadi Dictionary

```python
data = dict([
    [1, "A"],
    [2, "B"]
])
```

Hasil:

```python
{
    1: "A",
    2: "B"
}
```

---

# Fungsi Konversi yang Sering Digunakan

| Fungsi | Kegunaan |
|----------|----------------|
| `int()` | Mengubah menjadi Integer |
| `float()` | Mengubah menjadi Float |
| `str()` | Mengubah menjadi String |
| `bool()` | Mengubah menjadi Boolean |
| `list()` | Mengubah menjadi List |
| `tuple()` | Mengubah menjadi Tuple |
| `set()` | Mengubah menjadi Set |
| `dict()` | Mengubah menjadi Dictionary |

---

# Kesimpulan

Pada materi ini kita telah mempelajari bahwa:

- Data adalah inti dari semua program.
- Abstraksi Data memberi makna terhadap data melalui tipe data.
- Variabel adalah tempat menyimpan data.
- Python menggunakan **Dynamic Typing**, sehingga tipe data ditentukan secara otomatis.
- Python memiliki dua kelompok tipe data utama:
  - **Primitif**
  - **Collection**
- Setiap tipe data memiliki karakteristik dan kegunaan masing-masing.
- Python menyediakan berbagai fungsi untuk melakukan **Type Casting**.

Materi ini menjadi pondasi penting sebelum mempelajari operasi, percabangan, perulangan, fungsi, maupun struktur data yang lebih kompleks.