a, b, c = [1, 5, 3], [1, 5, 1, 5], [1, 3, 1, 5, 3, 3]
def calculate(temp, temp2, b):
    a.extend(b)
    count = 0
    for i in a:
        if i == temp:
            count += 1
    print("Кол-во цифр", temp, "при", temp2, "объединении: ", count)

calculate(5, "первом", b)
calculate(3, "втором", c)
print("Итоговый список: ", a)
