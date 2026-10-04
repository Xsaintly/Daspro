# Nama File: penjumlahan suku no 7.py
# Pembuat: Muhammad Deren Julian
# tanggal 04/10/2026
# Deskripsi: Menjumlahkan suku pertama sampai ke-15 (S15) dari deret 1 + 3 + 5 + 7 + 9 + 11...(n15) secara rekursif

# Definisi dan Spesifikasi
# jumlah_suku: integer -> integer
#   {jumlah_suku(n)  Menjumlahkan suku pertama sampai ke-15 (S15) dari deret 1 + 3 + 5 + 7 + 9 + 11...(n15) secara rekursif}

# Realisasi


def jumlah_suku(n) :
    if n == 0 : 
        return 0
    return jumlah_suku(n-1)+(2*n-1)

print(jumlah_suku(15))