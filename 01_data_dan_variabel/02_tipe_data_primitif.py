# =====================================================================
# FILE: 02_tipe_data_primitif.py
# DESKRIPSI: Eksplorasi tipe data tunggal (Integer, Float, Bool, String)
# =====================================================================

# --- 1. MEMBUKTIKAN DYNAMIC TYPING ---
print("=== 1. DYNAMIC TYPING ===")
kotak_ajaib = 99
print(f"Isi: {kotak_ajaib} | Tipe data: {type(kotak_ajaib)}")

# Tanpa deklarasi ulang, kita langsung ganti isinya dengan teks
kotak_ajaib = "Sekarang jadi string!"
print(f"Isi: {kotak_ajaib} | Tipe data: {type(kotak_ajaib)}\n")


# --- 2. NUMBERS & EKSPLORASI IMMUTABLE ---
print("=== 2. ANGKA & ALAMAT MEMORI (IMMUTABLE) ===")
skor = 10
print(f"Skor awal : {skor} | Lokasi Memori: {id(skor)}")

# Saat kita ubah nilainya...
skor = 11
print(f"Skor baru : {skor} | Lokasi Memori: {id(skor)}")
print("-> Perhatikan lokasi memorinya berubah! Python membuat objek baru di memori.\n")


# --- 3. BOOLEAN & KEBENARAN SEMU (TRUTHY / FALSY) ---
print("=== 3. KEBENARAN BOOLEAN ===")
apakah_hujan = True
print(f"Status hujan: {apakah_hujan} | Tipe: {type(apakah_hujan)}")

# Eksperimen nilai kosong vs nilai berisi
nama_kosong = ""
nama_isi = "Fathin Zidan"
print(f"Apakah teks kosong itu bernilai benar? -> {bool(nama_kosong)}")
print(f"Apakah teks berisi itu bernilai benar? -> {bool(nama_isi)}\n")


# --- 4. STRING & BERBAGAI CARA FORMATTING ---
print("=== 4. RAHASIA STRING ===")
# Teks multi-baris
pesan_pantai = """Halo Bro!
Kapan kita main voli pantai lagi?
Ditunggu di lapangan biasa ya!"""
print(pesan_pantai)

# Bermain dengan Indeks dan Slicing
game_favorit = "RobloxStudio"
print(f"Huruf pertama: {game_favorit[0]}")
print(f"Potong kata belakang (Slicing): {game_favorit[6:]}")

# HATI-HATI: String itu Immutable!
# Kode di bawah ini kalau diaktifkan bakal bikin error:
# game_favorit[0] = "P"  # TypeError: 'str' object does not support item assignment

print("\n--- 3 Gaya Menampilkan String (Formatting) ---")
pemain = "Zidan"
no_punggung = 7

# Gaya 1: Formatted String (f-string) -> Paling direkomendasikan & modern!
print(f"[F-String] {pemain} memakai nomor punggung {no_punggung}")

# Gaya 2: str.format() -> Gaya rapi abad pertengahan
print("[Str.Format] {} memakai nomor punggung {}".format(pemain, no_punggung))

# Gaya 3: %-formatting -> Gaya klasik/jadul mirip C
print("[%%-Formatting] %s memakai nomor punggung %d" % (pemain, no_punggung))