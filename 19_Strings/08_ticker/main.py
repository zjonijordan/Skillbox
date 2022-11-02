first = input("Первая строка: ")
second = input("Вторая строка: ")

o = [(i - k) for i in range(len(first)) for k in range(len(second)) if first[i] == second[k]]
temp = 0
if len(o) == len(first):
    for i in o:
        if i > temp:
            temp = i
count = temp - 1
count2 = 0
for i in range(len(first)):
    count += 1
    if count > len(first) - 1:
        count = 0
    if first[count] == second[i]:
        count2 += 1
if count2 == len(first):
    print("Первая строка получается из второй со сдвигом", temp)
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")