def segitiga (x: int, y: int, z: int) -> str :
    if x == y == z :
        return 'Sama Sisi'
    elif x == y or y == z or z == x :
        return 'Sama Kaki'
    else :
        return 'Sembarang'
    
print(segitiga(2, 2, 2))
print(segitiga(2, 2, 3))
print(segitiga(3, 4, 5))