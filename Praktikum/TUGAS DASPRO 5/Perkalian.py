# Nama File: Perkalian.py
# Pembuat: Muhammad Deren Julian
# tanggal 04/10/2026
# Deskripsi: Mengalikan dua bilangan secara rekursif

# Definisi dan Spesifikasi
# perkalian: 2integer -> integer
#   {perkalian(a,b) mengalikan dua bilangan a dan b secara rekursif.}

# Realisasi

def perkalian(a,b) :
    if b < 0 : 
        return -perkalian(a,-b)    
    elif b == 0 : 
        return 0
    elif b == 1 : 
        return a 
    else : 
        return a+perkalian(a, b-1)

print(perkalian(1,10))