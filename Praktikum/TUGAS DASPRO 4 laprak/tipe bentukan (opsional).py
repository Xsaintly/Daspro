#==tuple==#
type mahasiswa = tuple [str, str, str, float]

#==konstruktor==#
def mahasiswa(nama:str,nim:str,ttl:str,ipk:float)->mahasiswa:
    return (nama,nim,ttl,ipk)

#==selektor==#
def get_nama(nama:mahasiswa) -> str:
    return nama[0]
def get_nim(nim:mahasiswa) -> str:
    return nim[1]
def get_ttl(ttl:mahasiswa)->str:
    return ttl[2]
def get_ipk(ipk:mahasiswa) ->float:
    return ipk[3]

#==fungsi penghitung==##
def max_2(m1:mahasiswa,m2:mahasiswa)->mahasiswa:
    return m1 if get_ipk(m1) >= get_ipk(m2) else m2

def min_2(m1:mahasiswa,m2:mahasiswa)-> mahasiswa:
    return m1 if get_ipk(m1) <= get_ipk(m2) else m2

#==Fungsi Utama==#
def max_ipk(mhs1, mhs2, mhs3, mhs4, mhs5, mhs6, mhs7) -> mahasiswa:
    return max_2(mhs1, max_2(mhs2, max_2(mhs3, max_2(mhs4, max_2(mhs5, max_2(mhs6, mhs7)))))) 

def min_ipk(mhs1, mhs2, mhs3, mhs4, mhs5, mhs6, mhs7) -> mahasiswa:
    return min_2(mhs1, min_2(mhs2, min_2(mhs3, min_2(mhs4, min_2(mhs5, min_2(mhs6, mhs7))))))

def is_cumlaude(mhs:mahasiswa)->bool:
    return get_ipk(mhs) >= 3.50


#==Input==#
print(get_nama(
    max_ipk(
        mahasiswa("yanto", "24060123", "12-10-2000", 3.9),
        mahasiswa("andri", "24060523", "12-10-2000", 2.9),
        mahasiswa("yanti", "24060623", "12-10-2000", 4.0),
        mahasiswa("budi", "24060723", "12-10-2000", 3.1),
        mahasiswa("pendi", "24060823", "12-10-2000", 3.2),
        mahasiswa("karman", "24060923", "12-10-2000", 3.3),
        mahasiswa("karno", "24060223", "10-09-2001", 3.4)
    )
))

# 2. Mencari nama mahasiswa dengan IPK Terendah
print(get_nama(
    min_ipk(
        mahasiswa("yanto", "24060123", "12-10-2000", 3.9),
        mahasiswa("andri", "24060523", "12-10-2000", 2.9),
        mahasiswa("yanti", "24060623", "12-10-2000", 4.0),
        mahasiswa("budi", "24060723", "12-10-2000", 3.1),
        mahasiswa("pendi", "24060823", "12-10-2000", 3.2),
        mahasiswa("karman", "24060923", "12-10-2000", 3.3),
        mahasiswa("karno", "24060223", "10-09-2001", 3.4)
    )
))

# 3. Mengecek status cumlaude (gunakan konstruktor juga)
print(is_cumlaude(
    mahasiswa("yanto", "24060123", "12-10-2000", 3.9)
))