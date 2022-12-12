phonebook = dict()
flag = True
while flag:
    ask = int(input('1: добавить контакт, 2: найти человека: '))
    if ask == 1:
        new_contact = input('Имя, Фамилия, номер телефона(через пробел): ').split()
        if (new_contact[0] + ' ' + new_contact[1]) in phonebook:
            print('Этот контакт уже есть в книге!')
        else:
            phonebook.update({tuple((new_contact[0] + ' ' + new_contact[1]).split()): new_contact[2]})
            print(phonebook)
    if ask == 2:
        search = input('Ведите фамилию: ')
        for name, number in phonebook.items():
            if search.lower() == name[1].lower():
                print('контакт: ' + name[0] + ' ' + name[1], ': ' + number)
    if ask == 000:
        flag = False
    else:
        print('Неверная команда. Можно водить только 1 или 2')
