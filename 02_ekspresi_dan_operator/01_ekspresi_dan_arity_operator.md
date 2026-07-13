# 01. Membongkar Misteri Ekspresi & Arity Operator

> Setelah memahami tipe data dan variabel, langkah berikutnya adalah mempelajari bagaimana data tersebut diolah. Dalam pemrograman, proses menggabungkan data dengan operator sehingga menghasilkan nilai baru disebut **ekspresi (expression)**.
>
> Hampir setiap program yang kita tulis terdiri dari ribuan ekspresi. Oleh karena itu, memahami konsep ini merupakan salah satu pondasi penting sebelum mempelajari percabangan, perulangan, maupun fungsi.

---

# Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan mampu:

- Memahami pengertian ekspresi.
- Mengenal komponen penyusun sebuah ekspresi.
- Memahami konsep **Arity Operator**.
- Membedakan ekspresi aritmetika, relasional, dan logika.
- Mengetahui bagaimana Python mengevaluasi sebuah ekspresi.

---

# 1. Apa Itu Ekspresi?

Dalam pemrograman, **Ekspresi (Expression)** adalah kombinasi dari nilai, variabel, operator, maupun fungsi yang akan dievaluasi oleh Python untuk menghasilkan **satu nilai akhir**.

Dengan kata lain, setiap ekspresi selalu memiliki hasil.

---

# Analogi: Memasak di Dapur

Bayangkan kamu sedang membuat kue.

Terdapat beberapa komponen:

- 🥚 Telur
- 🌾 Tepung
- 🧈 Mentega

Semua bahan tersebut dapat dianalogikan sebagai **Operan (Operand)**.

Kemudian kamu melakukan beberapa proses:

- Mengaduk
- Menambahkan
- Memanggang

Proses tersebut dapat dianalogikan sebagai **Operator**.

Hasil akhirnya adalah adonan atau kue yang sudah jadi.

Begitu pula dalam pemrograman.

Misalnya:

```python
10 + 5
```

Komponennya adalah:

```
10      → Operan
+
        → Operator
5       → Operan
```

Python kemudian mengevaluasi ekspresi tersebut menjadi:

```text
15
```

---

# Struktur Dasar Ekspresi

Secara sederhana, sebuah ekspresi dapat digambarkan sebagai:

```text
Operan  Operator  Operan
```

Contoh:

```python
10 + 5
```

atau

```python
stok + 20
```

atau

```python
harga * jumlah
```

Setelah dievaluasi, seluruh ekspresi tersebut akan menghasilkan **satu nilai**.

---

# 2. Komponen Penyusun Ekspresi

Sebuah ekspresi umumnya tersusun dari beberapa komponen berikut.

## Operan (Operand)

Operan adalah data yang akan diproses.

Contoh:

```python
20 + 5
```

Operannya adalah:

- 20
- 5

Operan dapat berupa:

- Konstanta

```python
10
```

- Variabel

```python
umur
```

- Hasil fungsi

```python
len(nama)
```

---

## Operator

Operator adalah simbol yang digunakan untuk melakukan operasi terhadap operan.

Contoh:

```python
+
```

```python
-
```

```python
*
```

```python
/
```

```python
>
```

```python
and
```

Operator inilah yang menentukan jenis operasi yang akan dilakukan.

---

# 3. Apa Itu Arity?

**Arity** adalah jumlah operan yang dibutuhkan oleh sebuah operator agar dapat bekerja.

Dengan kata lain, Arity menjelaskan:

> **"Berapa banyak data yang diperlukan oleh operator ini?"**

Di Python, operator umumnya dibagi menjadi dua kelompok.

- Unary Operator
- Binary Operator

---

# A. Unary Operator (Operator Uner)

Unary berasal dari kata **"uni"** yang berarti satu.

Artinya operator hanya membutuhkan **satu operan**.

Contoh:

```python
-x
```

Operator negatif (`-`) hanya bekerja pada satu angka.

Misalnya:

```python
angka = 10

print(-angka)
```

Output

```text
-10
```

---

## Operator `not`

Operator `not` digunakan untuk membalik nilai Boolean.

```python
login = True

print(not login)
```

Output

```text
False
```

Operator `not` juga termasuk Unary Operator karena hanya membutuhkan satu nilai.

---

# Operator Penugasan Singkat

Python menyediakan operator yang dapat mengubah nilai variabel secara langsung.

Contohnya:

```python
level += 1
```

Kode di atas sama dengan:

```python
level = level + 1
```

Operator serupa antara lain:

```python
+=
```

```python
-=
```

```python
*=
```

```python
/=
```

Operator ini sering disebut **Augmented Assignment Operator**.

---

# B. Binary Operator (Operator Biner)

Binary berasal dari kata **"bi"** yang berarti dua.

