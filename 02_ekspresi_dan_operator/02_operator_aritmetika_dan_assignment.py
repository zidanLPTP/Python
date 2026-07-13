# =====================================================================
# FILE: 02_operator_aritmetika_dan_assignment.py
# DESKRIPSI: Eksplorasi Operator Matematika & Singkatan Assignment
# =====================================================================

# --- 1. OPERATOR MATEMATIKA STANDARD ---
print("=== 1. OPERASI MATEMATIKA DASAR ===")
a = 15
b = 4

print(f"Angka Pertama (a): {a} | Angka Kedua (b): {b}\n")
print(f"Penjumlahan (+)      : {a + b}")
print(f"Pengurangan (-)      : {a - b}")
print(f"Perkalian (*)        : {a * b}")
print(f"Pembagian Riil (/)   : {a / b}  <- Hasilnya selalu Float")
print(f"Pembagian Bulat (//) : {a // b}  <- Membulatkan ke bawah")
print(f"Sisa Bagi / Modulo (%): {a % b}  <- Berguna cek ganjil/genap")
print(f"Perpangkatan (**)    : {a ** b} <- Sama dengan a pangkat b\n")


# --- 2. JONGKLEUR DATA: OPERATOR PADA LIST & STRING ---
print("=== 2. SIHIR OPERATOR PADA LIST & STRING ===")
# Menggabungkan (Concatenation)
kue_asin = ["Roti", "Keju"]
kue_manis = ["Donat", "Cokelat"]
menu_kafe = kue_asin + kue_manis
print(f"Menu Gabungan (+)    : {menu_kafe}")

# Replikasi (Multiplication)
teriakan = "Hei! "
print(f"Replikasi String (*) : {teriakan * 3}")

opsi_list = [0]
print(f"Inisialisasi List (*) : {opsi_list * 5}\n")


# --- 3. OPERATOR ASSIGNMENT (SHORTCUT PENULISAN) ---
print("=== 3. PENULISAN CEPAT (ASSIGNMENT OPERATOR) ===")
stok_buku = 10
print(f"Stok Awal: {stok_buku}")

# Cara konvensional: stok_buku = stok_buku + 5
# Cara keren (Shortcut):
stok_buku += 5
print(f"Setelah ditambah 5 (+=)  : {stok_buku}")

stok_buku -= 3
print(f"Setelah dikurangi 3 (-=) : {stok_buku}")

stok_buku *= 2
print(f"Setelah dikali 2 (*=)    : {stok_buku}")

stok_buku /= 4
print(f"Setelah dibagi 4 (/=)    : {stok_buku} (Berubah jadi float!)")
