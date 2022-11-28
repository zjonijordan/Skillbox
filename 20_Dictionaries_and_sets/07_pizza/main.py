all = dict()
for _ in range(int(input("Введите кол-во заказов: "))):
    zakaz = input(str(_ + 1) + " заказ: ").split()
    if zakaz[0] in all:
        for i in list(all[zakaz[0]][0]):
            if i == zakaz[1]:
                all[zakaz[0]][0][zakaz[1]] += int(zakaz[2])
            else:
                all[zakaz[0]][0].setdefault(zakaz[1], zakaz[2])
    else:
        all.update({zakaz[0]: [{str(zakaz[1]): int(zakaz[2])}]})
for i in all:
    print(i, ':')
    for u in all[i]:
        for p, t in u.items():
            print(7 * ' ', str(p) + ':', t)