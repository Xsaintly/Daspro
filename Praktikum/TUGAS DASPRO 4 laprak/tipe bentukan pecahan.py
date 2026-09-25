def MakeP(x, y):
    return (x, y)

def Pemb(p):
    return p[0]

def Peny(p):
    return p[1]

# Operator (3)
def AddP(P1, P2):
    return MakeP(Pemb(P1)*Peny(P2) + Pemb(P2)*Peny(P1), Peny(P1)*Peny(P2))

def SubP(P1, P2):
    return MakeP(Pemb(P1)*Peny(P2) - Pemb(P2)*Peny(P1), Peny(P1)*Peny(P2))

def MulP(P1, P2):
    return MakeP(Pemb(P1)*Pemb(P2), Peny(P1)*Peny(P2))

# Predikat (3)
def IsEqP(P1, P2):
    return Pemb(P1)*Peny(P2) == Peny(P1)*Pemb(P2)

def IsLtP(P1, P2):
    return Pemb(P1)*Peny(P2) < Peny(P1)*Pemb(P2)

def IsGtP(P1, P2):
    return Pemb(P1)*Peny(P2) > Peny(P1)*Pemb(P2)


# Contoh pemakaian
P1 = MakeP(1, 2)
P2 = MakeP(1, 3)

print("AddP:", AddP(P1, P2))
print("SubP:", SubP(P1, P2))
print("MulP:", MulP(P1, P2))
print("IsEqP?:", IsEqP(P1, P2))
print("IsLtP?:", IsLtP(P1, P2))
print("IsGtP?:", IsGtP(P1, P2))