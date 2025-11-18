a = int(input("Введите число: "))
b = int(input("Второе число: "))

while b != 0:
    remainder = a % b     # настоящий остаток
    a = b                 # сдвигаем
    b = remainder         # новое b — остаток

print("НОД =", a)