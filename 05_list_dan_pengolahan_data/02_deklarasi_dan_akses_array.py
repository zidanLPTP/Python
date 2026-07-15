# =====================================================================
# FILE: 02_deklarasi_dan_akses_array.py
# DESKRIPSI: Praktek deklarasi array (List vs Modul Array) & Nilai Default
# =====================================================================

import array as arr

# --- 1. CARA KLASIK: SIMULASI VARIABEL INDEPENDEN VS LIST ---
print("=== 1. SKENARIO VARIABEL MANUAL VS LIST ===")
# Bayangkan merekap skor tim e-sport "Cyber Nusantara" dengan variabel satu per satu:
skor_pemain_1 = 85
skor_pemain_2 = 90
skor_pemain_3 = 75
# ... Bayangkan jika ada 100 pemain! Kode akan sangat panjang dan kaku.

# Solusi Premium: Gunakan List Python sebagai Array!
skor_tim = [85, 90, 75, 95, 80]
print(f"Daftar Skor Tim : {skor_tim}")
print(f"Skor Pemain Ke-1 (Indeks 0): {skor_tim[0]}")
print(f"Skor Pemain Ke-3 (Indeks 2): {skor_tim[2]}\n")


print("=== 2. PEMBUKTIAN ALAMAT MEMORI (id) ===")
# Mari kita lihat apakah setiap elemen disimpan di memori yang berbeda
for i in range(len(skor_tim)):
    print(f"Elemen '{skor_tim[i]}' disimpan di alamat memori: {id(skor_tim[i])}")
print("-> Terbukti! Python mengalokasikan alamat memori unik untuk setiap elemen.\n")


print("=== 3. DEKLARASI ARRAY HOMOGEN (MODUL ARRAY) ===")
# Jika kamu benar-benar ingin membuat array kaku yang 100% homogen (seperti di C++):
# Huruf 'i' menandakan tipe data Integer (Signed Int).
array_murni = arr.array('i', [10, 20, 30, 40])
print(f"Array Murni Bawaan: {array_murni}")
print(f"Tipe Kelas        : {type(array_murni)}")

# Coba aktifkan kode di bawah ini untuk melihat error-nya secara langsung!
# array_murni.append("Tulisan") # Ini akan memicu TypeError karena array ini khusus integer!
print("-> Array murni menolak tipe data asing demi menjaga konsistensi performa.\n")


print("=== 4. MENENTUKAN NILAI DEFAULT (INITIALIZATION) ===")
# Jika kamu belum tahu nilai aslinya, sangat disarankan membuat nilai default (misal angka -1 atau 0)
# Kita gunakan teknik list comprehension untuk membuat 8 kotak bernilai default -1
nilai_default = [-1 for _ in range(8)]
print(f"Array Awal (Default) : {nilai_default}")

# Kemudian kita isi nilainya secara dinamis seiring berjalannya program
for indeks in range(8):
    nilai_default[indeks] = indeks * 10

print(f"Array Akhir (Diupdate): {nilai_default}\n")