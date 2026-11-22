# Nama      : Muhammad Deren Julian 
# Nim       : 24060126140191
# Tanggal   : 22 November 2026

from List_import import *

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def MakePN(A,C):
    """MakePN(A,C) membuat pohon N-ner dengan A sebagai akar dan C sebagai anak-akannya.
    Bisa berupa daun maupun pohon n-ner utuh"""
    return (A,C)

def Akar(PN):
    """Akar(PN) adalah Akar dari P. Jika P adalah (A, PN) = Akar(P)"""
    return PN[0]

def Anak(PN):
    """Anak(PN) adalah list of pohon N-ner yang merupakan anak anak dari P, 
    dengan P adalah pohon N-ner yang tidak kosong. Jika P adalah (A, PN) = Anak(P) adalah PN"""
    return PN[1]

#DEFINISI DAN SPESIFIKASI PREDIKAT
def IsTreeNEmpty(PN):
    """IsTreeNEmpty(PN) bernilai True jika PN kosong : []"""
    return PN == []

def IsOneElmt(PN):
    """IsOneElmt(PN) bernilai True jika PN hanya terdiri dari akar"""
    return (not IsTreeNEmpty(PN)) and (IsTreeNEmpty(Anak(PN)))

def NBNElmt(PN):
    """NBNElmt(PN) memberikan banyaknya node dari pohon P:
    Basis 0: IsTreeNEmpty((A))=0
    Basis 1: IsOneElmt((A))=1
    Rekurens: NBNElmt((A,PN))= 1+ NBElmtChild(PN)"""
    if IsTreeNEmpty(PN):
        return 0
    elif IsOneElmt(PN):
        return 1
    else:
        return 1 + NBNElmtChild(Anak(PN))

def NBNElmtChild(PN):
    """NBNElmtChild(PN) merekursif list of Pohon N-ner yang merupakan anak anak dari suatu akar:
    Basis 0: IsTreeNEmpty((A)) = 0
    Rekurens: NBNElmtChild(PN) = NBNElmt(FirstElmt(PN)) + NBNElmtChild(TailList(PN))"""
    if IsTreeNEmpty(PN):
        return 0
    else:
        return NBNElmt(FirstElmt(PN)) + NBNElmtChild(Tail(PN))

# --------------------Tugas Latihan-------------------
# Misal diberikan pohon N-ner:
P = (
    (2, [
       (3, [
          (1, []),
          (4, []),
          (5, [
             (9, [])
          ])
       ]),
       (7, [
          (6, []),
          (8, [])
       ])
    ])
)

# NBNDaun: PohonN-ner -> integer >= 0
#  {NBNElmt(P) memberikan banyaknya daun dari pohon P:
#  Basis 0: IsTreeNEmpty((A)) = 0
#  Basis 1: IsOneElmt((A)) = 1
#  Rekurens: NBNDaun((A, PN)) = NBNDaun(PN)}
#  Contoh: 
#  NBNDaun(P) -> 5 
#  {terdapat 5 daun pada pohonN-ner P}

def NBNDaun(P):
    """
    NBNDaun(P) memberikan banyaknya daun dari pohon P:
    Basis 0: IsTreeNEmpty(P) = 0
    Basis 1: IsOneElmt(P) = 1
    Rekurens: NBNDaun((A, PN)) = NBNDaunChild(PN)
    Contoh: NBNDaun(P) -> 5
    """
    # Realisasi
    if IsTreeNEmpty(P):
        return 0
    elif IsOneElmt(P):
        return 1
    else:
        return NBNDaunChild(Anak(P))

def NBNDaunChild(PN):
    """
    NBNDaunChild(PN) menjumlahkan banyak daun dari list of pohon N-ner PN:
    Basis: IsTreeNEmpty(PN) = 0
    Rekurens: NBNDaunChild(PN) = NBNDaun(FirstElmt(PN)) +
              NBNDaunChild(Tail(PN))
    """
    # Realisasi
    if IsTreeNEmpty(PN):
        return 0
    else:
        return NBNDaun(FirstElmt(PN)) + NBNDaunChild(Tail(PN))

# IsMemberPN: PohonN-ner, elemen -> integer >= 0
#  {IsMemberPN(P, X) mengembalikan True jika X merupakan bagian dari P.
#  Basis 0: IsTreeNEmpty((A)) = False
#  Basis 1: IsOneElmt((A)) = A == X
#  Rekurens: IsMember((A, PN)) = IsMemberPN(PN)}
#  Contoh: 
#  IsMemberPN(P, 10) -> False 
#  {Tidak ada 10 pada pohon}
#  IsMemberPN(P, 8) -> True 
#  {Elemen 8 ada pada pohon}

def IsMemberPN(P, X):
    """
    IsMemberPN(P, X) mengembalikan True jika X merupakan bagian dari P.
    Basis 0: IsTreeNEmpty(P) = False
    Basis 1: IsOneElmt(P) = (A == X)
    Rekurens: IsMemberPN((A, PN), X) = (A == X) or IsMemberChild(PN, X)
    Contoh: IsMemberPN(P, 10) -> False ; IsMemberPN(P, 8) -> True
    """
    # Realisasi
    if IsTreeNEmpty(P):
        return False
    elif IsOneElmt(P):
        return Akar(P) == X
    else:
        return (Akar(P) == X) or IsMemberChild(Anak(P), X)

