# Nama File : ipk mahasiswa
# Pembuat   : Muhammad Deren Julian
# Tanggal   : 7 September 2026
# Deskripsi : mementukan status kelayakan predikat cumlaude berdasarkan nilai ipk 
# dan lama masa studi dalam bulan

# Definisi dan Spesifikasi
# float,int -> bool, mengembalikan nilai boolean true jika 3.50 <= ipk <= 4.00 dan bulan <= 54, dengan domain
# 0.0 <= ipk <= 4.00 dan bulan >= 0

# Realisasi
def mahasiswa_cumlaude(ipk: float, bulan: int) -> bool :
    return 3.50 <= ipk <= 4.00 and bulan <= 54

print(mahasiswa_cumlaude(3.60, 50))
print(mahasiswa_cumlaude(3.40, 20))
print(mahasiswa_cumlaude(5.00, 30))