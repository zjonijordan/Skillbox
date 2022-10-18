N = list(input("Ведите список чисел: "))
count = N.count("0")
def delite(flag):
    for i in N:
        N.remove("0")
    if flag == True:
        for q in range(count):
            N.append('0')
    return N

print("Список до удаления:", delite(True))
print("Список после сжатия:", delite(False))


