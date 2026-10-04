# Nama File: Deret no 6.py
# Pembuat: Muhammad Deren Julian
# tanggal 04/10/2026
# Deskripsi: Mencari suku ke-n dari deret 1, -2, 3, -4, 5, -6,... secara rekursif

# Definisi dan Spesifikasi
# deret_2: integer -> integer
#   {deret_2(n) Mencari suku ke-n dari deret 1, -2, 3, -4, 5, -6,... secara rekursif.}

# Realisasi

def deret_2(n) :
    if n == 1 : 
        return 1
    return -deret_2(n-1) + (1 if n%2 == 1 else -1)

print(deret_2(4))