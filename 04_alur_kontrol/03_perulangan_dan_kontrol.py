# =====================================================================
# FILE: 03_perulangan_dan_kontrol.py
# DESKRIPSI: Praktek perulangan For, While, Nested Loop, dan Kontrol Loop
# =====================================================================

print("=== 1. PERULANGAN FOR & MATEMATIKA RANGE() ===")
# range(start, stop, step) -> start inklusif, stop eksklusif
print("Menghitung bilangan ganjil 1 sampai 10:")
for angka in range(1, 10, 2):
    print(f"-> Angka ganjil saat ini: {angka}")
print()


print("=== 2. PERULANGAN WHILE (INDEFINITE ITERATION) ===")
stok_peluru = 5

# Perulangan berjalan selama kondisi bernilai True
while stok_peluru > 0:
    print(f"Duar! Menembak musuh. Sisa peluru: {stok_peluru}")
    stok_peluru -= 1  # Mengurangi counter agar tidak memicu INFINITE LOOP!

print("Klik! Peluru habis, segera reload senjata.\n")


print("=== 3. RADAR KOORDINAT GAME (NESTED LOOP) ===")
# Skenario scanning koordinat grid 2x3 (X, Y)
for baris_x in range(1, 3):      # Outer loop (Baris)
    for kolom_y in range(1, 4):  # Inner loop (Kolom)
        print(f"Scanning Sektor -> [{baris_x}, {kolom_y}]")
print()


print("=== 4. KONTROL PERULANGAN (BREAK, CONTINUE, PASS) ===")

print("Eksperimen 'Continue' (Lewati huruf vokal):")
for huruf in "KODING":
    if huruf in "AIUEO":
        continue  # Menghentikan iterasi saat ini dan langsung lompat ke iterasi berikutnya
    print(f"Huruf konsonan: {huruf}")

print("\nEksperimen 'Break' (Berhenti jika bertemu spasi):")
nama_lengkap = "Fathin Zidan"
for karakter in nama_lengkap:
    if karakter == " ":
        break  # Memaksa perulangan berhenti total saat itu juga
    print(karakter, end="")
print(" (Berhenti di spasi!)\n")

print("Eksperimen 'Pass' (Placeholder kosong):")
for i in range(3):
    if i == 1:
        pass  # Tidak melakukan tindakan apa pun, hanya agar sintaks tetap valid
    else:
        print(f"Nilai: {i}")
print()


print("=== 5. SIHIR 'ELSE' SETELAH LOOP ===")
# Else setelah FOR atau WHILE hanya dieksekusi jika perulangan SELESAI SECARA ALAMI
# (artinya tidak ada perintah 'break' yang dipicu di tengah jalan)

daftar_barang = ["Pedang", "Ramuan", "Perisai", "Kunci"]
target_cari = "Emas"

print(f"Mencari barang '{target_cari}' di dalam tas...")
for barang in daftar_barang:
    if barang == target_cari:
        print("-> Ketemu! Harta karun berhasil diamankan.")
        break
else:
    # Blok ini berjalan karena loop selesai menyisir semua barang tanpa memicu 'break'
    print("-> Pencarian selesai. Barang tidak ditemukan di dalam tas.")