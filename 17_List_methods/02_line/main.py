first = []
second = []
Flag = True
def klass(first, beg, end, step):
    for i in range(beg, end, step):
        first.append(i)

klass(first, 160, 177, 2)
klass(second, 162, 181, 3)

first += second
while Flag == True:
    Flag = False
    for index in range(len(first)):
        if (index + 1 <= len(first) - 1) and (first[index] > first[index + 1]):
            Flag = True
            first[index], first[index + 1] = first[index + 1], first[index]

print("Отсортированный список:", first)