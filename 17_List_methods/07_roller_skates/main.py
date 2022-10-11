size_list = []
people_list = []
end_list = []
def alg(temp, temp2, temp3, temp4):
    count = 0
    HM = int(input(temp))
    while count != HM:
        count += 1
        size = int(input(temp2 + str(count) + temp3))
        temp4.append(size)

alg("Кол-во коньков: ","Размер ", ' пары: ', size_list)
alg("Кол-во людей: ", "Размер ноги ", ' человека: ', people_list)

for i in people_list:
    for t in size_list:
        if t == i or t + 1 == i:
            size_list.remove(t)
            end_list.append(t)

print("Наибольшее кол-во людей, которые могут взять ролики: ", len(end_list))