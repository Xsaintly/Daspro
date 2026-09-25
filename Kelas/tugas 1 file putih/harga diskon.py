# Nama File : harga diskon.py
# Pembuat   : Muhammad Deren Julian
# Tanggal   : 7 September 2026
# Deskripsi : memetakan nilai x (harga awal) dan y (persentase diskon) kedalam
# harga akhirdengan rumus x *(x*y/100) 

# Definisi dan Spesifikasi
# harga diskon : float, float -> float, mengembalikan nilai nominal akhirdari harga awal x 
# setelah dikurangi persentase diskon y, 
# dengan domain x kurang dari = 0 dan 0 kurang dari = y kurang dari = 100

# Realisasi
def harga_diskon(x: float, y: float) -> float :
    return (x-(x*y/100))

print(harga_diskon(1000000, 20))