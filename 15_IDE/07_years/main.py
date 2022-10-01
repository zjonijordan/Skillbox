A = int(input("Введите первый год: "))
B = int(input("Введите второй год: "))
count = 0
A1 = ""
A2 = ""
A3 = ""
A4 = ""
print("Года от", A, "до", B, "с тремя одинаковыми цифрами:")

for i in range (A, B + 1):
    for t in str(i):
        count += 1
        if count > 4:
            count = 1
            A1 = ""
            A2 = ""
            A3 = ""
            A4 = ""
        if count == 1:
            A1 = t
        elif count == 2:
            A2 = t
        elif count == 3:
            A3 = t
        elif count == 4:
            A4 = t
    if A1 == A3 == A4 or A1 == A2 == A4 or A1 == A2 == A3 or A1 == A2 == A3 == A4 or A2 == A3 == A4:
        print(A1 + A2 + A3 + A4)








