# =====================================================================
# FILE: 05_penanganan_error_dan_exception.py
# DESKRIPSI: Menguasai Try, Except, Else, Finally, dan Raise Exception
# =====================================================================

print("=== 1. SYNTANX ERROR VS RUNTIME EXCEPTION ===")
print("""
Sebagai programmer, kamu wajib membedakan dua klan error ini:
1. Syntax Error (Kesalahan Tata Bahasa):
   Terjadi sebelum kode dijalankan. Misalnya lupa menulis titik dua (:), typo perintah,
   atau salah menaruh indentasi (IndentationError). Interpreter langsung mogok total.

2. Runtime Exception (Pengecualian saat Operasi):
   Sintaks kodemu secara tata bahasa sudah 100% benar, tetapi di tengah jalan program 
   menabrak masalah yang mustahil diproses (misal: membagi angka dengan nol, 
   atau memanggil variabel yang belum dibuat).
""")


print("=== 2. PENYELAMATAN KODE (TRY-EXCEPT-ELSE-FINALLY) ===")

pembagi = 0

try:
    # Letakkan kode yang berisiko memicu kecelakaan di sini
    print("Mencoba melakukan pembagian...")
    hasil = 100 / pembagi
    print(f"Berhasil! Hasil pembagian: {hasil}")
except ZeroDivisionError:
    # Skenario penyelamatan jika terjadi error pembagian nol
    print("[ERROR DETECTED] Ups! Di dunia matematika kita tidak boleh membagi dengan angka 0.")
else:
    # Blok ini hanya berjalan jika area 'try' mulus tanpa error sama sekali
    print("Hebat! Tidak ada error yang terjadi dalam proses tadi.")
finally:
    # Blok sakral yang AKAN SELALU dijalankan, baik program sukses maupun hancur lebur
    print("Blok finally: Pembersihan memori selesai. Sistem tetap aman terkendali!\n")


print("=== 3. MENYARING BEBERAPA TIPE ERROR SEKALIGUS ===")
biodata_agen = {"nama": "Anya", "level": 99}

try:
    # Skenario A: Mengakses kunci yang tidak ada di dictionary (KeyError)
    # print(biodata_agen["alamat"]) 
    
    # Skenario B: Menghitung string dengan angka (TypeError)
    hitung_level = biodata_agen["nama"] / 2
    print(hitung_level)
except KeyError:
    print("[KeyError] Kunci biodata yang kamu cari tidak terdaftar!")
except TypeError:
    print("[TypeError] Kamu tidak bisa membagi tipe data teks (string) dengan angka!")
print()


print("=== 4. MENOLAK DATA DENGAN SENGAJA (RAISE EXCEPTION) ===")

def setor_tunai(nominal):
    # Kita tidak ingin menerima transaksi bernilai minus atau nol!
    if nominal <= 0:
        # Lempar error ValueError secara sengaja agar program luar tahu ada yang salah
        raise ValueError(f"Sistem Menolak! Nominal Rp{nominal} tidak valid untuk setor tunai.")
    else:
        print(f"Setor tunai sukses! Saldo bertambah Rp{nominal}")

# Uji coba sistem setor tunai
try:
    setor_tunai(50000)   # Aman
    setor_tunai(-10000)  # Ini akan melempar ValueError sengaja!
except ValueError as pesan_error:
    print(f"[BLOCKED] Terjadi Kesalahan Keuangan: {pesan_error}")