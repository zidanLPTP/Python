# =====================================================================
# FILE: 07_operasi_kumpulan_data.py
# DESKRIPSI: Praktek fungsi len, min, max, count, in, unpacking, & sort
# =====================================================================

# --- 1. MENCOBA FUNGSI LEN, MIN, MAX, DAN COUNT ---
print("=== 1. OPERASI DASAR KUMPULAN DATA ===")
skor_pemain = [25, 40, 15, 90, 40, 75, 40]
print(f"Daftar Skor: {skor_pemain}")
print(f"Jumlah data (len)     : {len(skor_pemain)}")
print(f"Skor terendah (min)   : {min(skor_pemain)}")
print(f"Skor tertinggi (max)  : {max(skor_pemain)}")
print(f"Berapa kali skor 40 muncul? -> {skor_pemain.count(40)} kali\n")

# Mencoba len & count pada Tipe Data String
pesan = "Belajar Python di Nusantara sangat seru!"
print(f"Teks: \"{pesan}\"")
print(f"Jumlah karakter (termasuk spasi): {len(pesan)}")
print(f"Berapa kali huruf 'a' muncul?   : {pesan.count('a')}\n")


# --- 2. OPERATOR KEYAKINAN (IN & NOT IN) ---
print("=== 2. OPERATOR IN & NOT IN ===")
menu_makanan = ["Kopi", "Roti", "Susu", "Keju"]
print(f"Menu: {menu_makanan}")
print(f"Apakah ada 'Kopi' di menu?      -> {'Kopi' in menu_makanan}")
print(f"Apakah 'Teh' tidak ada di menu? -> {'Teh' not in menu_makanan}\n")


# --- 3. MULTIPLE VARIABLE ASSIGNMENT (UNPACKING) ---
print("=== 3. TEKNIK UNPACKING ===")
spesifikasi = ["Asus Rogue", "16GB", "1TB SSD"]

# Cara praktis memasukkan nilai list ke dalam variabel terpisah sekaligus
brand, ram, storage = spesifikasi
print(f"Brand   : {brand}")
print(f"RAM     : {ram}")
print(f"Storage : {storage}\n")


# --- 4. MISTERI PENGURUTAN DATA (SORT & TABEL ASCII) ---
print("=== 4. RAHSIA URUTAN DATA (SORT) ===")
# Pengurutan Angka
daftar_angka = [50, 10, 85, 5, 45]
daftar_angka.sort()
print(f"Urutan Angka Ascending : {daftar_angka}")

# Pengurutan Descending (Menurun)
daftar_angka.sort(reverse=True)
print(f"Urutan Angka Descending: {daftar_angka}\n")

# HATI-HATI! Pengurutan String menggunakan Nilai ASCII
kata_unik = ["kopi", "Roti", "susu", "Keju"]
kata_unik.sort()
print("Hasil .sort() standar (perhatikan huruf kapital berada di depan):")
print(kata_unik) # Output: ['Keju', 'Roti', 'kopi', 'susu']
print("-> Mengapa 'Roti' mendahului 'kopi'? Karena nilai ASCII 'R' kapital lebih kecil dibanding 'k' kecil.\n")

# SOLUSI: Mengurutkan tanpa mempedulikan huruf besar/kecil (Case-Insensitive)
kata_unik.sort(key=str.lower)
print("Hasil .sort(key=str.lower) (urutan rapi sesuai alfabet asli):")
print(kata_unik)