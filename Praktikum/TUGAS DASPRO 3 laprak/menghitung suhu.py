def suhu(x: float, y: str) -> float :
    if y == 'reamur' :
        return x*4/5
    elif y == 'fahrenheit' :
        return (x*9/5) + 32
    elif y == 'kelvin' :
        return x + 273

print(suhu(25, 'reamur'))
print(suhu(25, 'fahrenheit'))
print(suhu(25, 'kelvin'))