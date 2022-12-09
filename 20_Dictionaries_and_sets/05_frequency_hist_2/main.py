string = input('Введите текст: ')
text = dict()
invert = dict()

for i in string:
    if i in text:
        text[i] += 1
    else:
        text[i] = 1

print('Оригинальный словарь частот:')
for u in text:
    print(u[0], ':', text[u])

print('Инвертированный словарь частот:')
for letters, number in text.items():
    if str(number) in invert:
        invert[str(number)] += letters
    else:
        invert.update({str(number): [letters]})

for q, a in invert.items():
    print(str(q) + ' : ' + str(a))