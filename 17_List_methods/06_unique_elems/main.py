list_1 = []
def calculate(temp, temp2):
    count_1 = 0
    while count_1 != temp:
        count_1 += 1
        first = input("Ведите " + str(count_1) + ' число из ' + temp2 +' списка чисел: ')
        list_1.append(first)
calculate(3, "первого")
calculate(7, "второго")

print("Новый первый список с уникальными элементами: ", set(list_1))