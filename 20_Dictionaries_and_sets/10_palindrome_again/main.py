all = dict()
chot = 0
stringer = [i for i in input('Введите строку: ')]
for i in stringer:
    if i not in all:
        all.update({i: 1})
    else:
        all[i] += 1
for i in list(all.items()):
    if i[1] % 2 != 0:
        chot += 1
if chot > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
