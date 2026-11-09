# Nama File : Mean olympique
# Pembuat   : Muhammad Deren Julian
# Tanggal   : 31 Agustus 2026
# Deskripsi : Mean Olympique dari 4 bilangan

# Definisi dan Spesifikasi
# Menghapus nilai maksimum dan minimum untuk menghitung rata rata

# Realisasi

def max2 (a,b) : 
    return (a + b + abs (a - b))/2
def min2 (a,b) : 
    return (a + b - abs (a - b))/2

def max6 (o,p,q,r) :
    return max2 (max2(o,p),max2(q,r))
def min6 (o,p,q,r) :
    return min2 (min2(o,p),min2(q,r))

def MO (u,v,w,x):  
    return (u+v+w+x-min6(u,v,w,x)-max6(u,v,w,x))/2

print(MO(2,6,6,10))