# 08. Misteri Sintaks: Fungsi (`fungsi()`) vs Metode (`objek.metode()`)

> Saat mulai belajar Python, banyak pemula merasa bingung ketika melihat dua bentuk pemanggilan yang berbeda. Mengapa menghitung panjang string menggunakan `len(nama)`, tetapi mengubah huruf menjadi kapital menggunakan `nama.upper()`? Mengapa tidak semuanya menggunakan cara yang sama?
>
> Jawabannya terletak pada perbedaan antara **fungsi (function)** dan **metode (method)**. Memahami konsep ini akan membuatmu jauh lebih mudah mempelajari Python maupun bahasa pemrograman lain yang berbasis **Object-Oriented Programming (OOP).**

---

# Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan mampu:

- Memahami perbedaan fungsi dan metode.
- Mengetahui kapan menggunakan `fungsi(objek)` dan `objek.metode()`.
- Memahami hubungan metode dengan Object-Oriented Programming (OOP).
- Mengenali contoh fungsi dan metode yang sering digunakan di Python.

---

# 1. Apa Itu Fungsi?

Fungsi (_Function_) adalah sekumpulan instruksi yang dapat dipanggil untuk melakukan suatu pekerjaan tertentu.

Python memiliki banyak **Built-in Function**, yaitu fungsi yang sudah disediakan secara langsung dan dapat digunakan tanpa perlu membuatnya sendiri.

Penulisannya menggunakan format:

```python
fungsi(objek)
```

Contohnya:

```python
len("Python")
```

atau

```python
type(100)
```

atau

```python
print("Halo")
```

---

# Analogi: Timbangan Digital

Bayangkan sebuah **timbangan digital**.

Timbangan tersebut dapat digunakan untuk menimbang berbagai macam benda:

- Beras
- Buku
- Laptop
- Buah
- Tas

Timbangan tidak peduli benda apa yang diletakkan di atasnya. Selama benda tersebut dapat ditimbang, alat tersebut tetap dapat bekerja.

Begitu pula dengan fungsi bawaan Python.

Misalnya fungsi `len()`.

Fungsi ini dapat digunakan untuk berbagai jenis objek.

```python
len("Python")
```

```python
len([1, 2, 3])
```

```python
len((10, 20))
```

```python
len({"nama": "Zidan"})
```

Seluruh contoh di atas menggunakan fungsi yang sama.

Karena sifatnya umum dan tidak terikat pada satu tipe data tertentu, penulisannya menggunakan:

```python
fungsi(objek)
```

---

# Contoh Built-in Function

Beberapa fungsi bawaan Python yang paling sering digunakan antara lain:

| Fungsi     | Kegunaan                               |
| ---------- | -------------------------------------- |
| `print()`  | Menampilkan output                     |
| `len()`    | Menghitung jumlah elemen               |
| `type()`   | Mengetahui tipe data                   |
| `min()`    | Mencari nilai terkecil                 |
| `max()`    | Mencari nilai terbesar                 |
| `sum()`    | Menjumlahkan data numerik              |
| `sorted()` | Menghasilkan data yang sudah diurutkan |

---

# 2. Apa Itu Metode?

Berbeda dengan fungsi, **Method (Metode)** adalah fungsi yang menjadi bagian dari suatu objek.

Artinya, metode hanya dimiliki oleh tipe data tertentu dan hanya dapat dipanggil melalui objek tersebut.

Penulisannya menggunakan format:

```python
objek.metode()
```

---

# Analogi: Kemampuan Bawaan

Bayangkan terdapat dua objek berikut.

```
🐶 Anjing

Kemampuan:
• menggonggong()
• berlari()
```

```
🚗 Mobil

Kemampuan:
• starter()
• belok()
```

Seekor anjing bisa menggonggong.

```text
anjing.menggonggong()
```

Tetapi mobil tidak bisa.

```text
mobil.menggonggong()
```

Begitu juga sebaliknya.

Mobil bisa dinyalakan.

```text
mobil.starter()
```

Sedangkan anjing tentu tidak memiliki kemampuan tersebut.

Kemampuan tersebut melekat pada objeknya masing-masing.

Konsep inilah yang digunakan Python pada **Method**.

---

# Contoh Method pada String

String memiliki banyak kemampuan bawaan.

Misalnya:

```python
nama = "python"

print(nama.upper())
```

Output

```text
PYTHON
```

Method `.upper()` hanya dimiliki oleh String.

Jika digunakan pada Integer:

```python
angka = 100

angka.upper()
```

Maka Python akan menghasilkan error karena Integer tidak memiliki method tersebut.

---

# Contoh Method pada List

List memiliki method yang berbeda.

Misalnya:

```python
angka = [1, 2]

angka.append(3)

print(angka)
```

Output

```text
[1, 2, 3]
```

Method `.append()` hanya tersedia pada List.

Jika digunakan pada String:

