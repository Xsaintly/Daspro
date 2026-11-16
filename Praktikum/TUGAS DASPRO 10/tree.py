

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
