import random

stick = ["I" for _ in range(int(input("Кол-во палок: ")))]
throw = int(input("Кол-во бросков: "))

count = 0
while count != throw:
    count += 1
    L = random.randint(1, len(stick))
    R = random.randint(L, len(stick))
    print("Бросок " + str(count + 1) + ". Сбиты палки с номера " + str(L) + " по номер " + str(R))
    for i in range(len(stick)):
        count2 = L - 1
        if L == R:
            stick[count2] = "."
        elif L == len(stick) or R == len(stick):
            stick[len(stick)] = "."
        else:
            while count2 != R:
                count2 += 1
                stick[count2 - 1] = "."
print(str(stick))