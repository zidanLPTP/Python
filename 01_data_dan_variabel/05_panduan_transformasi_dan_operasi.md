# 05. Menguasai String & Operasi Kumpulan Data

> Dalam pemrograman, data yang kita terima sering kali tidak langsung siap digunakan. Nama pengguna bisa memiliki huruf kapital yang tidak konsisten, terdapat spasi berlebih, atau bahkan format data yang berantakan. Untungnya, Python menyediakan banyak fungsi bawaan (*built-in methods*) yang memudahkan kita membersihkan, memvalidasi, dan memanipulasi data tersebut.

---

# Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan mampu:

- Memanipulasi string menggunakan berbagai method bawaan Python.
- Melakukan validasi isi string.
- Memformat tampilan teks agar lebih rapi.
- Memahami penggunaan *escape character* dan *raw string*.
- Menggunakan operasi umum pada kumpulan data.
- Melakukan teknik **Unpacking**.
- Mengurutkan data menggunakan `.sort()`.

---

# 1. Manipulasi String

String merupakan salah satu tipe data yang paling sering digunakan.

Perlu diingat bahwa **string bersifat immutable**, artinya isi string tidak dapat diubah secara langsung. Ketika sebuah method dijalankan, Python akan menghasilkan string baru tanpa mengubah string sebelumnya.

---

# A. Mengubah Huruf Besar dan Huruf Kecil

## `upper()`

Mengubah seluruh huruf menjadi huruf kapital.

```python
nama = "Python"

print(nama.upper())
```

Output

```text
PYTHON
```

---

## `lower()`

Mengubah seluruh huruf menjadi huruf kecil.

```python
nama = "PyThOn"

print(nama.lower())
```

Output

```text
python
```

---

# B. Menghapus Spasi Berlebih

Saat menerima input dari pengguna, sering kali terdapat spasi yang tidak sengaja ditambahkan.

Misalnya:

```text
"   Zidan   "
```

Python menyediakan beberapa method untuk membersihkannya.

---

## `lstrip()`

Menghapus spasi di sebelah kiri.

```python
teks = "   Python"

print(teks.lstrip())
```

Output

```text
Python
```

---

## `rstrip()`

Menghapus spasi di sebelah kanan.

```python
teks = "Python   "

print(teks.rstrip())
```

Output

```text
Python
```

---

## `strip()`

Menghapus spasi di kedua sisi.

```python
teks = "   Python   "

print(teks.strip())
```

Output

```text
Python
```

---

### Menghapus Karakter Tertentu

Selain spasi, `strip()` juga dapat menghapus karakter tertentu.

```python
kode = "###Python###"

print(kode.strip("#"))
```

Output

```text
Python
```

---

# C. Mengecek Awalan dan Akhiran

---

## `startswith()`

Memeriksa apakah string diawali teks tertentu.

```python
file = "laporan.pdf"

print(file.startswith("laporan"))
```

Output

```text
True
```

---

## `endswith()`

Memeriksa apakah string diakhiri teks tertentu.

```python
file = "laporan.pdf"

print(file.endswith(".pdf"))
```

Output

```text
True
```

Method ini sangat berguna ketika memeriksa format file, URL, atau nama dokumen.

---

# D. Memecah dan Menggabungkan String

---

## `split()`

Memecah sebuah string menjadi List.

```python
kalimat = "Belajar Python itu mudah"

hasil = kalimat.split()

print(hasil)
```

Output

```python
['Belajar', 'Python', 'itu', 'mudah']
```

Secara default, pemisahnya adalah spasi.

Kita juga dapat menentukan pemisah sendiri.

```python
data = "apel,mangga,jeruk"

print(data.split(","))
```

Output

```python
['apel', 'mangga', 'jeruk']
```

---

## `join()`

Kebalikan dari `split()`.

Method ini menggabungkan seluruh elemen List menjadi satu string.

```python
buah = [
    "Apel",
    "Mangga",
    "Jeruk"
]

print(", ".join(buah))
```

Output

```text
Apel, Mangga, Jeruk
```

---

# 2. Validasi String

Python menyediakan banyak method untuk memeriksa isi sebuah string.

