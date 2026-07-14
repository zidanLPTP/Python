# =====================================================================
# FILE: 04_list_comprehension.py
# DESKRIPSI: Menguasai List Comprehension (Sihir Manipulasi List Kilat)
# =====================================================================

print("=== 1. KLASIK VS PREMIUM (LIST COMPREHENSION) ===")
skor_dasar = [10, 20, 30, 40, 50]

# --- Cara Klasik (Menggunakan Loop For biasa & .append) ---
skor_ganda_klasik = []
for skor in skor_dasar:
    skor_ganda_klasik.append(skor * 2)

print(f"Hasil Gaya Klasik : {skor_ganda_klasik}")


# --- Cara Premium / List Comprehension (One-Liner) ---
# Format dasar: [expression for item in iterable]
skor_ganda_premium = [skor * 2 for skor in skor_dasar]

print(f"Hasil Gaya Premium: {skor_ganda_premium}\n")


print("=== 2. LIST COMPREHENSION DENGAN FILTER (IF) ===")
# Kita hanya ingin mengambil angka genap lalu memangkatkannya dengan 2
daftar_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Format: [expression for item in iterable if condition]
pangkat_genap = [angka ** 2 for angka in daftar_angka if angka % 2 == 0]

print(f"Daftar Angka Asli : {daftar_angka}")
print(f"Hasil Pangkat Genap: {pangkat_genap}")
print("-> Keren banget, kan? Semua proses filter & transformasi selesai dalam 1 baris!")