films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
name = ""
likines = []
flag = True

while name != "end":
    name = str(input("Ведите название фильма: "))
    for i in films:
        if name == i:
            print("Такой фильм есть! Добавлено в список любимых фильмов!")
            likines.append(i)
            flag = True
            break
        else:
            flag = False
    if flag == False:
        print("ТАКОГО ФИЛЬМА НЕТУ В СПИСКЕ!")

print("список любимых фильмов:", likines)