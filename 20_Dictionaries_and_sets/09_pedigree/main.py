all = dict()
people = int(input("Введите количество человек: "))
count = 0

while people != len(all):
    count += 1
    couple = input(str(count) + " пара: ").split()
    if couple[1] in all:
        all.setdefault(couple[0], all[couple[1]])
        all[couple[0]] += 1
    else:
        all.setdefault(couple[0], 1)
        all.setdefault(couple[1], 0)

print('“Высота” каждого члена семьи:')
for name in all:
    print(name, all[name])