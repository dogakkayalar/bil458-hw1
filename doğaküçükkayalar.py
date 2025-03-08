def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))
num3 = float(input("Üçüncü sayıyı girin: "))

print("En büyük sayı:", find_largest(num1, num2, num3))