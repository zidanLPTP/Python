# =====================================================================
# FILE: 03_blok_kode_dan_indentasi.py
# DESKRIPSI: Memahami konsep kode blok dan aturan sakral Indentasi
# =====================================================================

print("=== 1. BLOK KODE DENGAN INDENTASI YANG BENAR ===")

# Di Python, blok kode didefinisikan dengan menyisipkan spasi/indentasi.
# Contoh di bawah adalah sebuah perulangan (loop) untuk menghitung mundur.
# Program akan mencetak pesan sebanyak 3 kali secara berurutan.

for i in range(1, 4):
    # Baris di bawah ini menjorok ke dalam (4 spasi / 1 Tab).
    # Ini menandakan baris tersebut adalah 'anak buah' dari perintah for di atas.
    print(f"Langkah ke-{i}: Sedang memproses data...")
    print("-> Selesai memproses sub-langkah.")

print("Ini di luar blok perulangan. Hanya tercetak SEKALI di akhir.\n")


print("=== 2. MISTERI INDENTATION ERROR ===")
print("""
HATI-HATI!
Jika kamu menulis kode seperti ini:

for i in range(3):
print(i)

Interpreter Python akan langsung ngambek dan melempar error:
'IndentationError: expected an indented block after f-string/statement'

Mengapa? Karena Python tidak memakai kurung kurawal {}, dia murni 
bergantung pada kerapian spasi untuk menentukan di mana awal dan akhir 
sebuah blok kode.
""")

# Coba aktifkan baris kode di bawah ini dengan menghapus tanda pagar (#) 
# untuk melihat error-nya secara langsung di terminalmu!
# for i in range(3):
# print(i)