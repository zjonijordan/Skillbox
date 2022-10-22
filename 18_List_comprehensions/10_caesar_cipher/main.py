dict = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
korn = int(input("Введите сдвиг: "))
message = input("Введите сообщение: ")

index = [((dict.index(i) + korn) % len(dict)) if i != " " else -1 for i in message]
new_word = [dict[r] if r != -1 else " " for r in index]

print("Зашифрованное сообщение: " + ''.join(new_word))