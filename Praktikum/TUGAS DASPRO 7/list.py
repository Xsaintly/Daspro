# Pembuat   : Muhammad Deren Julian
# Nim       : 24060126140191
# Tanggal   : 23 Oktober 2026

def konso(E,L):
    return [E]+L

def konsi(E,L):
    return L+[E]

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def isEmpty(L):
    return L == []

def IsOneElmt(L):
    if isEmpty(L):
        return False
    else:
        return Tail(L)==[] and Head(L)==[]

def NbElmt(L):
    if isEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))


# --------------------Tugas Latihan--------------------  

# ElmtKeN: integer ≥ 0, List -> elemen  
# {ElmtKeN(N, L) menghasilkan elemen ke-N dari list L.}  
def ElmtKeN(N:int, L:list):
    if N == 0 :
     return FirstElmt(L)
    else:
        return ElmtKeN(N-1, Tail(L))

print(2,[8,6,10,12])

# IsMember: elemen, List -> boolean  
# {IsMember(X, L) bernilai True apabila X merupakan elemen dari List.}
def IsMember(X, L):
    if isEmpty(L):
        return False
    else:
        if FirstElmt(L) == X:
            return True
        else:
            return IsMember(X, Tail(L))

print(IsMember(79, [83, 202, 79, 44]))

# Copy: List -> List 
# {Copy(L) menghasilkan List yang identik dengan list asal.} 
def copy(L: list) -> list:
    if isEmpty(L): 
        return[]
    else:
        return konso(FirstElmt(L), copy(Tail(L)))

print(copy([83, 202, 79, 44])) 
  
# Inverse: List -> List  
# {Inverse(L) menghasilkan list L yang dibalik, yaitu   
# yang urutan elemennya adalah kebalikan dari list awal.}  
def inverse(L:list) -> list :
    if isEmpty(L):
        return []
    else:
        konso(inverse(Tail(L)),FirstElmt(L))

print(inverse([2,4,6,8])) 

# Konkat: 2 List -> List  
# {Konkat(L1, L2) menghasilkan List yang merupakan hasil konkatenasi  # list L1 dan L2.} 
def konkat(L1:list, L2:list) -> list :
    return L1 + L2

print(konkat([2,4,6],[8,10,12]))
 
# SumElmt(L): List of integer -> integer  
# {SumElmt(L) menghasilkan bilangan bulat yang merupakan jumlah  # nilai dari seluruh elemen L.}
def SumElmt(L:list)-> int :
    if isEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))
    
print(SumElmt([2,4,6]))
 
# AvgElmt(L): List of integer -> real  
# {AvgElmt(L) menghasilkan bilangan riil yang merupakan rata-rata # nilai dari seluruh elemen L.} 
def AvgElmt(L:list) -> float :
    if isEmpty(L):
        return 0
    else:
        return SumElmt(L)/NbElmt(L)

print(AvgElmt([2,4,6]))

# MaxElmt(L): List of integer -> integer  
# {MaxElmt(L) mengembalikan elemen dengan nilai maksimum dari list L.}  
def MaxElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        if FirstElmt(L) > MaxElmt(Tail(L)):
            return FirstElmt(L)
        else:
            return MaxElmt(Tail(L))

print(MaxElmt([83, 202, 79, 44]))
 
# MaxNB: List of integer -> = 1> # {MaxNB(L) menghasilkan tipe bentukan yang berisikan bilangan maksimum 
# pada list L dan seberapa banyak bilangan itu muncul di dalam list.} 
# Fungsi bantu: CountElmt(X, L) -> banyaknya kemunculan X di L
def CountX(X, L):
    if isEmpty(L):
        return 0
    else:
        if FirstElmt(L) == X:
            return 1 + CountX(X, Tail(L))
        else:
            return CountX(X, Tail(L))

def MaxNB(L: list) -> tuple:
    return (MaxElmt(L), CountX(MaxElmt(L), L))

print(MaxNB([83, 202, 202, 79, 44, 202]))

# AddList: 2 List of integer -> List  
# {AddList(L1, L2) menghasilkan list baru yang setiap elemennya adalah  # hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama.}  
def AddList(L1:list, L2:list) -> list :
    if isEmpty(L1) and isEmpty(L2):
        return []
    else:
        return konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

print(AddList([12,4,2,6], [1,3,5,7]))

