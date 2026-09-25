def kelayakan_pinjaman(x,y) :
    if x >= 1500000 and y >= 18 :
        return "LAYAK"
    else :
        return "TIDAK LAYAK"

print(kelayakan_pinjaman(1500000, 18))
print(kelayakan_pinjaman(1500000, 15))
