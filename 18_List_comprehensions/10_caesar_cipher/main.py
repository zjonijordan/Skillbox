dict = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
count = 0
message = input("Введите сообщение: ")
korn = int(input("Введите сдвиг: "))
skript = ''

for i in message:
    if i == " ":
        skript += " "
    for t in dict:
        count += 1
        if korn + count > len(dict):
            count = count - len(dict)
        if t == i:
            skript += dict[count - 1 + korn]
    count = 0

print("Зашифрованное сообщение: ", skript)