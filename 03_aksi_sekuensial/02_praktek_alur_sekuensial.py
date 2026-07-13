# =====================================================================
# FILE: 02_praktek_alur_sekuensial.py
# DESKRIPSI: Membuktikan alur sekuensial & efek perubahan urutan kode
# =====================================================================

print("=== SISTEM KAFE CAFFEINE-KICK (TAHUN 2026) ===")
print("Harap isi data pelanggan di bawah ini secara jujur:\n")

# Program membaca baris ini secara berurutan dari atas ke bawah
nama = input("Masukkan nama Anda         : ")
tahun_lahir = input("Masukkan tahun lahir Anda  : ")

# Melakukan kalkulasi usia (Ingat, sekarang adalah tahun 2026!)
tahun_sekarang = 2026
usia = tahun_sekarang - int(tahun_lahir)

print(f"\nHalo {nama}! Berdasarkan tahun lahirmu, usiamu adalah {usia} tahun.")

# Menentukan apakah boleh memesan kopi espresso double shot
boleh_minum_kopi = usia >= 15
print(f"Apakah boleh memesan Espresso Double Shot? -> {boleh_minum_kopi}")
print("\nTerima kasih telah bertransaksi di kafe kami!\n")


print("=== EKSPERIMEN 1: URUTAN TIDAK BERPENGARUH ===")
# Kita punya dua harga bahan baku independen
harga_kopi = 15000
harga_susu = 5000

total_bahan = harga_kopi + harga_susu
print(f"Total bahan baku (Urutan A): Rp{total_bahan}")

# Jika posisi inisialisasi ditukar, hasilnya tetap sama!
harga_susu_baru = 5000
harga_kopi_baru = 15000
total_bahan_baru = harga_kopi_baru + harga_susu_baru
print(f"Total bahan baku (Urutan B): Rp{total_bahan_baru}\n")


print("=== EKSPERIMEN 2: URUTAN SANGAT BERPENGARUH ===")
# Skenario Awal:
# Kita ingin memangkatkan angka 4, lalu membagi bulat angka 10.
angka_a = 4
angka_b = 10

print("Hasil Skenario Awal:")
print(f"Pangkat 2 dari {angka_a} -> {angka_a ** 2}")
print(f"Bagi bulat {angka_b} dengan 3 -> {angka_b // 3}\n")

# Skenario Modifikasi:
# Kita tidak sengaja menukar posisi perintah print() di atas.
print("Hasil Skenario Modifikasi (Urutan Cetak Ditukar):")
print(f"Bagi bulat {angka_b} dengan 3 -> {angka_b // 3}")
print(f"Pangkat 2 dari {angka_a} -> {angka_a ** 2}")
print("-> Perhatikan! Urutan output pada layar berubah total karena posisi print() ditukar.")