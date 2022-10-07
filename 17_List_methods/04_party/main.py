guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
Flag = False

while Flag == False:
    guest = input("Гость пришел или ушел? ")
    if guest == "Пришел":
        name = input("Имя гостя: ")
        if len(guests) >= 6:
            print("Прости,", name, " но мест нет.")
        else:
            guests.append(name)
            print("Привет,", name + "!", "\nСейчас на вечеринке", len(guests), "человек:", guests)
    elif guest == "Ушел":
        name = input("Имя гостя: ")
        guests.remove(name)
        print("Пока,", name + "!", "\nСейчас на вечеринке", len(guests), "человек:", guests)
    elif guest == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        Flag = True
