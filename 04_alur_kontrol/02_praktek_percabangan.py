# =====================================================================
# FILE: 02_praktek_percabangan.py
# DESKRIPSI: Praktek if, elif, else, truthy/falsy, dan ternary operator
# =====================================================================

print("=== 1. STATEMENT IF & SENSITIVITAS HURUF ===")
status_gerbang = "Terbuka"

# Aturan Sakral: Ingat indentasi (4 spasi/1 tab) setelah tanda titik dua (:)
if status_gerbang == "Terbuka":
    print("Gerbang markas terbuka. Selamat datang!")

# Eksperimen Case-Sensitivity: "terbuka" (t kecil) tidak akan memicu blok di bawah ini
if status_gerbang == "terbuka":
    print("Pesan ini tidak akan pernah tercetak karena huruf awal 'T' berbeda dengan 't'.")
print("-> Selesai pengecekan gerbang.\n")


print("=== 2. MISTERI TRUTHY & FALSY IN PYTHON ===")
# Python menganggap wadah kosong atau angka 0 sebagai False, sisanya dianggap True
daftar_belanja = []  # List kosong (Falsy)
nama_pengunjung = "Ronaldo"  # String berisi (Truthy)

if daftar_belanja:
    print("Daftar belanja ada isinya!")
else:
    print("Daftar belanja masih kosong melompong (Dievaluasi sebagai False).")

if nama_pengunjung:
    print(f"Pengunjung terdeteksi: {nama_pengunjung} (Dievaluasi sebagai True).")
print()


print("=== 3. SISTEM VERIFIKASI BIOSKOP (IF-ELIF-ELSE) ===")
# Skenario rating usia penonton bioskop
usia_penonton = 15
memiliki_tiket = True

print(f"Profil Penonton -> Usia: {usia_penonton} | Tiket: {memiliki_tiket}")

if usia_penonton >= 17 and memiliki_tiket:
    print("Akses Diterima: Boleh menonton film kategori Dewasa (D17).")
elif usia_penonton >= 13 and memiliki_tiket:
    print("Akses Diterima: Boleh menonton film kategori Remaja (R13).")
elif usia_penonton < 13 and memiliki_tiket:
    print("Akses Diterima: Hanya boleh menonton film kategori Semua Umur (SU).")
else:
    print("Akses Ditolak: Anda tidak memiliki tiket fisik!")
print()


print("=== 4. SIHIR TERNARY OPERATOR (ONE-LINER CONDITIONAL) ===")
is_admin = True

# Gaya Premium (Sangat direkomendasikan karena mudah dibaca)
status_akses = "Akses Server Diberikan!" if is_admin else "Akses Ditolak!"
print(f"Hasil Ternary Standar -> {status_akses}")

# Gaya Lama / Ternary Tuple (Sebaiknya dihindari, tapi wajib tahu agar tidak bingung)
# format: (Hasil_Jika_False, Hasil_Jika_True)[Kondisi_Boolean]
status_akses_tuple = ("Akses Ditolak!", "Akses Server Diberikan!")[is_admin]
print(f"Hasil Ternary Tuple   -> {status_akses_tuple}")