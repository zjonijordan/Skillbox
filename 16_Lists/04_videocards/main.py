card = int(input("Кол-во видеокарт: "))
hight_model = "0"
old_list = []
new_list = []

for i in range(1, card + 1):
    model = str(input(str(i) + " Видеокарта: "))
    if model > hight_model:
        hight_model = model
    old_list.append(model)
for t in old_list:
    if t != hight_model:
        new_list.append(t)
print("Старый список видеокарт: ", old_list, "\nНовый список видеокарт: ", new_list)