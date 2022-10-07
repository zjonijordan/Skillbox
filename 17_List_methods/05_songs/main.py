violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56], ['Halo', 4.9],
    ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83]]

count = -1
duration = 0

for i in range(int(input("Сколько песен выбрать? "))):
    name = input("Название " + str(i + 1) + ' песни: ')
    for song in violator_songs:
        count += 1
        if violator_songs[count][0] == name:
            duration += violator_songs[count][1]
    count = -1
print("Общее время звучания песен: ", duration, "min")