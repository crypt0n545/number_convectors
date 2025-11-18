# Ввод числа
a = int(input("Введите число: "))

# Инициализация строк для разных систем счисления
binary = ""
octal = ""
hexadecimal = ""

# Копии числа для разных систем
b = a
c = a

# Двоичное
while a != 0:
    binary += str(a % 2)
    a //= 2

# Восьмеричное
while b != 0:
    octal += str(b % 8)
    b //= 8

# Шестнадцатеричное
while c != 0:
    digit = c % 16
    if digit < 10:
        hexadecimal += str(digit)
    else:
        # 10 -> A, 11 -> B, ..., 15 -> F
        hexadecimal += chr(ord('A') + digit - 10)
    c //= 16

# Вывод результатов в правильном порядке
print("Двоичное:", binary[::-1])
print("Восьмеричное:", octal[::-1])
print("Шестнадцатеричное:", hexadecimal[::-1])
