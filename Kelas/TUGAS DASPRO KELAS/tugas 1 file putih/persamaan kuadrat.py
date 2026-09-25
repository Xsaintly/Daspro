# Nama File : Apakah huruf A
# Pembuat   : Muhammad Deren Julian
# Tanggal   : 7 September 2026
# Deskripsi : menghitung ekspresi aljabar (b^2 - 2ac)/a^2 berdasarkan tiga parameter koefisien
# persamaan kuadrat

# Definisi dan Spesifikasi
# float, float, float -> float, menghasilkan nilai keluaran float dari formula (b**2 - 2*a*c)
# / (a**2), dengan masukan a, b , bertipe float dan batasan domain a !=0

# Realisasi
def jumlah_akar_kuadrat(a: float, b: float, c: float) -> float :
    return (b**2 - 2 * a * c) / (a**2)

print(jumlah_akar_kuadrat(5, 10, 6))
print(jumlah_akar_kuadrat(5, 11, 6))