```python
teks = "Python"

teks.append("!")
```

Maka akan muncul error.

Karena String tidak memiliki kemampuan `append()`.

---

# 3. Mengapa Penulisannya Berbeda?

Perhatikan dua contoh berikut.

## Fungsi

```python
len(nama)
```

Artinya:

> Gunakan fungsi **len()** untuk menghitung objek **nama**.

---

### Method

```python
nama.upper()
```

Artinya:

> Minta objek **nama** menjalankan kemampuan **upper()** miliknya sendiri.

Perbedaannya sangat sederhana.

- Fungsi menerima objek sebagai **parameter**.
- Method dijalankan langsung oleh **objek**.

---

# Contoh Perbandingan

## Menghitung Panjang String

```python
nama = "Python"

print(len(nama))
```

Output

```text
6
```

Karena `len()` adalah fungsi.

---

## Mengubah Huruf Menjadi Kapital

```python
nama = "Python"

print(nama.upper())
```

Output

```text
PYTHON
```

Karena `upper()` adalah method milik String.

---

## Menghapus Spasi

```python
nama = "   Python   "

print(nama.strip())
```

Output

```text
Python
```

Method `strip()` juga hanya dimiliki oleh String.

---

## Menambah Elemen List

```python
angka = [1, 2]

angka.append(3)
```

Method `append()` hanya dimiliki oleh List.

---

# 4. Fungsi dan Method Tidak Selalu Bisa Dipertukarkan

Misalnya:

Kode berikut **benar**.

```python
len("Python")
```

Tetapi ini salah.

```python
"Python".len()
```

Karena String memang tidak memiliki method `len()`.

---

Sebaliknya.

Kode berikut benar.

```python
"python".upper()
```

Tetapi ini salah.

```python
upper("python")
```

Karena Python tidak memiliki fungsi bawaan bernama `upper()`.

---

# 5. Hubungan dengan Object-Oriented Programming (OOP)

Python merupakan bahasa pemrograman yang mendukung paradigma **Object-Oriented Programming (OOP)**.

Dalam OOP, hampir semua data dianggap sebagai **objek**.

Setiap objek memiliki:

- Data (Attribute)
- Kemampuan (Method)

Sebagai contoh:

```
String

Data:
"Python"

Method:
.upper()
.lower()
.strip()
.split()
.replace()
```

Sedangkan List memiliki kumpulan method yang berbeda.

```
List

Data:
[1, 2, 3]

Method:
.append()
.remove()
.sort()
.reverse()
.pop()
```

Karena setiap tipe data memiliki kemampuan yang berbeda, maka setiap objek juga memiliki method yang berbeda pula.

---

# Ringkasan Perbedaan

| Fungsi                                  | Method                                     |
| --------------------------------------- | ------------------------------------------ |
| Berdiri sendiri                         | Menjadi bagian dari objek                  |
| Ditulis `fungsi(objek)`                 | Ditulis `objek.metode()`                   |
| Dapat digunakan pada berbagai tipe data | Hanya dimiliki tipe data tertentu          |
| Bersifat umum                           | Bersifat spesifik                          |
| Contoh: `len()`, `type()`, `print()`    | Contoh: `.upper()`, `.append()`, `.sort()` |

---

# Cara Mudah Mengingat

Bayangkan dua situasi berikut.

## Fungsi

```
🔧 Alat dari luar
        │
        ▼
fungsi(objek)
```

Objek dimasukkan ke dalam alat agar diproses.

Contoh:

```python
len(data)
```

---

### Method

```
📦 Objek
 ├── kemampuan 1
 ├── kemampuan 2
 └── kemampuan 3
```

Objek sudah memiliki kemampuan bawaan.

Tinggal dipanggil.

```python
data.upper()
```

atau

```python
data.append(10)
```

---

# Kesimpulan

Pada materi ini kita telah mempelajari bahwa:

- **Function (Fungsi)** adalah sekumpulan instruksi yang berdiri sendiri dan digunakan melalui sintaks `fungsi(objek)`.
- **Method (Metode)** adalah fungsi yang dimiliki oleh suatu objek dan dipanggil menggunakan sintaks `objek.metode()`.
- Fungsi bersifat umum sehingga dapat digunakan pada berbagai tipe data.
- Method bersifat khusus karena hanya dimiliki oleh tipe data tertentu.
- Memahami perbedaan fungsi dan method akan mempermudah proses belajar Python, terutama saat memasuki materi **Object-Oriented Programming (OOP)**.

Dengan memahami konsep ini, kamu tidak lagi perlu menghafal sintaks satu per satu. Cukup tanyakan pada diri sendiri:

> **"Apakah ini merupakan alat umum yang bisa digunakan untuk banyak objek?"** → Gunakan **Function**.

> **"Apakah ini merupakan kemampuan bawaan dari objek tertentu?"** → Gunakan **Method**.
