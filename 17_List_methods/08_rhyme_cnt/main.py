people = int(input("Кол-во человек: "))
listing = []
number = int(input("Какое число в считалке? "))
step = number
inx = 0
print("Значит, выбывает каждый ", number, 'человек')
print("---------------------------")

for i in range(1, people + 1):
    listing.append(i)

while len(listing) > 1:
    l_ln = len(listing)
    if l_ln <= number:
        step = number - (number // l_ln) * l_ln
    target_inx = inx + step - 1 if step > 0 else inx
    if target_inx >= l_ln:
        target_inx = target_inx - (l_ln - 1)
    print("Текущий круг людей:", listing, "\nНачало счёта с номера: ", listing[inx], "\nВыбывает человек под номером: ", listing[target_inx])
    listing.remove(listing[target_inx])
    inx = target_inx
    if inx > len(listing) - 1:
        inx = 0
    print("---------------------------")

print("Остался человек под номером: ", listing[0])