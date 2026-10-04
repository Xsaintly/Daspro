# Definisi Tipe
# type Waktu: <menit: int, detik: int>
# { <menit, detik> adalah tipe bentukan waktu shift Ahmad. }
type Waktu = tuple[int, int]

# --------------------------------------------------------------------
# Definisi dan Spesifikasi Konstruktor
# BuatWaktu: 2 integer -> Waktu
# { <menit, detik> membentuk tipe data Waktu dari input (menit, detik). }
# Realisasi:
def makewaktu (menit: int, detik: int) -> Waktu :
    if 0 <= menit < 60 and 0 <= detik < 60:
        return (menit,detik)
    else:
        raise ValueError("Waktu tidak valid")

# --------------------------------------------------------------------
# Definisi dan Spesifikasi Selektor
# AmbilMenit(w): Waktu -> int
#     { mengembalikan menit dari waktu (w). }
# AmbilDetik(w): Waktu -> int
#     { mengembalikan detik dari waktu (w). }
# Realisasi:
def ambilmenit(m) -> int:
    return m[0]
    
def ambildetik(d) -> int :
    return d[1]

def ApakahPindahTempat(waktu: Waktu) -> bool:
    return ambildetik(waktu) == 0

def ApakahJamRawan(waktu1: Waktu) -> bool:
    return ambilmenit(waktu1) % 24 == 0

def ApakahIstirahat(waktu: Waktu) -> bool:
    return ambildetik(waktu) == 0

def ApakahMomenSangatAman(waktu: Waktu) -> bool:
    if ApakahPindahTempat(waktu):
        return True
    if ApakahJamRawan(waktu):
        return True
    if ApakahIstirahat(waktu):
        return True
    return ApakahIstirahat((59, 59))


print(ApakahPindahTempat((10, 7)))
print(ApakahPindahTempat((10, 9)))
print(ApakahJamRawan((4, 16)))
print(ApakahJamRawan((3, 16)))
print(ApakahIstirahat((30, 0)))
print(ApakahIstirahat((5, 0)))
print(ApakahMomenSangatAman((4, 16)))
