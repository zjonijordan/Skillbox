string = input("Ведите строку с буквами h: ")
def calculation(value, flag):
    index = 0
    for i in value:
        index += 1
        if i == "h" or i == "H":
            break
    if flag == True:
        if index == 0:
            index = 1
    return index

begin, end = calculation(string, False), -calculation(string[::-1], True)
new_string = string[begin:end]
print(new_string[::-1])