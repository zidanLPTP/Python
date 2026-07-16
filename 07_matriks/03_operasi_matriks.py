# =====================================================================
# FILE: 03_operasi_matriks.py
# DESKRIPSI: Operasi perkalian matriks dengan konstanta
# =====================================================================

# --- 1. METODE KLASIK: PERKALIAN SKALAR DENGAN NESTED LOOP ---
print("=== 1. PERKALIAN MATRIKS DENGAN KONSTANTA (METODE KLASIK) ===")
# Skenario: Kita memiliki matriks kekuatan sinyal wifi asli berukuran 2x2.
# Kita ingin memperkuat sinyal tersebut sebanyak 3 kali lipat (Konstanta = 3).

sinyal_wifi = [
    [4, 2],  # Baris 0
    [1, 5]   # Baris 1
]

# Siapkan matriks kosong untuk menampung hasil perkalian (harus seukuran 2x2)
sinyal_diperkuat = [[0 for _ in range(2)] for _ in range(2)]

# Lakukan nested loop untuk menyisir baris dan kolom secara sekuensial
konstanta = 3

for i in range(len(sinyal_wifi)):           # Loop Baris
    for j in range(len(sinyal_wifi[0])):     # Loop Kolom
        # Kalikan setiap elemen asli dengan konstanta, simpan ke wadah baru
        sinyal_diperkuat[i][j] = sinyal_wifi[i][j] * konstanta

# Tampilkan hasil
print("Kekuatan Sinyal Asli:")
for b in sinyal_wifi:
    print(f"  {b}")

print(f"\nKekuatan Sinyal Setelah Diperkuat {konstanta}x Lipat:")
for b in sinyal_diperkuat:
    print(f"  {b}")
print()


# --- 2. METODE PREMIUM: DENGAN SIHIR NUMPY ---
print("=== 2. PERKALIAN MATRIKS DENGAN NUMPY (TANPA LOOP!) ===")
try:
    import numpy as np
    
    # Konversi list biasa menjadi array NumPy
    sinyal_np = np.array([[4, 2], [1, 5]])
    
    # Dengan NumPy, kita bisa langsung mengalikan objek layaknya angka matematika biasa!
    hasil_np = sinyal_np * 3
    
    print("Hasil Perkalian NumPy:")
    print(hasil_np)
    print("-> Sangat instan dan clean, tanpa perlu menulis nested loop!")
except ImportError:
    print("-> Note: NumPy tidak terinstall. Skenario NumPy dilewati.")
print()