place = []
town = dict()
for i in range(int(input("Кол-во стран: "))):
    place += [i for i in input(str(i + 1) + " страна: ").split()]
    for p in place[1::]:
        town.setdefault(p, place[0])
    place.clear()
for num in range(3):
    city = input(str(num + 1) + " город: ")
    answer = town.get(city)
    if answer == None:
        print('По городу ' + str(city) + 'данных нет.')
    else:
        print('Город '+ city + ' расположен в стране ' + str(answer))