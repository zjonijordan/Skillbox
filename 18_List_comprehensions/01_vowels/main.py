word = str(input("Введите текст: "))
new_word = [i for i in word if i == "А" or i == "О" or i == "И" or i == "Ы" or i == "У" or i == "Е" or i == "а" or i == "о" or i == "и" or i == "ы" or i == "у" or i == "е"]

print(new_word, "\nДлина списка:", len(new_word))


