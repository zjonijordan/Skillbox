cage = int(input("Кол-во клеток: "))
cage_new = []

for i in range(1, cage + 1):
    effect = int(input('Эффективность ' + str(i) + " клетки: "))
    if effect < i:
        cage_new.append(effect)

print("Неподходящие значения: ", cage_new)


