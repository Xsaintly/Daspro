# Nama File : Apakah huruf A
# Pembuat   : Muhammad Deren Julian
# Tanggal   : 7 September 2026
# Deskripsi : Mengonversi durasi waktu dari satuan jam,menit,dan detik
# ke dalam satuan detik

# Definisi dan Spesifikasi
# int, int, int -> int, mengembalikan nilai integer total detik dari penjumlahan
# jam,menit,dan detik, dengan domain jam >= 0, 0<= menit < 60, dan 0 <= detik < 60

# Realisasi
def konversi_waktu (jam: int, menit: int, detik: int) -> int :
    return (jam*3600) + (menit*60) + (detik)

print(konversi_waktu(6, 50, 20))
print(konversi_waktu(7, 100, 30))