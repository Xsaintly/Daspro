# Nama      : Muhammad Deren Julian 
# nim       : 24060126140191
# Tanggal   : 9 November 2026

from tugas_list import *

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
 


# --------------------Tugas Latihan--------------------  
# IsMemberS: elemen, list of list -> boolean 
# {IsMemberS(x,S) mengembalikan true jika elemen x ada di dalam list of list S. 
def isMemberS(X, L) -> bool:
    if isEmpty(L):
        return False
    if isList(firstList(L)):
        return isMemberS(X, firstList(L)) or isMemberS(X, tailList(L))
    return X == firstList(L) or isMemberS(X, tailList(L))
# Contoh aplikasi:  
print(isMemberS(3, [])) #-> False  
print(isMemberS(3, [2, 4, 3, [1], [4,5]])) #-> True  
print(isMemberS(3, [2, 4, 7, [1], [3,5]])) #-> True  

# RemberList: elemen, List of List -> List of List  
# {RemberList(x,S) menghapus semua elemen x yang ada di list of list S. 
# Contoh aplikasi:  
# Rember*(3, []) -> []  
# Rember*(3, [4, 3, [2,4], 3]) -> [4, [2,4]]  
# Rember*(3, [2, 4, [3,6,9], 5, 3]) -> [2, 4, [6,9], 5]  

# MaxLOL: List of List -> elemen  
# {MaxLOL(S) mengembalikan elemen maksimum di dalam list of list S. 
# Contoh aplikasi:  
# Max([4, 5, 6, [8,9,10], [12,0], 8]) -> 12  
# Max([4, 15, 6, [8,9,10], [12,0], 8]) -> 15  

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
# Contoh aplikasi:  
# SumLoL([[]]) -> 0  
# SumLoL([4, 5, 6, [2, 3, 1]]) -> 21  
# SumLoL([[2, 3, 4]]) -> 9  
 
# MaxNBElmtList: List of List -> integer  
# {MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S.  
# Contoh aplikasi:  
# MaxNBElmtList([[4,5,6,7], [8,9,10], [12,0], 8]) -> 4  
# MaxNBElmtList([[4,15], 6, [8, 9], 10, [12], 8]) -> 2  
# MaxNBElmtList([8, 9, 10]) -> 0  
 
# MaxSumElmt: List of List -> integer  
# {MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S;  
# Jika elemen berupa list, maka dihitung sum dari elemen dalam list tersebut;  
# Jika elemen berupa atom, maka nilainya adalah elemen tersebut. 
        
# Contoh aplikasi:  
#print(MaxSumElmt([[1, 2], 9, [4, 5, 6], 8])) #-> 15 
# MaxSumElmt([1, 2], 90, [4, 5, 6], 8]) -> 90  
# MaxSumElmt([8, 9, 10]) -> 10  
# MaxSumElmt([[8, 9, 10]]) -> 27 
 
 
