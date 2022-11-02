enter = input("Введите IP: ")
new_IP = ''
abc = 'A E I O U Y B C D F G H J K L M N P Q R S T V W X Z'.lower().split(" ")
flag = False
for coma in enter:
    if coma == ",":
        print('Адрес - это четыре числа, разделенные точками')
        flag = True
count = -1
for i in enter.split("."):
    count += 1
    for k in i:
        for j in abc:
            if j == k or j.upper() == k:
                print(enter.split(".")[count], "не целое число")
                flag = True
if flag == False:
    count = -1
    for t in enter.split('.'):
        count += 1
        if int(t) > 0 and int(t) <= 255:
            new_IP += str(t) + "."
        elif int(t) > 255:
            print(enter.split(".")[count], 'превышает 255')
    if len(new_IP.split('.')) == 5:
        print("IP-адрес корректен", new_IP[:len(new_IP) - 1])
    else:
        print("IP-адрес НЕ корректен!")