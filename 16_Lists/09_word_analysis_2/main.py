word = input("Введите слово: ")
inverted = ""

for i in word:
    inverted = i + inverted

if word == inverted:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")