# IsPalindrom: List of character -> boolean  
# {IsPalindrom(L) bernilai True jika L merupakan kata palindrom, # yakni kata yang sama jika dibaca dari kiri atau kanan.} 
def IsPalindrom(L: list) -> bool:
    if isEmpty(L) or IsOneElmt(L):
        return True
    else:
        return FirstElmt(L) == LastElmt(L) and IsPalindrom(Tail(Head(L)))

print(IsPalindrom(['k', 'a', 't', 'a', 'k']))

# IsEqual: 2 List -> boolean 
# {IsEqual(L1,L2) true jika dan hanya jika kedua list sama, yaitu setiap elemen dan urutan kemunculannya sama} 
def IsEqual(L1, L2):
    if isEmpty(L1) and isEmpty(L2):
        return True
    elif isEmpty(L1) or isEmpty(L2):
        return False
    else:
        return FirstElmt(L1) == FirstElmt(L2) and IsEqual(Tail(L1), Tail(L2))

print(IsEqual([1, 2, 3], [1, 2, 3]))

# MinElmt: List of integer (tidak kosong) -> integer 
# {MinElmt(L) mengembalikan elemen dengan nilai minimum dari list L.}
def MinElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        if FirstElmt(L) < MinElmt(Tail(L)):
            return FirstElmt(L)
        else:
            return MinElmt(Tail(L))
      
print(MinElmt([83, 202, 79, 44])) 
 
# CountN: character, list of character -> integer 
# {CountN(C, T) menghasilkan banyaknya kemunculan karakter C pada list of character (T)}
def CountN(C, T):
    if isEmpty(T):
        return 0
    elif FirstElmt(T) == C:
        return 1 + CountN(C, Tail(T))
    else:
        return CountN(C, Tail(T))

print(CountN('a', ['a', 'b', 'a', 'c', 'a'])) 
 
# Atleast: integer > 0, character, list of character -> boolean 
# {Atleast (N,C,T) benar, jika karakter C minimal muncul N kali pada list of character (T)}
def Atleast(N, C, T):
    return CountN(C, T) >= N

print(Atleast(3, 'a', ['a', 'b', 'a', 'c', 'a'])) 
 
# IsXElmtKeN (N,L) :elemen, integer ≥ 0, List (tidak kosong) → boolean  
# {IsXElmtKeN (L) true jika X adalah elemen ke-N list L, N ≥ 0, dan N ≤ banyaknya elemen list, false jika tidak} 
def IsXElmtKeN(X, N, L):
    if N >= NbElmt(L):
        return False
    else:
        return ElmtKeN(N, L) == X

print(IsXElmtKeN(79, 2, [83, 202, 79, 44]))

# DelFirstElmt(Li) mengembalikan list L tanpa elemen→ pertamanya. kondisi: List L tidak kosong.}
# DelFirstElmt: List of integer (tidak kosong) 	 List of integer 
def DelFirstElmt(L):
    return Tail(L)

print(DelFirstElmt([83, 202, 79, 44]))

# MultiRember: elemen, List -> List  
# {MultiRember(X, L) menghapus seluruh kemunculan elemen X dari list L.}
def MultiRember(X, L):
    if isEmpty(L):
        return []
    else:
        if FirstElmt(L) == X:
            return MultiRember(X, Tail(L))
        else:
            return konso(FirstElmt(L), MultiRember(X, Tail(L)))

print(MultiRember(2, [1, 2, 3, 2, 4, 2])) 

#CountGenap: List of Integer -> integer 
# {CountGenap(L) menghasilkan banyaknya elemen bernilai genap dalam list L.}
def CountGenap(L):
    if isEmpty(L):
        return 0
    else:
        if FirstElmt(L) % 2 == 0:
            return 1 + CountGenap(Tail(L))
        else:
            return CountGenap(Tail(L))

print(CountGenap([83, 202, 79, 44])) 

# IndexOf: integer, list of integer -> integer 
# {IndexOf(X, Li) menghasilkan indeks (dimulai dari 0) kemunculan pertama X di list L. Jika Xx tidak ada di L, hasilnya -1.}
def IndexOf(X: int, L: list) -> int:
    if isEmpty(L):
        return -1
    elif FirstElmt(L) == X:
        return 0
    else:
        if IndexOf(X, Tail(L)) == -1:
            return -1
        else:
            return 1 + IndexOf(X, Tail(L))

print(IndexOf(79, [83, 202, 79, 44])) 
