def akar_persamaankuadrat1 (a: int, b: int, c: int) -> float :
    return (-b + (b**2 - 4*a*c)**0.5)/(2*a)
def akar_persamaankuadrat2 (a: int, b: int, c: int) -> float :
    return (-b - (b**2 - 4*a*c)**0.5)/(2*a)
def diskriminan (o: int, p: int, q: int) -> float :
    return p**2 - (4*o*q)
def hasil(x,y,z) -> float:
    if x == 0 or diskriminan(x, y, z) < 0 :
        return -999
    elif (akar_persamaankuadrat1(x, y, z) > akar_persamaankuadrat2(x, y, z)) :
        if akar_persamaankuadrat2(x, y, z) == 0 :
            return -999
        return (akar_persamaankuadrat1(x, y, z) / akar_persamaankuadrat2(x, y, z)) 
    elif (akar_persamaankuadrat1(x, y, z) < akar_persamaankuadrat2(x, y, z)) :
        if akar_persamaankuadrat1(x, y, z) == 0 :
            return -999
        return akar_persamaankuadrat2(x, y, z) / akar_persamaankuadrat1(x, y, z) 
    else :
        if akar_persamaankuadrat1(x, y, z) == 0 :
            return -999
        return akar_persamaankuadrat1(x, y, z) / akar_persamaankuadrat2(x, y, z)

print(hasil(2, 3, 4))
print(hasil(7, 3, -4))
print(hasil(8, -110, -4))
print(hasil(-9, 3, -4))
