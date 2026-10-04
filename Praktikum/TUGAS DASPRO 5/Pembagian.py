# Nama File: Pembagian.py
# Pembuat: Muhammad Deren Julian
# tanggal 04/10/2026
# Deskripsi: Membagi dua bilangan secara rekursif

# Definisi dan Spesifikasi
# Pembagian: 2integer -> integer
#   {Pembagian(a,b) membagi a dengan b secara rekursif.}

# Realisasi
def bagi (x,y) :
    if y == 0:
        return 0
    elif x < 0 and y < 0 :
        return bagi(-x, -y)
    elif x < 0 :
        return bagi(-x, y)
    elif y < 0 :
        return bagi(x, -y)
    elif x < y :
        return 0
    else:
        return 1 + bagi(x, y - y)

print(bagi(10, 2))
