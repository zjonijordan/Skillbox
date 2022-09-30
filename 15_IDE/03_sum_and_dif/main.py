"Задача 3. Сумма и разность"
N = str(input("Ведите число: "))
def summa():
    N1 = 0
    for i in N:
        N1 = int(i) + N1
    return N1
def summa2():
    count = 0
    for i in N:
        count += 1
    return count

print("Сумма цифр: ", summa(), "\nКол-во цифр в числе: ", summa2(), "\nРазность суммы и кол-ва цифр: ", summa() - summa2() )



