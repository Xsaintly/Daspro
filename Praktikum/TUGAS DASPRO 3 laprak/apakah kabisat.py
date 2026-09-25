def kabisat(x) :
    if x%400 == 0 or x%4 == 0 and x%100 != 0 :
        return 'Tahun Kabisat'
    else :
        return 'Bukan Kabisat'

print(kabisat(1945))
print(kabisat(2000))