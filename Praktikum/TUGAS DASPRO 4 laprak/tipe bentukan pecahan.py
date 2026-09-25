type Point = tuple[int, int]
def MakePoint(x:float, y:float) -> Point:
    return (x,y)
def GetAbsis(P: Point) -> float:
    return P[0]
def GetOrdinat(P: Point) -> float:
    return P[1]
def PanjangGaris (Titik1: Point, Titik2: Point) -> float:
    return ((GetAbsis(Titik2) - (GetAbsis(Titik1)))**2 + ((GetOrdinat(Titik2) - GetOrdinat(Titik1)))**2)**0.5 

def Gradien(Titik1: Point, Titik2: Point) -> float:
    return ((GetOrdinat(Titik2) - (GetOrdinat(Titik1))) / (GetAbsis(Titik2) - (GetAbsis(Titik1))))
def IsSejajar(Titik1: Point, Titik2: Point, Titik3: Point, Titik4: Point) -> float:
    return(
        ((Gradien(Titik1, Titik2)) == (Gradien(Titik3, Titik4))) and ((PanjangGaris(Titik1, Titik2)) == (PanjangGaris(Titik3, Titik4)))
    )

print (PanjangGaris((0,0), (3,4)))
print (Gradien((0,0), (3,4)))
print (IsSejajar(
    (3,4),
    (4,10),
    (5,4),
    (9,10)
    
))