Seluruh method berikut menghasilkan nilai **Boolean** (`True` atau `False`).

---

## `isupper()`

Apakah seluruh huruf kapital?

```python
print("PYTHON".isupper())
```

Output

```text
True
```

---

## `islower()`

Apakah seluruh huruf kecil?

```python
print("python".islower())
```

Output

```text
True
```

---

## `isalpha()`

Apakah hanya berisi huruf?

```python
print("Python".isalpha())
```

Output

```text
True
```

---

## `isalnum()`

Apakah hanya terdiri dari huruf dan angka?

```python
print("Python123".isalnum())
```

Output

```text
True
```

---

## `isdecimal()`

Apakah hanya berisi angka?

```python
print("2026".isdecimal())
```

Output

```text
True
```

---

## `isspace()`

Apakah seluruh isi string berupa spasi?

```python
print("   ".isspace())
```

Output

```text
True
```

---

## `istitle()`

Apakah setiap awal kata menggunakan huruf kapital?

```python
print("Belajar Python".istitle())
```

Output

```text
True
```

---

# Ringkasan Validasi String

| Method | Fungsi |
|---------|--------|
| `isupper()` | Semua huruf kapital |
| `islower()` | Semua huruf kecil |
| `isalpha()` | Hanya huruf |
| `isalnum()` | Huruf dan angka |
| `isdecimal()` | Hanya angka |
| `isspace()` | Hanya spasi |
| `istitle()` | Awal setiap kata kapital |

---

# 3. Memformat Tampilan String

Python memiliki beberapa method untuk membuat tampilan teks lebih rapi.

---

## `zfill()`

Menambahkan angka nol di depan string hingga mencapai panjang tertentu.

```python
nomor = "25"

print(nomor.zfill(5))
```

Output

```text
00025
```

Contoh penggunaan:

- Nomor antrean
- Nomor transaksi
- Kode produk

---

## `rjust()`

Membuat teks rata kanan.

```python
print("Python".rjust(12))
```

Output

```text
      Python
```

Kita juga dapat mengganti karakter pengisi.

```python
print("Python".rjust(12, "-"))
```

Output

```text
------Python
```

---

## `ljust()`

Membuat teks rata kiri.

```python
print("Python".ljust(12, "-"))
```

Output

```text
Python------
```

---

## `center()`

Membuat teks berada di tengah.

```python
print("Python".center(15, "="))
```

Output

```text
====Python====
```

---

# 4. Escape Character

Terkadang kita ingin menampilkan karakter khusus di dalam string.

