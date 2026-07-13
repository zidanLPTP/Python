# =====================================================================
# FILE: 04_case_sensitivity_dan_oneliner.py
# DESKRIPSI: Praktek sensitivitas huruf & sihir One-Liner (Tukar Variabel)
# =====================================================================

print("=== 1. PEMBUKTIAN CASE-SENSITIVITY ===")
token_akses = "A001_Aman"
Token_Akses = "B002_Waspada"
TOKEN_AKSES = "C003_Bahaya"

# Bagi komputer, ketiga nama di atas merujuk pada tiga lokasi memori berbeda!
print(f"Isi token_akses (lowercase) : {token_akses}")
print(f"Isi Token_Akses (Titlecase) : {Token_Akses}")
print(f"Isi TOKEN_AKSES (UPPERCASE) : {TOKEN_AKSES}\n")

# HATI-HATI: Typo sedikit saja berujung bencana NameError!
# print(tOkEn_AkSeS) # Un-comment ini untuk melihat NameError: 'tOkEn_AkSeS' is not defined


print("=== 2. CARA KLASIK: PENUKARAN NILAI (3 GELAS) ===")
# Skenario: Kita ingin menukar isi Gelas Matcha dan Gelas Espresso.
gelas_matcha = "Matcha Latte"
gelas_espresso = "Espresso Shot"

print(f"Sebelum ditukar -> Matcha: {gelas_matcha} | Espresso: {gelas_espresso}")

# Cara Klasik: Kita butuh satu gelas kosong cadangan (gelas_temp)
gelas_temp = gelas_matcha     # Pindahkan Matcha ke gelas cadangan (Gelas Matcha kini kosong)
gelas_matcha = gelas_espresso  # Tuangkan Espresso ke Gelas Matcha (Gelas Espresso kini kosong)
gelas_espresso = gelas_temp    # Tuangkan Matcha dari gelas cadangan ke Gelas Espresso

print(f"Setelah ditukar -> Matcha: {gelas_matcha} | Espresso: {gelas_espresso}\n")


print("=== 3. CARA PREMIUM PYTHON: ONE-LINER SWAP! ===")
# Kembalikan kondisi awal
gelas_matcha = "Matcha Latte"
gelas_espresso = "Espresso Shot"

print(f"Sebelum ditukar -> Matcha: {gelas_matcha} | Espresso: {gelas_espresso}")

# SIHIR SATU BARIS (One-Liner Tuple Unpacking)
# Di Python, kita tidak perlu gelas bantuan sama sekali! Cukup lakukan ini:
gelas_matcha, gelas_espresso = gelas_espresso, gelas_matcha

print(f"Setelah ditukar -> Matcha: {gelas_matcha} | Espresso: {gelas_espresso}")
print("\n-> Kok bisa? Python mengevaluasi sisi kanan terlebih dahulu untuk membuat tuple")
print("   sementara di memori, lalu membaginya sekaligus ke variabel di sisi kiri!")