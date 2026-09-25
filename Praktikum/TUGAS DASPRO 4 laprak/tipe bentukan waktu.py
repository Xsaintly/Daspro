type Waktu = tuple[int, int, int]

def MakeWaktu(jam: int, menit: int, detik: int) -> Waktu:
    return (jam, menit, detik)
def GetJam(W: Waktu) -> int:
    return W[0]
def GetMenit(W: Waktu) -> int:
    return W[1]
def GetDetik(W: Waktu) -> int:
    return W[2]
def DetikSinceMidnight(W: Waktu) -> int:
    return (GetJam(W) * 3600) + (GetMenit(W) * 60) + GetDetik(W)
def IsHalfDay(W: Waktu) -> bool:
    return (DetikSinceMidnight(W) == 12 * 3600)
def IsBefore(W1: Waktu, W2: Waktu) -> bool:
    return (DetikSinceMidnight(W1) < DetikSinceMidnight(W2))
def IsAfter(W1: Waktu, W2: Waktu) -> bool:
    return (DetikSinceMidnight(W1) > DetikSinceMidnight(W2))


print (DetikSinceMidnight((7,30,15)))
print (IsHalfDay((12,0,0)))
print (IsHalfDay((12,0,1)))
print (IsBefore(
    (7,30,15),
    (8,10,0)
))
print (IsAfter(
    (8,10,0),
    (7,30,15)
))