shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

count = -1
name = input("Название детали: ")

for i in shop:
        count += 1
        if (shop[count][0]) == name:
                match = int(input("Кол-во деталей - "))
                print("Общая стоимость - ", shop[count][1] * match)
                break