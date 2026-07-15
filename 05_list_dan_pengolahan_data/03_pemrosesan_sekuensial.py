# =====================================================================
# FILE: 03_pemrosesan_sekuensial.py
# DESKRIPSI: Pemrosesan array secara berurutan & perbandingan suksesor
# =====================================================================

print("=== 1. PEMROSESAN SEKUENSIAL: MENGHITUNG RATA-RATA SKOR ===")
# Skenario: Data skor uji kelayakan sistem keamanan server
skor_keamanan = [90, 85, 88, 92, 80, 95, 89]

total_skor = 0
for skor in skor_keamanan:
    total_skor += skor  # Memproses setiap elemen dari indeks terkecil ke terbesar

rata_rata = total_skor / len(skor_keamanan)
print(f"Data Skor Keamanan : {skor_keamanan}")
print(f"Total Akumulasi Skor: {total_skor}")
print(f"Rata-rata Keamanan  : {rata_rata:.2f}\n")


print("=== 2. ALGORITMA PENGECEKAN SUKSESOR (CURRENT VS NEXT) ===")
# Skenario: Kita ingin mendeteksi tren kenaikan/penurunan suhu server cloud
suhu_server = [32, 35, 34, 38, 40] # dalam derajat Celcius

print(f"Data Suhu Server: {suhu_server}")
panjang_suhu = len(suhu_server)

for i in range(panjang_suhu):
    suhu_sekarang = suhu_server[i]
    indeks_berikutnya = i + 1
    
    # Cek apakah suksesor indeks masih berada dalam jangkauan array
    if indeks_berikutnya < panjang_suhu:
        suhu_berikutnya = suhu_server[indeks_berikutnya]
        
        # Bandingkan apakah suhu sedang naik atau turun dibanding jam sebelumnya
        if suhu_berikutnya > suhu_sekarang:
            status = "(Suhu Naik)"
        elif suhu_berikutnya < suhu_sekarang:
            status = "(Suhu Turun)"
        else:
            status = "(Suhu Stabil)"
    else:
        # Jika sudah sampai di ujung lantai apartemen / akhir indeks
        suhu_berikutnya = None
        status = "⏹(Akhir Pemantauan)"
        
    print(f"Jam Ke-{i} | Suhu Saat Ini: {suhu_sekarang}°C -> Berikutnya: {suhu_berikutnya if suhu_berikutnya else '-'} {status}")
print()