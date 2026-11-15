# Nama      : Muhammad Deren Julian 
# nim       : 24060126140191
# Tanggal   : 9 November 2026

from tugas_list_copy import *

# DEFINISI DAN SPESIFIKASI PREDIKAT KHUSUS LIST  
# isEmpty: List of List -> boolean  
# {isEmpty(S) benar jika S adalah list of list kosong.}  
# Realisasi:  
def isEmpty(S: list[list]) -> bool:  
    return not S 
 
# isAtom: List of List -> boolean  
# {isAtom(S) benar jika S adalah sebuah atom/elemen tunggal.}  
# Realisasi:  
def isAtom(S: list[list]) -> bool:  
    return type(S) != list  

# isList: List of List -> boolean  
# {isList(S) benar jika S adalah sebuah list.}  
# Realisasi:  
def isList(S: list[list]) -> bool:  
    return type(S) == list  
 
#Definisi dan Spesifikasi Konstruktor List of List  
#Untuk membedakan dengan konstruktor List biasa, tambahkan fungsi-fungsi berikut: 

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR  
# konsLo: List, List of List -> List of List  
# {konsLo(L, S) membentuk list baru dengan list (L) sebagai   
# elemen pertama list of list (S).}  
# Realisasi:  
def konsLo(L: list, S : list[list])-> list[list]: 
    return [L] + S  

# konsLi: List of List, List -> List of List  
# {konsLi(S, L) membentuk list baru dengan list (L) sebagai   
# elemen terakhir list of list (S).}  
# Realisasi:  
def konsLi(S : list[list], L: list)-> list[list]:  
    return S + [L]  
 
#Definisi dan Spesifikasi Selektor List of List  
#Untuk membedakan dengan selektor List biasa, tambahkan fungsi-fungsi berikut:  
 
# DEFINISI DAN SPESIFIKASI SELEKTOR  
# firstList: List of List tidak kosong -> List  
# {firstList(S) menghasilkan elemen pertama list (mungkin sebuah list atau atom).} 
# Realisasi:  
def firstList(S: list[list])-> list:  
    return S[0]  

# lastList: List of List tidak kosong -> List  
# {lastList(S) menghasilkan elemen terakhir list(mungkin sebuah list atau atom).} 
# Realisasi:  
def lastList(S : list[list])-> list:  
    return S[-1] 
 
# tailList: List of List tidak kosong -> List of List  
# {tailList(S) menghasilkan sisa list of list S tanpa elemen pertamanya.}  
# Realisasi:  
def tailList(S : list[list])-> list[list]:  
    return S[1:]  

# headList: List of List tidak kosong -> List of List  
# {headList(S) menghasilkan sisa list of list S tanpa elemen terakhirnya.}  
# Realisasi: 
def headList(S: list[list])-> list[list]:  
    return S[:-1] 

# Max2: 2 elemen -> elemen
# {Max2(A, B) menghasilkan nilai yang lebih besar dari A dan B.
# Jika salah satunya None, menghasilkan yang lain.
# Fungsi bantu untuk MaxLOL, MaxNBElmtList, dan MaxSumElmt.
# Realisasi:
def Max2(A, B):
    if A is None:
        return B
    elif B is None:
        return A
    elif A > B:
        return A
    else:
        return B

# NilaiElmt: elemen atau List of List -> integer
# {NilaiElmt(E) menghasilkan E jika E atom, atau jumlah seluruh elemen E jika E list.
# Fungsi bantu untuk MaxSumElmt.
# Contoh aplikasi:
# NilaiElmt(7) -> 7
# NilaiElmt([1, 2, 3]) -> 6
# }
# Realisasi:
def NilaiElmt(E):
    if isAtom(E):
        return E
    else:
        return SumLoL(E)
 


# --------------------Tugas Latihan--------------------  
# IsMemberS: elemen, list of list -> boolean 
# {IsMemberS(x,S) mengembalikan true jika elemen x ada di dalam list of list S. 
def IsMemberS(x, S:list) -> bool:
    if isEmpty(S):
        return False
    elif isAtom(firstList(S)):
        if firstList(S) == x:
            return True
        else:
            return IsMemberS(x, tailList(S))
    else:
        return IsMemberS(x, firstList(S)) or IsMemberS(x, tailList(S))
# Contoh aplikasi:  
print(IsMemberS(3, [])) #-> False  
print(IsMemberS(3, [2, 4, 3, [1], [4,5]])) #-> True  
print(IsMemberS(3, [2, 4, 7, [1], [3,5]])) #-> True  

