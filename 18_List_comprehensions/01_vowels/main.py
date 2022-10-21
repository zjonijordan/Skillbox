word = str(input("Введите текст: "))
new_word = [i for i in word for t in ["А", "О", "И", "Ы", "У", "Е", "а", "о", "и", "ы", "у", "е"] if i == t]

print(new_word, "\nДлина списка:", len(new_word))


