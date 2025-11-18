a = float(input("Введите число: "))
b = float(input("Введите второе число: "))

while True:
    plus = a + b
    minus = a - b
    mult = a * b
    if b != 0:
        div = a / b
    else:
        div = "Ошибка: деление на 0"
    break

print("Сложение:", plus)
print("Вычитание:", minus)
print("Умножение:", mult)
print("Деление:", div)