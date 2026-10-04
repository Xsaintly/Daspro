# Nama File: Deret no 5.py
# Pembuat: Muhammad Deren Julian
# tanggal 04/10/2026
# Deskripsi: Mencari suku ke-n dari deret 3, 6, 9, 12, 15, 18 secara rekursif

# Definisi dan Spesifikasi
# deret: integer -> integer
#   {deret(n) Mencari suku ke-n dari deret 3, 6, 9, 12, 15, 18 secara rekursif.}

# Realisasi

def deret_1(n) :
    if n == 1 : 
        return 3
    return deret_1(n-1) + 3

print(deret_1(2))