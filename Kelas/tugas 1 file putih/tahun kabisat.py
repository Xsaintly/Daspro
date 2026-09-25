# Nama File : Apakah huruf A
# Pembuat   : Muhammad Deren Julian
# Tanggal   : 7 September 2026
# Deskripsi : Menentukan apakah suatu tahun merukapan tahun kabisat
# berdasarkan aturan kelipatan 400 atau kelipatan 4 yang bukan kelipatan 100

# Definisi dan Spesifikasi
# int -> bool, mengembalikan nilai boolean true jika x habis dibagi 400 atau habis dibagi 4
# dan tidak habis dibagi 100, serta false jika tidak memenuhi, dengan domain X > 0 

# Realisasi
def tahun_kabisat(x) :
    return x%400 == 0 or x%4 == 0 and x%100 != 0

print(tahun_kabisat(1945))
print(tahun_kabisat(2000))
