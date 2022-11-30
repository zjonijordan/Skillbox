enev = set()
not_even = set()
Flag = False
for i in range(1, int(input("Введите максимальное число: ")) + 1):
    if i % 2 == 0:
        enev.add(i)
    else:
        not_even.add(i)
flag = True
question = input('Нужное число есть среди вот этих чисел:' + str(enev) + "\nОтвет Артёма: ")
if question == 'Нет' or question == 'нет':
    enev = not_even
    not_even = set()
while len(enev) > 0:
    if question == 'Да' or question == 'да':
        not_even = set()
        not_even = enev.pop()
        if len(enev) < 2:
            question2 = input("Число которое загадал Артём:" + str(enev) + '?'+ "\nОтвет Артёма: ")
            if question2 == 'Да' or question2 == 'да':
                print("Число которое загадал Артём:", enev)
                break
            elif question2 == 'Нет' or question2 == 'нет':
                print("Число которое загадал Артём:", not_even)
                break
    elif question == 'Помогите!' or question == 'помогите!':
        print('Артём мог загадать следующие числа: ', enev)
        break
    elif Flag == True:
        if question == 'Нет' or question == 'нет':
            print("Число которое загадал Артём:", not_even)
            break
    Flag = True
    question = input('Нужное число есть среди вот этих чисел:' + str(enev) + "\nОтвет Артёма: ")