def change_num(num):
    count2 = ""
    for word in num:
        count2 = word + count2
    return count2
def separate(arg):
    j = str()
    k = str()
    for i in arg:
        j += i
        if i == ".":
            j = j.replace(".", "")
            break
    j = change_num(j)
    for i in arg:
        if i == ".":
            k = str()
        else:
            k += i
    k = change_num(k)
    return (str(j) + "." + str(k))

first_inp = str(input("Ведите первое число: "))
second_inp = str(input("Ведите второе число: "))

first_num = float(separate(first_inp))
print("Первое число наоборот: ", first_num)
second_num = float(separate(second_inp))
print("Второе число наоборот: ", second_num)
print("Сумма: ", first_num + second_num)