Artinya operator membutuhkan **dua operan**.

Contoh:

```python
10 + 5
```

atau

```python
umur > 18
```

atau

```python
nilai * 2
```

Seluruh operator tersebut membutuhkan data di sebelah kiri dan kanan.

Visualisasinya:

```text
Operan   Operator   Operan
```

Contoh:

```text
10   +   5
```

---

# Ringkasan Arity

| Jenis | Jumlah Operan | Contoh |
|--------|---------------|---------|
| Unary | 1 | `-x`, `not x` |
| Binary | 2 | `a + b`, `x > y`, `nilai * 2` |

---

# 4. Jenis-Jenis Ekspresi

Walaupun bentuknya berbeda-beda, setiap ekspresi akan menghasilkan **satu nilai**.

Nilai tersebut bisa berupa:

- Integer
- Float
- String
- Boolean
- dan sebagainya.

---

# A. Ekspresi Aritmetika

Ekspresi aritmetika menggunakan operator matematika.

Contoh:

```python
10 * 5
```

Output

```text
50
```

Contoh lainnya:

```python
20 + 15
```

Output

```text
35
```

Hasil ekspresi aritmetika biasanya berupa angka.

Operator yang umum digunakan:

```text
+
-
*
/
/
//
%
**
```

---

# B. Ekspresi Relasional

Ekspresi relasional digunakan untuk membandingkan dua nilai.

Hasil akhirnya selalu berupa Boolean.

Contoh:

```python
nilai = 90

print(nilai > 75)
```

Output

```text
True
```

Contoh lain:

```python
umur == 18
```

Output

```text
True
```

atau

```text
False
```

Operator relasional yang sering digunakan:

| Operator | Arti |
|----------|------|
| `==` | Sama dengan |
| `!=` | Tidak sama dengan |
| `>` | Lebih besar |
| `<` | Lebih kecil |
| `>=` | Lebih besar atau sama |
| `<=` | Lebih kecil atau sama |

---

# C. Ekspresi Logika

Ekspresi logika digunakan untuk menggabungkan beberapa kondisi Boolean.

Operator yang digunakan adalah:

- `and`
- `or`
- `not`

Contoh:

```python
is_login = True
is_admin = True

print(is_login and is_admin)
```

Output

```text
True
```

Operator `and` menghasilkan `True` hanya jika seluruh kondisi bernilai `True`.

---

Contoh operator `or`:

```python
True or False
```

Output

```text
True
```

Operator `or` menghasilkan `True` jika salah satu kondisi bernilai `True`.

---

Contoh operator `not`:

```python
not True
```

Output

```text
False
```

Operator `not` membalik nilai Boolean.

---

# Bagaimana Python Mengevaluasi Ekspresi?

Setiap ekspresi akan diproses oleh Python hingga menghasilkan satu nilai akhir.

Misalnya:

```python
10 + 5 * 2
```

Python tidak langsung menghitung dari kiri ke kanan.

Python mengikuti aturan prioritas operator.

Langkahnya:

```
5 × 2
```

Hasilnya:

```
10
```

Kemudian:

```
10 + 10
```

Hasil akhirnya:

```text
20
```

Artinya, satu ekspresi akan terus disederhanakan hingga menghasilkan satu nilai.

---

# Contoh Lengkap

```python
umur = 20

status = umur >= 17

print(status)
```

Proses evaluasi:

```
20 >= 17
```

↓

```
True
```

↓

```python
status = True
```

---

# Ringkasan Jenis Ekspresi

| Jenis | Menggunakan | Hasil |
|--------|-------------|--------|
| Aritmetika | `+`, `-`, `*`, `/` | Angka |
| Relasional | `>`, `<`, `==`, `!=` | Boolean |
| Logika | `and`, `or`, `not` | Boolean |

---

# Kesimpulan

Pada materi ini kita telah mempelajari bahwa:

- **Ekspresi (Expression)** adalah kombinasi data, variabel, operator, atau fungsi yang menghasilkan satu nilai.
- Sebuah ekspresi terdiri dari **operan** dan **operator**.
- **Arity** menunjukkan jumlah operan yang dibutuhkan oleh suatu operator.
- Python mengenal **Unary Operator** (1 operan) dan **Binary Operator** (2 operan).
- Berdasarkan hasil akhirnya, ekspresi dapat berupa:
  - **Ekspresi Aritmetika**
  - **Ekspresi Relasional**
  - **Ekspresi Logika**
- Python selalu mengevaluasi sebuah ekspresi hingga menghasilkan satu nilai akhir.

Memahami ekspresi adalah langkah penting sebelum mempelajari materi selanjutnya seperti **operator**, **percabangan (`if`)**, **perulangan (`for` dan `while`)**, serta **fungsi**.