# 01. Konsep Percabangan & Alur Kontrol Keputusan

> Sampai sejauh ini, program yang kita buat selalu berjalan **secara berurutan (sekuensial)**, yaitu dari baris pertama hingga baris terakhir. Namun, program di dunia nyata harus mampu **mengambil keputusan** berdasarkan kondisi tertentu.
>
> Misalnya:
>
> - Apakah pengguna sudah login?
> - Apakah nilai siswa sudah mencapai batas kelulusan?
> - Apakah saldo rekening mencukupi?
> - Apakah stok barang masih tersedia?
>
> Untuk menangani situasi seperti inilah Python menyediakan **percabangan (branching)** atau **alur kontrol keputusan (decision control flow)**.

---

# Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan mampu:

- Memahami konsep percabangan dalam pemrograman.
- Menggunakan statement `if`, `elif`, dan `else`.
- Mengetahui bagaimana Python mengevaluasi kondisi.
- Memahami penggunaan **Ternary Operator**.
- Mengetahui perbedaan percabangan biasa dan percabangan satu baris.

---

# 1. Apa Itu Percabangan?

Percabangan (**Branching**) adalah mekanisme yang memungkinkan program memilih jalur eksekusi berdasarkan suatu kondisi.

Program akan mengevaluasi sebuah kondisi menjadi nilai:

- `True`
- `False`

Kemudian menentukan blok kode mana yang harus dijalankan.

---

# Analogi: Gerbang Keamanan Otomatis

Bayangkan sebuah gedung memiliki sistem keamanan otomatis.

Ketika seseorang datang, sistem akan melakukan pemeriksaan.

```
Apakah memiliki Kartu VIP?
        │
   ┌────┴────┐
   │         │
 Ya         Tidak
   │         │
   ▼         ▼
Buka      Cek Kartu Staff
Pintu          │
          ┌────┴────┐
          │         │
         Ya       Tidak
          │         │
          ▼         ▼
     Buka Pintu   Aktifkan Alarm
```

Sistem tidak menjalankan semua tindakan sekaligus.

Sistem hanya menjalankan tindakan yang sesuai dengan kondisi yang terpenuhi.

Begitu pula cara kerja percabangan dalam Python.

---

# 2. Mengapa Percabangan Dibutuhkan?

Tanpa percabangan, program hanya mampu menjalankan instruksi secara lurus.

Contohnya:

```python
print("Program Dimulai")

print("Program Berjalan")

print("Program Selesai")
```

Program tersebut akan selalu menghasilkan output yang sama.

Namun bagaimana jika kita ingin membuat program seperti berikut?

- Jika nilai ≥ 75 → Lulus
- Jika nilai < 75 → Tidak Lulus

Program membutuhkan kemampuan untuk memilih.

Di sinilah percabangan digunakan.

---

# 3. Struktur Percabangan di Python

Python menyediakan tiga statement utama.

- `if`
- `elif`
- `else`

Ketiganya bekerja sama untuk mengatur jalannya program.

---

# A. Statement `if`

Statement `if` digunakan untuk memeriksa suatu kondisi.

Sintaks dasar:

```python
if kondisi:
    perintah
```

Jika kondisi bernilai `True`, maka blok di dalam `if` akan dijalankan.

Jika bernilai `False`, blok tersebut akan dilewati.

---

## Contoh

```python
nilai = 90

if nilai >= 75:
    print("Lulus")
```

Output

```text
Lulus
```

Karena kondisi:

```python
90 >= 75
```

bernilai `True`.

---

Jika nilai diubah menjadi:

```python
nilai = 60
```

Maka output:

```text
(tidak ada)
```

Karena kondisi bernilai `False`.

---

# B. Statement `else`

`else` digunakan sebagai alternatif ketika kondisi pada `if` tidak terpenuhi.

Sintaks:

```python
if kondisi:
    ...
else:
    ...
```

Contoh:

```python
nilai = 60

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
```

Output

```text
Tidak Lulus
```

Karena kondisi pada `if` bernilai `False`, maka Python menjalankan blok `else`.

---

# C. Statement `elif`

`elif` merupakan singkatan dari **Else If**.

Digunakan ketika terdapat lebih dari dua kemungkinan.

Sintaks:

```python
if kondisi_1:
    ...

elif kondisi_2:
    ...

else:
    ...
```

Python akan memeriksa kondisi satu per satu dari atas ke bawah.

Begitu menemukan kondisi yang bernilai `True`, Python langsung menjalankan blok tersebut dan mengabaikan kondisi berikutnya.

---

## Contoh

```python
nilai = 80

if nilai >= 90:
    print("Grade A")

elif nilai >= 75:
    print("Grade B")

else:
    print("Grade C")
```

Output

```text
Grade B
```

Karena:

- `nilai >= 90` → False
- `nilai >= 75` → True

Python berhenti pada kondisi kedua.

---

# Alur Kerja Percabangan

Diagram sederhananya sebagai berikut.

