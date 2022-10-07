first = []
second = []
def klass(first, beg, end, step):
    for i in range(beg, end, step):
        first.append(i)

klass(first, 160, 177, 2)
klass(second, 162, 181, 3)

first += second
first.sort()

print("Отсортированный список:", first)