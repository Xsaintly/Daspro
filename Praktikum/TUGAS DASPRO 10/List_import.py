# Nama file     : List.py
# Nama pembuat  : Muhammad Hanif
# Tanggal       : 17 November 2026
# Deskripsi     : 

"""
DEFINISI DAN SPESIFIKASI KONSTRUKTOR

Konso(E,L), dengan E integer dan L List, menghasilkan sebuah list
dari E dan L dengan E sebagai elemen pertama dari List L.

Konsi(L,E), dengan L List dan E integer, menghasilkan sebuah list
dari L dan E dengan E sebagai elemen terakhir dari List L.
"""

"""
DEFINISI DAN SPESIFIKASI SELEKTOR

FirstElmt(L) mengembalikan elemen pertama dari List L yang tidak kosong.

LastElmt(L) mengembalikan elemen terakhir dari List L yang tidak kosong.

Head(L) mengembalikan List tanpa elemen terakhir dari L yang tidak kosong;
dapat menghasilkan list kosong.

Tail(L) mengembalikan List tanpa elemen pertama dari L yang tidak kosong;
dapat menghasilkan list kosong.
"""

"""
DEFINISI DAN SPESIFIKASI PREDIKAT

IsEmpty(L) bernilai True jika L merupakan List kosong.

IsOneElmt(L) bernilai True jika L merupakan List yang hanya memiliki
tepat 1 elemen.
"""

"""
DEFINISI DAN SPESIFIKASI OPERATOR

NbElmt(L) menghasilkan banyaknya elemen (integer) dari List L.
"""

# REALISASI
def Konso(E,L):
    return [E] + L

def Konsi(L,E):
    return L + [E]

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def IsEmpty(L):
    return L == []

def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []
    
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Head(L))

def IsEqual(L1, L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return True
    elif NbElmt(L1) != NbElmt(L2):
        return False
    else:
        return FirstElmt(L1) == FirstElmt(L2) and IsEqual(Tail(L1), Tail(L2))
