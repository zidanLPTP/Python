# =====================================================================
# FILE: 02_deklarasi_dan_akses_matriks.py
# DESKRIPSI: Praktek inisialisasi matriks & teknik akses koordinat [Baris][Kolom]
# =====================================================================

import sys

# --- 1. DEKLARASI LANGSUNG DENGAN DATA NYATA ---
print("=== 1. DEKLARASI MATRIKS PETA TERRAIN GAME RPG ===")
# Skenario: Kita memetakan area permainan 3x3
# 0 = Air, 1 = Tanah, 2 = Hutan
peta_game = [
    [1, 1, 0],  # Baris 0
    [1, 2, 0],  # Baris 1
    [1, 1, 1]   # Baris 2
]

print(f"Bentuk Matriks Mentah: {peta_game}")
print("Tampilan visual peta game:")
for baris in peta_game:
    print(f"  {baris}")
print()


# --- 2. DEKLARASI MATRIKS DENGAN NILAI DEFAULT ---
print("=== 2. DEKLARASI MATRIKS DEFAULT DENGAN LIST COMPREHENSION ===")
# Misalkan kita ingin membuat grid sensor kosong berukuran 3 Baris x 4 Kolom.
# Kita isi nilai default-nya dengan angka -1 (menandakan sensor belum aktif).

# Format: [[default_val for kolom in range(m)] for baris in range(n)]
jumlah_baris = 3
jumlah_kolom = 4
grid_sensor = [[-1 for _ in range(jumlah_kolom)] for _ in range(jumlah_baris)]

print("Grid Sensor Kosong (Default -1):")
for baris in grid_sensor:
    print(f"  {baris}")
print()


# --- 3. TEKNIK AKSES KOORDINAT (DOUBLE INDEXING) ---
print("=== 3. MENGAKSES ELEMEN MATRIKS [BARIS][KOLOM] ===")
# Skenario: Papan koordinat wilayah pertahanan militer (5x5)
# Baris melambangkan koordinat Utara-Selatan, Kolom melambangkan Barat-Timur.
koordinat_radar = [
    [10, 12, 15, 18, 20],  # Baris 0
    [21, 25, 30, 28, 22],  # Baris 1
    [35, 45, 99, 40, 32],  # Baris 2 (Ada target penyusup '99'!)
    [19, 17, 15, 12, 10],  # Baris 3
    [ 8,  9,  5,  4,  2]   # Baris 4
]

# Kita ingin mendeteksi nilai target penyusup di tengah radar.
# Target '99' berada di Baris ke-3 (indeks 2), Kolom ke-3 (indeks 2).
baris_target = 2
kolom_target = 2
nilai_radar = koordinat_radar[baris_target][kolom_target]

print(f"Membaca Sektor [{baris_target}][{kolom_target}]...")
print(f"-> Target Terdeteksi! Kekuatan Sinyal: {nilai_radar}")

# Coba akses koordinat pojok kanan bawah (Baris 4, Kolom 4)
print(f"-> Sinyal pojok kanan bawah [{4}][{4}]: {koordinat_radar[4][4]}\n")


# --- 4. PEMBUKTIAN PEMBOROSAN MEMORI LIST VS NUMPY ---
print("=== 4. PEMBUKTIAN ALOKASI MEMORI ===")
try:
    import numpy as np
    
    # Kita buat matriks 3x3 yang sama persis
    matriks_list  = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriks_numpy = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Hitung estimasi bytes
    ukuran_list  = sys.getsizeof(matriks_list) * len(matriks_list)
    ukuran_numpy = matriks_numpy.size * matriks_numpy.itemsize
    
    print(f"Ukuran Matriks List biasa : {ukuran_list} bytes")
    print(f"Ukuran Matriks NumPy Array: {ukuran_numpy} bytes")
    print("-> Terbukti! NumPy mengonsumsi memori jauh lebih efisien.")
except ImportError:
    print("-> Note: NumPy belum terinstall di lingkungan ini. Lewati tes memori.")