def IsMemberChild(PN, X):
    """
    IsMemberChild(PN, X) True jika X ada pada salah satu pohon di list PN.
    Basis: IsTreeNEmpty(PN) = False
    Rekurens: IsMemberPN(FirstElmt(PN), X) or IsMemberChild(Tail(PN), X)
    """
    # Realisasi
    if IsTreeNEmpty(PN):
        return False
    else:
        return IsMemberPN(FirstElmt(PN), X) or IsMemberChild(Tail(PN), X)

# SumPN: PohonN-ner -> integer
#  {SumPN(P) memberikan jumlah seluruh nilai elemen (node) dari pohon P:
#  Basis 0: IsTreeNEmpty((A)) = 0
#  Basis 1: IsOneElmt((A)) = A
#  Rekurens: SumPN((A, PN)) = A + SumPN(PN)}
#  Contoh:
#  SumPN(P) -> 45
#  {2+3+1+4+5+9+7+6+8 = 45}

def SumPN(P):
    """
    SumPN(P) memberikan jumlah seluruh nilai elemen (node) dari pohon P:
    Basis 0: IsTreeNEmpty(P) = 0
    Basis 1: IsOneElmt(P) = A
    Rekurens: SumPN((A, PN)) = A + SumChild(PN)
    Contoh: SumPN(P) -> 45
    """
    # Realisasi
    if IsTreeNEmpty(P):
        return 0
    elif IsOneElmt(P):
        return Akar(P)
    else:
        return Akar(P) + SumChild(Anak(P))

def SumChild(PN):
    """
    SumChild(PN) menjumlahkan SumPN dari seluruh pohon pada list of pohon N-ner PN:
    Basis: IsTreeNEmpty(PN) = 0
    Rekurens: SumChild(PN) = SumPN(FirstElmt(PN)) + SumChild(Tail(PN))
    """
    # Realisasi
    if IsTreeNEmpty(PN):
        return 0
    else:
        return SumPN(FirstElmt(PN)) + SumChild(Tail(PN))

# TinggiPN: PohonN-ner -> integer >= 0
#  {TinggiPN(P) memberikan tinggi pohon P, yaitu banyaknya node pada
#  lintasan terpanjang dari akar ke daun:
#  Basis 0: IsTreeNEmpty((A)) = 0
#  Basis 1: IsOneElmt((A)) = 1
#  Rekurens: TinggiPN((A, PN)) = 1 + max(TinggiPN(PN))}
#  Contoh:
#  TinggiPN(P) -> 4
#  {lintasan terpanjang: 2 -> 3 -> 5 -> 9}

def TinggiPN(P):
    """
    TinggiPN(P) memberikan tinggi pohon P, yaitu banyaknya node pada
    lintasan terpanjang dari akar ke daun:
    Basis 0: IsTreeNEmpty(P) = 0
    Basis 1: IsOneElmt(P) = 1
    Rekurens: TinggiPN((A, PN)) = 1 + TinggiChild(PN)
    Contoh: TinggiPN(P) -> 4
    """
    # Realisasi
    if IsTreeNEmpty(P):
        return 0
    elif IsOneElmt(P):
        return 1
    else:
        return 1 + TinggiChild(Anak(P))

def TinggiChild(PN):
    """
    TinggiChild(PN) memberikan tinggi terbesar di antara pohon pada list PN:
    Basis: IsTreeNEmpty(PN) = 0
    Rekurens: TinggiChild(PN) = max(TinggiPN(FirstElmt(PN)), TinggiChild(Tail(PN)))
    """
    # Realisasi
    if IsTreeNEmpty(PN):
        return 0
    else:
        return max(TinggiPN(FirstElmt(PN)), TinggiChild(Tail(PN)))

# CountX: PohonN-ner, elemen -> integer >= 0
#  {CountX(P, X) memberikan banyaknya kemunculan X pada pohon P:
#  Basis 0: IsTreeNEmpty((A)) = 0
#  Basis 1: IsOneElmt((A)) = 1 jika A == X, 0 jika A != X
#  Rekurens: CountX((A, PN), X) = (1 jika A == X, 0 jika A != X) + CountX(PN, X)}
#  Contoh:
#  CountX(P, 4) -> 1
#  {elemen 4 muncul satu kali}
#  CountX(P, 10) -> 0
#  {elemen 10 tidak ada pada pohon}

def CountX(P, X):
    """
    CountX(P, X) memberikan banyaknya kemunculan X pada pohon P:
    Basis 0: IsTreeNEmpty(P) = 0
    Basis 1: IsOneElmt(P) = 1 jika A == X, 0 jika A != X
    Rekurens: CountX((A, PN), X) = (1 jika A == X, 0 jika A != X) +
              CountXChild(PN, X)
    Contoh: CountX(P, 4) -> 1 ; CountX(P, 10) -> 0
    """
    # Realisasi
    if IsTreeNEmpty(P):
        return 0
    elif IsOneElmt(P):
        if Akar(P) == X:
            return 1
        else:
            return 0
    else:
        if Akar(P) == X:
            return 1 + CountXChild(Anak(P), X)
        else:
            return CountXChild(Anak(P), X)

