def hampir_sama(x, y) -> bool :
    return abs(x - y) <= 0.05

print(hampir_sama(36.50, 36.53))
print(hampir_sama(36.50, 36.60))