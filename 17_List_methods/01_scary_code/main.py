a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
def func(number, temp, temp2):
    count = 0
    for i in a:
        if i == number:
            count += 1
    print("Кол-во цифр", temp, "при", temp2, "объединении: ", count)
func(5, 5, "первом")
a.extend(c)
func(3, 3, "втором")
print(a)