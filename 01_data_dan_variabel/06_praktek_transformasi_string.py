# =====================================================================
# FILE: 06_praktek_transformasi_string.py
# DESKRIPSI: Eksplorasi metode transformasi, pembersihan, & pengecekan string
# =====================================================================

# --- 1. MENGUBAH CAPITAL & LOWER CASE ---
print("=== 1. HURUF BESAR & KECIL ===")
nama_belajar = "python nusantara"
print(f"Awal : {nama_belajar}")
print(f"Upper: {nama_belajar.upper()}")
print(f"Title: {nama_belajar.title()}\n") # Setiap awal kata kapital


# --- 2. MEMBERSIHKAN WHITESPACE & TEKS PENGGANGGU ---
print("=== 2. SIHIR STRIP ===")
teks_kotor = "     Kopi Luwak     "
# rstrip hapus kanan, lstrip hapus kiri, strip hapus keduanya
print(f"Normal: |{teks_kotor}|")
print(f"Strip : |{teks_kotor.strip()}|\n")

# Menghilangkan kata tertentu di ujung string
teks_berulang = "KopiKopiPythonKopiKopi"
print(f"Awal   : {teks_berulang}")
print(f"Dipotong: {teks_berulang.strip('Kopi')}\n")


# --- 3. MENCOCOKKAN AWALAN & AKHIRAN ---
print("=== 3. START/END WITH ===")
domain = "https://belajarpython.id"
print(f"Domain: {domain}")
print(f"Apakah secure link? (diawali https) -> {domain.startswith('https')}")
print(f"Apakah berdomain .id?               -> {domain.endswith('.id')}\n")


# --- 4. MEMECAH & MENGGABUNGKAN STRING (SPLIT & JOIN) ---
print("=== 4. SPLIT & JOIN ===")
kalimat = "Aku suka belajar bahasa Python"
# split() default memisahkan berdasarkan spasi
kata_kata = kalimat.split()
print(f"Hasil Split: {kata_kata}")

# Menggabungkan kembali dengan delimiter unik
kalimat_baru = " - ".join(kata_kata)
print(f"Hasil Join : {kalimat_baru}\n")

# Memisahkan baris pada teks multiline menggunakan '\n'
teks_panjang = """Halo,
aku elang,
aku suka terbang tinggi."""
print("Hasil Split Multiline:")
print(teks_panjang.split('\n'))
print()


# --- 5. MENGGANTI ELEMEN (REPLACE) ---
print("=== 5. SIHIR REPLACE ===")
kalimat_asal = "Ayo ngopi dan belajar Coding di Pythonis!"
# Ingat! Replace bersifat case-sensitive
kalimat_edit = kalimat_asal.replace("Coding", "Pemrograman")
print(f"Asli: {kalimat_asal}")
print(f"Edit: {kalimat_edit}\n")


# --- 6. PENGECEKAN KARAKTER (VALIDASI) ---
print("=== 6. PENGECEKAN STRING ===")
id_user = "budi123"
print(f"Apakah '{id_user}' alfanumerik?  -> {id_user.isalnum()}")
print(f"Apakah '{id_user}' hanya angka?   -> {id_user.isdecimal()}")
print(f"Apakah '12345' hanya angka?      -> {'12345'.isdecimal()}")
print(f"Apakah '  ' hanya berisi spasi?  -> {'  '.isspace()}\n")


# --- 7. MERAPIKAN FORMAT LEBAR TEKS ---
print("=== 7. SIHIR FORMATTING ===")
no_antrean = "45"
print(f"No Antrean (zfill)   : {no_antrean.zfill(5)}")
print(f"Rata Kanan (rjust)   : {'Kopi'.rjust(15, '*')}")
print(f"Rata Tengah (center) : {'Python'.center(14, '=')}\n")


# --- 8. ESCAPE CHARACTER VS RAW STRING ---
print("=== 8. ESCAPE CHARACTER VS RAW STRING ===")
# Menggunakan petik satu di tengah string & enter (\n)
print("Hari Jum'at ini,\nkita belajar \"Python\" di lab komputer.")
print()

# Perbedaan string biasa vs Raw String
string_biasa = "Folder_PC\\temp\\new_file.txt"
string_raw   = r"Folder_PC\temp\new_file.txt" # Huruf 'r' di depan string

print(f"Biasa : {string_biasa}")
print(f"Raw   : {string_raw}")