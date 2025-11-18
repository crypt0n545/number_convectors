a = float(input("Введите число: "))
int_part = int(a)
frack_part = a - int_part

if frack_part >= 0.5:
    int_part += 1

print(int_part)
