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
for u, i in text.items():
    invert.update(dict.fromkeys([i], []))
for o, p in text.items():
    invert[p] += [o]
for q, w in invert.items():
    print(q,':', w)