```text
          if
           │
     Kondisi True?
      │         │
     Ya      Tidak
      │         │
      ▼         ▼
 Jalankan     elif
  Blok          │
          Kondisi True?
           │        │
          Ya     Tidak
           │        │
           ▼        ▼
      Jalankan    else
        Blok        │
                    ▼
               Jalankan
                  Blok
```

Python hanya akan menjalankan **satu jalur** yang sesuai dengan kondisi.

---

# 4. Kondisi Menggunakan Boolean

Percabangan bekerja menggunakan nilai Boolean.

Contoh:

```python
login = True

if login:
    print("Selamat Datang")
```

Output

```text
Selamat Datang
```

Karena variabel `login` bernilai `True`.

---

Contoh lain:

```python
login = False

if login:
    print("Selamat Datang")
```

Output

```text
(tidak ada)
```

Karena kondisi bernilai `False`.

---

# 5. Ternary Operator

Kadang kita hanya ingin memilih satu dari dua nilai sederhana.

Misalnya:

- Lulus
- Tidak Lulus

Jika menggunakan `if` biasa:

```python
if nilai >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"
```

Python menyediakan bentuk yang lebih ringkas.

Sintaksnya:

```python
nilai_jika_true if kondisi else nilai_jika_false
```

---

## Contoh

```python
nilai = 85

status = "Lulus" if nilai >= 75 else "Tidak Lulus"

print(status)
```

Output

```text
Lulus
```

---

Contoh lain:

```python
umur = 16

kategori = "Dewasa" if umur >= 17 else "Anak-anak"
```

Output

```text
Anak-anak
```

---

# Kapan Menggunakan Ternary Operator?

Gunakan Ternary Operator apabila:

- Kondisinya sederhana.
- Hanya menghasilkan dua kemungkinan.
- Kode menjadi lebih ringkas tanpa mengurangi keterbacaan.

Jika kondisi sudah mulai panjang atau bertingkat, lebih baik gunakan `if` biasa agar lebih mudah dipahami.

---

# 6. Ternary Tuple (Tidak Direkomendasikan)

Pada Python versi lama terdapat teknik yang memanfaatkan Tuple.

Contoh:

```python
status = ("Gagal", "Lulus")[nilai >= 75]
```

Cara kerjanya:

- Jika kondisi `False`, indeks bernilai `0`.
- Jika kondisi `True`, indeks bernilai `1`.

Misalnya:

```python
(True)
```

akan menjadi:

```python
1
```

Sehingga Python mengambil elemen kedua.

---

## Mengapa Tidak Disarankan?

Walaupun terlihat singkat, teknik ini memiliki beberapa kekurangan.

- Sulit dipahami oleh pemula.
- Membingungkan ketika kode menjadi panjang.
- Tidak mengikuti gaya penulisan Python yang dianjurkan (*Pythonic*).
- Lebih mudah menimbulkan kesalahan ketika kondisinya kompleks.

Karena itu, komunitas Python lebih menyarankan menggunakan Ternary Operator standar.

```python
"Lulus" if nilai >= 75 else "Gagal"
```

---

# Perbandingan Percabangan

| Jenis | Digunakan Untuk |
|--------|-----------------|
| `if` | Memeriksa satu kondisi |
| `if ... else` | Memilih satu dari dua kemungkinan |
| `if ... elif ... else` | Memilih satu dari banyak kemungkinan |
| Ternary Operator | Percabangan sederhana dalam satu baris |

---

# Ringkasan Alur Percabangan

```text
Mulai
   │
   ▼
 Periksa Kondisi
   │
 ┌─┴───────────────┐
 │                 │
True             False
 │                 │
 ▼                 ▼
Blok if      Periksa elif
                   │
              ┌────┴────┐
              │         │
            True      False
              │         │
              ▼         ▼
        Blok elif   Blok else
```

---

# Kesimpulan

Pada materi ini kita telah mempelajari bahwa:

- **Percabangan (Branching)** memungkinkan program mengambil keputusan berdasarkan suatu kondisi.
- Python mengevaluasi kondisi menjadi nilai **Boolean**, yaitu `True` atau `False`.
- Statement `if` digunakan untuk memeriksa kondisi.
- Statement `elif` digunakan ketika terdapat beberapa kemungkinan kondisi.
- Statement `else` menjadi jalur terakhir jika seluruh kondisi sebelumnya tidak terpenuhi.
- **Ternary Operator** memungkinkan percabangan sederhana ditulis dalam satu baris.
- Teknik **Ternary Tuple** sebaiknya dihindari karena kurang mudah dibaca dan tidak sesuai dengan gaya penulisan Python yang direkomendasikan.

Percabangan merupakan salah satu konsep terpenting dalam pemrograman. Dengan percabangan, program tidak lagi hanya menjalankan instruksi secara berurutan, tetapi mampu **mengambil keputusan**, **merespons kondisi**, dan **menyesuaikan perilakunya sesuai data yang diterima**.