size_list = []
people_list = []
Flag = False
def alg(temp, temp2, temp3, temp4):
    count = 0
    HM = int(input(temp))
    while count != HM:
        count += 1
        size = int(input(temp2 + str(count) + temp3))
        temp4.append(size)
        if Flag == True:
            for i in size_list:
                if i >= size:
                    size_list.remove(i)
                    break


alg("Кол-во коньков: ","Размер ", ' пары: ', size_list)
Flag = True
alg("Кол-во людей: ", "Размер ноги ", ' человека: ', people_list)
print("Наибольшее кол-во людей, которые могут взять ролики: ", len(size_list))