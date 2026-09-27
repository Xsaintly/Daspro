def MakeP(x, y):
    return (x, y)

def Pemb(p):
    return p[0]
 
def Peny(p):
    return p[1]
 
def AddP(P1, P2):
    return (Pemb(P1)*Peny(P2) + Pemb(P2)*Peny(P1), Peny(P1)*Peny(P2))
 
def SubP(P1, P2):
    return (Pemb(P1)*Peny(P2) - Pemb(P2)*Peny(P1), Peny(P1)*Peny(P2))
 
def MulP(P1, P2):
    return (Pemb(P1)*Pemb(P2), Peny(P1)*Peny(P2))
 
def DivP(P1, P2):
    return (Pemb(P1)*Peny(P2), Peny(P1)*Pemb(P2))
 
def RealP(P):
    return Pemb(P) / Peny(P)
 
def IsEqP(P1, P2):
    return Pemb(P1)*Peny(P2) == Peny(P1)*Pemb(P2)
 
def IsLtP(P1, P2):
    return Pemb(P1)*Peny(P2) < Peny(P1)*Pemb(P2)
 
def IsGtP(P1, P2):
    return Pemb(P1)*Peny(P2) > Peny(P1)*Pemb(P2)


print("AddP:", AddP((1, 2), (1, 4)))
print("SubP:", SubP((1, 3), (1, 5)))
print("MulP:", MulP((1, 4), (1, 6)))
print("DivP:", DivP((1, 5), (1,7)))
print("RealP:", RealP((1, 6)))
print("IsEqP?:", IsEqP((1, 7), (1, 8)))
print("IsLtP?:", IsLtP((1, 8), (1, 9)))
print("IsGtP?:", IsGtP((1, 9), (1, 10)))