# RemberList: elemen, List of List -> List of List  
# {RemberList(x,S) menghapus semua elemen x yang ada di list of list S.
def RemberList(x, S):
    if isEmpty(S):
        return []
    elif isAtom(firstList(S)):
        if firstList(S) == x:
            return RemberList(x, tailList(S))
        else:
            return konso(firstList(S), RemberList(x, tailList(S)))
    else:
        return konsLo(RemberList(x, firstList(S)), RemberList(x, tailList(S)))
# Contoh aplikasi:  
print(RemberList(3, [])) #-> []  
print(RemberList(3, [4, 3, [2,4], 3])) #-> [4, [2,4]]  
print(RemberList(3, [2, 4, [3,6,9], 5, 3])) #-> [2, 4, [6,9], 5]  

# MaxLOL: List of List -> elemen  
# {MaxLOL(S) mengembalikan elemen maksimum di dalam list of list S. 
def MaxLOL(S):
    if isEmpty(S):
        return None
    elif isAtom(firstList(S)):
        return Max2(firstList(S), MaxLOL(tailList(S)))
    else:
        return Max2(MaxLOL(firstList(S)), MaxLOL(tailList(S)))
# Contoh aplikasi:  
print(MaxLOL([4, 5, 6, [8,9,10], [12,0], 8])) #-> 12  
print(MaxLOL([4, 15, 6, [8,9,10], [12,0], 8])) #-> 15  

# NBElmtAtom: List of List -> integer  
# {NBElmtAtom(S) mengembalikan banyaknya elemen list of list S yang berupa atom.
def NBElmtAtom(S:list) -> int :
    if S == []:
        return 0
    elif isAtom(S[0]) == True :
        return 1 + NBElmtAtom(tailList(S))
    else:
        return 0 + NBElmtAtom(tailList(S))
# Contoh aplikasi:  
print(NBElmtAtom([4, 5, 6, [8, 9, 10], [12, 0], 8])) #-> 4  
print(NBElmtAtom([4, 15, 6, [8, 9], 10, [12], 8])) #-> 5  
print(NBElmtAtom([[8, 9, 10]])) #-> 0  

# NBElmtList: List of List -> integer  
# {NBElmtList(S) mengembalikan banyaknya elemen list of list S yang berupa list. 
def NBElmtList(S:list) -> int :
    if S == []:
        return 0
    elif isList(S[0]) == True :
        return 1 + NBElmtList(tailList(S))
    else:
        return 0 + NBElmtList(tailList(S))
# Contoh aplikasi:  
print(NBElmtList([4, 5, 6, [8, 9, 10], [12, 0], 8])) #-> 2  
print(NBElmtList([[4, 15], 6, [8, 9], 10, [12], 8])) #-> 3  
print(NBElmtList([[8, 9, 10]])) #-> 1  
 
# SumLoL: List of List -> integer  
# {SumLoL(S) mengembalikan jumlah semua elemen dalam list of list S. 
def SumLoL(S:list) -> int:
    if isEmpty(S):
        return 0
    elif isAtom(firstList(S)):
        return firstList(S) + SumLoL(tailList(S))
    else:
        return SumLoL(firstList(S)) + SumLoL(tailList(S))
# Contoh aplikasi:  
print(SumLoL([[]])) #-> 0  
print(SumLoL([4, 5, 6, [2, 3, 1]])) #-> 21  
print(SumLoL([[2, 3, 4]])) #-> 9 
 
# MaxNBElmtList: List of List -> integer  
# {MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S.  
# Realisasi MaxNBElmtList:
def MaxNBElmtList(S:list) -> int:
    if isEmpty(S):
        return 0
    elif isAtom(firstList(S)):
        return MaxNBElmtList(tailList(S))
    else:
        return Max2(MaxNBElmtList(firstList(S)), MaxNBElmtList(tailList(S)))
# Contoh aplikasi:  
print(MaxNBElmtList([[4,5,6,7], [8,9,10], [12,0], 8])) #-> 4  
print(MaxNBElmtList([[4,15], 6, [8, 9], 10, [12], 8])) #-> 2  
print(MaxNBElmtList([8, 9, 10])) #-> 0   
 
# MaxSumElmt: List of List -> integer  
# {MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S;  
# Jika elemen berupa list, maka dihitung sum dari elemen dalam list tersebut;  
# Jika elemen berupa atom, maka nilainya adalah elemen tersebut. 
def MaxSumElmt(S:list) -> int:
    if isEmpty(S):
        return None
    else:
        return Max2(NilaiElmt(firstList(S)), MaxSumElmt(tailList(S)))
# Contoh aplikasi:  
print(MaxSumElmt([[1, 2], 9, [4, 5, 6], 8])) #-> 15 
print(MaxSumElmt([[1, 2], 90, [4, 5, 6], 8])) #-> 90  
print(MaxSumElmt([8, 9, 10])) #-> 10  
print(MaxSumElmt([[8, 9, 10]])) #-> 27 
 
 
