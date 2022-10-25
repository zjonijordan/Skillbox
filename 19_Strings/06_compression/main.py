string = input("Введите строку: ")
new_string = []
temp = string[:1:]
count = 0
for i in string:
    if i != temp:
        new_string += temp + str(count)
        count = 1
        temp = i
    else:
        count += 1
new_string += temp + str(count)

print('Закодированная строка:',"".join(new_string))