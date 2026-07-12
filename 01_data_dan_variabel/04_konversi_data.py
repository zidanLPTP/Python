# =====================================================================
# FILE: 04_konversi_data.py
# DESKRIPSI: Praktek merubah jenis data!
# =====================================================================

print("=== 1. EKSPERIMEN KONVERSI DATA ===")
# Dari Angka ke Teks & sebaliknya
angka_bulat = 45
teks_angka = "75.5"

print(f"Int ke Float : {float(angka_bulat)}")
print(f"Teks ke Float: {float(teks_angka)}")
print(f"Float ke Int : {int(75.9)} (Ingat! Pembulatan ke bawah, bukan dibulatkan ke terdekat)\n")

# Konversi Kumpulan Data
kata = "VOLI"
print(f"String ke List : {list(kata)}")

# Konversi List Berpasangan menjadi Dictionary
data_mentah = [["nama", "Zidan"], ["divisi", "Media Kreatif"]]
kamus_data = dict(data_mentah)
print(f"Hasil konversi ke Dictionary: {kamus_data}\n")

