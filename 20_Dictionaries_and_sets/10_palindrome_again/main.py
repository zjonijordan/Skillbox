all = dict()
stringer = [i for i in input('Введите строку: ')]
one = []
for i in stringer:
    if i not in all:
        all.update({i: 1})
    else:
        all[i] += 1
for p in list(all.items()):
    if p[1] == 1:
        one += p[0]
        all.pop(p[0])
if ((len(one) * 100) / len(stringer)) >= 50:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')