Python menggunakan karakter **backslash (`\`)** sebagai penanda *escape sequence*.

---

## Petik Satu

```python
print('Hari Jum\'at')
```

Output

```text
Hari Jum'at
```

---

## Petik Dua

```python
print("Dia berkata \"Halo\"")
```

Output

```text
Dia berkata "Halo"
```

---

## Baris Baru

```python
print("Belajar\nPython")
```

Output

```text
Belajar
Python
```

---

## Tab

```python
print("Nama\t: Zidan")
```

Output

```text
Nama    : Zidan
```

---

## Backslash

```python
print("C:\\Users\\Zidan")
```

Output

```text
C:\Users\Zidan
```

---

# Raw String

Ketika bekerja dengan path folder Windows atau Regular Expression, karakter `\n` dan `\t` sering dianggap sebagai *escape character*.

Gunakan **Raw String** agar Python membaca teks apa adanya.

```python
path = r"C:\Users\Zidan\Documents"

print(path)
```

Output

```text
C:\Users\Zidan\Documents
```

Huruf `r` di depan string membuat Python mengabaikan efek *escape sequence*.

---

# 5. Operasi Umum pada Kumpulan Data

Beberapa fungsi bawaan Python dapat digunakan pada berbagai tipe data seperti:

- String
- List
- Tuple
- Set

---

## `len()`

Menghitung jumlah elemen.

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

Untuk string:

```python
print(len("Python"))
```

Output

```text
6
```

---

## `min()` dan `max()`

Mencari nilai terkecil dan terbesar.

```python
angka = [10, 3, 8, 25]

print(min(angka))
print(max(angka))
```

Output

```text
3
25
```

Pada string, perbandingan dilakukan berdasarkan urutan karakter ASCII.

---

## `count()`

Menghitung jumlah kemunculan suatu elemen.

```python
buah = [
    "Apel",
    "Jeruk",
    "Apel"
]

print(buah.count("Apel"))
```

Output

```text
2
```

Untuk string:

```python
print("banana".count("a"))
```

Output

```text
3
```

---

## Operator `in`

Memeriksa apakah suatu nilai terdapat dalam kumpulan data.

```python
buah = [
    "Apel",
    "Mangga"
]

print("Mangga" in buah)
```

Output

```text
True
```

---

## Operator `not in`

Memeriksa apakah suatu nilai **tidak** terdapat dalam kumpulan data.

```python
print("Jeruk" not in buah)
```

Output

```text
True
```

---

# 6. Unpacking

Tanpa Unpacking, kita harus mengambil data satu per satu.

```python
biodata = [
    "Budi",
    "Jakarta",
    25
]

nama = biodata[0]
kota = biodata[1]
umur = biodata[2]
```

Python menyediakan cara yang jauh lebih ringkas.

```python
nama, kota, umur = biodata
```

Sekarang isi variabel menjadi:

```text
nama = "Budi"
kota = "Jakarta"
umur = 25
```

> **Catatan:** Jumlah variabel di sebelah kiri harus sama dengan jumlah elemen pada List atau Tuple di sebelah kanan.

---

# 7. Mengurutkan Data dengan `.sort()`

Method `.sort()` digunakan untuk mengurutkan isi List secara permanen.

---

## Urutan Naik (Ascending)

```python
angka = [5, 2, 8, 1]

angka.sort()

print(angka)
```

Output

```text
[1, 2, 5, 8]
```

---

## Urutan Turun (Descending)

```python
angka.sort(reverse=True)
```

Output

```text
[8, 5, 2, 1]
```

---

# Pengurutan String dan ASCII

Saat mengurutkan string, Python menggunakan standar **ASCII (American Standard Code for Information Interchange)**.

Contoh:

```python
huruf = [
    "Z",
    "a",
    "B",
    "c"
]

huruf.sort()

print(huruf)
```

Output

```text
['B', 'Z', 'a', 'c']
```

Mengapa demikian?

Karena pada tabel ASCII, seluruh huruf kapital memiliki nilai yang lebih kecil dibandingkan huruf kecil.

---

## Mengabaikan Perbedaan Huruf Besar dan Kecil

Agar pengurutan tidak membedakan kapital dan huruf kecil, gunakan parameter `key`.

```python
huruf.sort(key=str.lower)
```

Sekarang Python akan mengurutkan berdasarkan huruf kecil sehingga hasilnya lebih natural.

---

# Ringkasan Method String

| Method | Fungsi |
|---------|--------|
| `upper()` | Mengubah menjadi huruf kapital |
| `lower()` | Mengubah menjadi huruf kecil |
| `strip()` | Menghapus spasi di kedua sisi |
| `lstrip()` | Menghapus spasi kiri |
| `rstrip()` | Menghapus spasi kanan |
| `startswith()` | Mengecek awalan |
| `endswith()` | Mengecek akhiran |
| `split()` | Memecah string menjadi List |
| `join()` | Menggabungkan List menjadi String |

---

# Kesimpulan

Pada materi ini kita telah mempelajari bahwa:

- Python menyediakan banyak method untuk memanipulasi string dengan mudah.
- String dapat dibersihkan, divalidasi, dan diformat menggunakan method bawaan.
- *Escape Character* digunakan untuk menampilkan karakter khusus di dalam string.
- *Raw String* sangat berguna ketika bekerja dengan path folder atau Regular Expression.
- Fungsi seperti `len()`, `min()`, `max()`, `count()`, serta operator `in` dan `not in` dapat digunakan pada berbagai tipe data.
- Teknik **Unpacking** membuat proses pengambilan data menjadi lebih ringkas.
- Method `.sort()` memudahkan pengurutan data baik secara menaik maupun menurun.

Materi ini menjadi bekal penting sebelum mempelajari struktur data yang lebih kompleks, pengolahan file, maupun analisis data menggunakan Python.
````
