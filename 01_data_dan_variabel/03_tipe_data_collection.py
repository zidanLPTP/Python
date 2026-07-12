# =====================================================================
# FILE: 03_tipe_data_collection.py
# DESKRIPSI: Menguasai List, Tuple, Set, dan Dictionary dengan Studi Kasus
# =====================================================================

# === 1. LIST: Fleksibel, Berurutan, & Bisa Diubah (Mutable) ===
print("=== 1. JELAJAHI LIST ===")
perlengkapan_gaming = ["Laptop", "Mouse", "Keyboard", "Headset"]
print(f"Daftar awal: {perlengkapan_gaming}")

# List bisa diubah sesuka hati (Mutable)
perlengkapan_gaming[1] = "Mouse Wireless"
print(f"Setelah diubah: {perlengkapan_gaming}")

# Slicing pada List -> pola: sequence[start:stop:step]
# start bersifat inklusif, stop bersifat eksklusif
print(f"Ambil indeks 0 sampai 2: {perlengkapan_gaming[0:3]}")
print(f"Ambil dari indeks ke-2 sampai habis: {perlengkapan_gaming[2:]}")
print(f"Ambil elemen paling terakhir: {perlengkapan_gaming[-1]}\n")


# === 2. TUPLE: Si Kaku yang Super Cepat (Immutable) ===
print("=== 2. TUPLE SI ANTI-UBAH ===")
koordinat_markas = (-6.2088, 106.8456)
print(f"Koordinat: {koordinat_markas} | Tipe: {type(koordinat_markas)}")

# Coba ubah tuple? Siap-siap ditolak!
# koordinat_markas[0] = -6.2500 # Ini bakal memicu TypeError!
print("-> Tuple aman dari perubahan data yang tidak sengaja.\n")


# === 3. SET: Himpunan Unik Tanpa Duplikat ===
print("=== 3. SET ANTI-DUPLIKAT ===")
# Kita punya data mentah ID yang double
id_peserta = {101, 102, 103, 101, 104, 102}
print(f"Isi Set otomatis bersih: {id_peserta}") # Duplikat hilang secara otomatis

# Operasi Himpunan Matematika (Union & Intersection)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Gabungan (Union): {set_a.union(set_b)}")
print(f"Irisan yang sama (Intersection): {set_a.intersection(set_b)}\n")


# === 4. DICTIONARY: Pemetaan Key-Value ===
print("=== 4. DICTIONARY STRUKTUR DATA PROFIL ===")
profil_developer = {
    "nama": "Zidan",
    "role": "Full-Stack Dev",
    "is_active": True
}
print(f"Nama Developer: {profil_developer['nama']}")

# Menambah data baru
profil_developer["bahasa_utama"] = "Python"

# Mengubah data yang ada
profil_developer["role"] = "Lead Engineer"

# Menghapus data
del profil_developer["is_active"]

print(f"Data Profil Terbaru: {profil_developer}\n")