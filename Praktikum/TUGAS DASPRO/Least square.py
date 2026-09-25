# Nama File : Least Square
# Pembuat   : Muhammad Deren Julian
# Tanggal   : 31 Agustus 2026
# Deskripsi : Least square (jarak 2 titik)

# Definisi dan Spesifikasi
# Digunakan untuk menghitung jarak antara 2 buah titik 

# Realisasi

def FX2(X) :  
    return X * X
def dif2(x,y) : 
    return FX2(x - y)
def least_square(x1,y1,x2,y2) : 
    total_kuadrat = dif2(y2,y1) + dif2(x2,x1)
    return total_kuadrat ** 0.5

print(least_square(1,3,6,9))