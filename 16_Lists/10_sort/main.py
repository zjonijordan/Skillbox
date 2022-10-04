N = [1, 4, -3, 0, 10]
Flag = True

print("Изначальный список:", N)
while Flag == True:
    Flag = False
    for index in range(len(N)):
        if (index + 1 <= len(N) - 1) and (N[index] > N[index + 1]):
            Flag = True
            N[index], N[index + 1] = N[index + 1], N[index]

print("Отсортированный список:", N)

