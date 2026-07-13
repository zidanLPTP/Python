# =====================================================================
# FILE: 03_operator_relasional_dan_logika.py
# DESKRIPSI: Membandingkan Nilai & Logika Boolean
# =====================================================================

# --- 1. OPERATOR RELASIONAL (PERBANDINGAN ANGKA) ---
print("=== 1. PERBANDINGAN NUMERIK ===")
nilai_rudi = 85
nilai_kkm = 75

print(f"Apakah Rudi Lulus? (nilai_rudi >= nilai_kkm) -> {nilai_rudi >= nilai_kkm}")
print(f"Apakah nilainya tidak sama dengan KKM?       -> {nilai_rudi != nilai_kkm}\n")


# --- 2. PERBANDINGAN STRING (MISTERI UNICODE/ASCII) ---
print("=== 2. PERBANDINGAN STRING ===")
# Ingat! Python membandingkan string berdasarkan urutan karakter di Tabel ASCII/Unicode.
# Huruf Kapital memiliki nilai angka yang lebih KECIL dibanding Huruf Kecil.

kata1 = "Apel"
kata2 = "banana"

print(f"Teks 1: '{kata1}' | Teks 2: '{kata2}'")
print(f"Apakah '{kata1}' == '{kata2}'? -> {kata1 == kata2}")
print(f"Apakah '{kata1}' < '{kata2}'?  -> {kata1 < kata2}")
print("-> Mengapa True? Karena huruf 'A' kapital mendahului 'b' kecil di tabel Unicode.\n")


# --- 3. OPERATOR LOGIKA (AND, OR, NOT) ---
print("=== 3. GERBANG LOGIKA ===")
punya_tiket = True
sudah_vaksin = False

print(f"Status Tiket: {punya_tiket} | Status Vaksin: {sudah_vaksin}")
# AND: Keduanya wajib True
print(f"Boleh masuk konser? (AND) : {punya_tiket and sudah_vaksin}")

# OR: Salah satu True sudah cukup
print(f"Boleh masuk mall? (OR)    : {punya_tiket or sudah_vaksin}")

# NOT: Membalikkan kenyataan
print(f"Apakah belum vaksin? (NOT): {not sudah_vaksin}\n")
