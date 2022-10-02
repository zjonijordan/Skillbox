quantity = int(input("Кол-во контейнеров: "))
massa = 0
count = 0
kon = []

while count != quantity:
    massa = int(input("Введите вес контейнера: "))
    if massa <= 200:
        kon.append(massa)
        count += 1
    else:
        print("Масса не может быть больше 200кг")

count = 0
new_cont = int(input("Введите вес нового контейнера: "))
for i in kon:
    if new_cont <= i:
        count += 1
print("Номер, куда встанет новый контейнер:", count)
