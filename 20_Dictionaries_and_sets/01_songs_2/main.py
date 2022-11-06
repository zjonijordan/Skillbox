import random
violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

HM = int(input("Сколько песен выбрать? "))
listing = [i for i in violator_songs]
cont = 0

for i in range(HM):
    cont += violator_songs[listing[i]]
    print("Название " + str(i+1) + " песни:", listing[i])
print("Общее время звучания песен:", round(cont, 2), "мин.")