def CountXChild(PN, X):
    """
    CountXChild(PN, X) menjumlahkan CountX dari seluruh pohon pada list PN:
    Basis: IsTreeNEmpty(PN) = 0
    Rekurens: CountXChild(PN, X) = CountX(FirstElmt(PN), X) +
              CountXChild(Tail(PN), X)
    """
    # Realisasi
    if IsTreeNEmpty(PN):
        return 0
    else:
        return CountX(FirstElmt(PN), X) + CountXChild(Tail(PN), X)

# MaxPN: PohonN-ner tidak kosong -> elemen
#  {MaxPN(P) memberikan nilai elemen terbesar dari pohon P yang tidak kosong:
#  Basis 1: IsOneElmt((A)) = A
#  Rekurens: MaxPN((A, PN)) = max(A, MaxPN(PN))}
#  Contoh:
#  MaxPN(P) -> 9
#  {nilai terbesar pada pohon adalah 9}

def MaxPN(P):
    """
    MaxPN(P) memberikan nilai elemen terbesar dari pohon P yang tidak kosong:
    Basis 1: IsOneElmt(P) = A
    Rekurens: MaxPN((A, PN)) = max(A, MaxChild(PN))
    Contoh: MaxPN(P) -> 9
    """
    # Realisasi
    if IsOneElmt(P):
        return Akar(P)
    else:
        return max(Akar(P), MaxChild(Anak(P)))

def MaxChild(PN):
    """
    MaxChild(PN) memberikan nilai terbesar dari list of pohon N-ner PN yang tidak kosong:
    Basis: IsTreeNEmpty(Tail(PN)) = MaxPN(FirstElmt(PN))
    Rekurens: MaxChild(PN) = max(MaxPN(FirstElmt(PN)), MaxChild(Tail(PN)))
    """
    # Realisasi
    if IsTreeNEmpty(Tail(PN)):
        return MaxPN(FirstElmt(PN))
    else:
        return max(MaxPN(FirstElmt(PN)), MaxChild(Tail(PN)))

# NBElmtLevel: PohonN-ner, integer >= 1 -> integer >= 0
#  {NBElmtLevel(P, L) memberikan banyaknya node pada level L (integer >= 1)
#  dari pohon P, akar berada pada level 1:
#  Basis 0: IsTreeNEmpty((A)) = 0
#  Basis 1: L == 1 -> 1
#  Rekurens: NBElmtLevel((A, PN), L) = NBElmtLevel(PN, L-1)}
#  Contoh:
#  NBElmtLevel(P, 3) -> 5
#  {level 3 berisi 1, 4, 5, 6, 8}
#  NBElmtLevel(P, 5) -> 0
#  {pohon tidak punya level 5}

def NBElmtLevel(P, L):
    """
    NBElmtLevel(P, L) memberikan banyaknya node pada level L (integer >= 1)
    dari pohon P, akar berada pada level 1:
    Basis 0: IsTreeNEmpty(P) = 0
    Basis 1: L == 1 -> 1
    Rekurens: NBElmtLevel((A, PN), L) = NBElmtLevelChild(PN, L-1)
    Contoh: NBElmtLevel(P, 3) -> 5 ; NBElmtLevel(P, 5) -> 0
    """
    # Realisasi
    if IsTreeNEmpty(P):
        return 0
    elif L == 1:
        return 1
    else:
        return NBElmtLevelChild(Anak(P), L - 1)

def NBElmtLevelChild(PN, L):
    """
    NBElmtLevelChild(PN, L) menjumlahkan NBElmtLevel dari seluruh pohon pada list PN:
    Basis: IsTreeNEmpty(PN) = 0
    Rekurens: NBElmtLevelChild(PN, L) = NBElmtLevel(FirstElmt(PN), L) +
              NBElmtLevelChild(Tail(PN), L)
    """
    # Realisasi
    if IsTreeNEmpty(PN):
        return 0
    else:
        return NBElmtLevel(FirstElmt(PN), L) + NBElmtLevelChild(Tail(PN), L)

# --------------------APLIKASI-------------------
print("NBNElmt(P)        =", NBNElmt(P))
print("NBNDaun(P)        =", NBNDaun(P))
print("IsMemberPN(P, 10) =", IsMemberPN(P, 10))
print("IsMemberPN(P, 8)  =", IsMemberPN(P, 8))
print("SumPN(P)          =", SumPN(P))
print("TinggiPN(P)       =", TinggiPN(P))
print("CountX(P, 4)      =", CountX(P, 4))
print("CountX(P, 10)     =", CountX(P, 10))
print("MaxPN(P)          =", MaxPN(P))
print("NBElmtLevel(P, 3) =", NBElmtLevel(P, 3))
print("NBElmtLevel(P, 5) =", NBElmtLevel(P, 5))