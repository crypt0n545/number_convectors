a = int(input("Введите число: "))
delitel = 1
result = ""
while delitel <= a:
    if a % delitel == 0:
        result += str(delitel)
        delitel += 1
    else:
        delitel += 1
print(result)