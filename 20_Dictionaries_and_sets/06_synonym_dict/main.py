word = dict()
for i in range(int(input("Введите количество пар слов: "))):
    words = input(str(i + 1) + ' пара: ')
    psh, temp, temp2, shit = {' ', '-', ',', '.'}, '', '', ''
    for i in words:
        if i not in psh:
            temp += i
        else:
            temp2 = temp
            temp = ''
            shit += i
    word.update({temp.lower(): temp2.lower()})

question = input("Введите слово: ").lower()
while question != 'end':
    flag = False
    for first, second in word.items():
        if first == question:
            print('Синоним: ', second)
            flag = True
        elif second == question:
            print('Синоним: ', first)
            flag = True
    if flag == False:
        print('Такого слова в словаре нет.')
    question = input("Введите слово: ").lower()