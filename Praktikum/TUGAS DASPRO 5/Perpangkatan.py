# Nama File: Perpangkatan.py
# Pembuat: Muhammad Deren Julian
# tanggal 04/10/2026
# Deskripsi: Mempangkatkan suatu bilangan secara rekursif

# Definisi dan Spesifikasi
# perpangkatan: 2integer -> integer
#   {perpangkatan(a,b) memangkatkan a dengan b (a^b)secara rekursif.}

# Realisasi
def perpangkatan(a,b) :
    if b < 0 : 
        return 1/perpangkatan(a,-b)
    if b == 0 :
        return 1
    if b == 1 :
        return a
    return a*perpangkatan(a,b-1)


#Aplikasi
print(perpangkatan(4,4))