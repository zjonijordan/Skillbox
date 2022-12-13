iteration = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
def yes_or_no():
    for index, name in enumerate(resolt):
        if int(resolt[index][0]) <= int(ask[0]):
            return index
        break

for i in range(iteration):
    ask = input(str(i + 1) + " запись: ").split()
    if i == 0:
        resolt = [tuple(ask)]
    else:
        index = yes_or_no()
        if index != None:
            resolt.insert(int(index), tuple(ask))
        else:
            resolt += [tuple(ask)]

print('\nИтоги соревнований:')
for index, name in enumerate(resolt):
    print(str(index + 1) + ' место. ' + name[1] + " с результатом " + name[0])