N = int(input("Enter: "))
count = 0
def calculate(enter, number):
    if enter != number:
        number += 1
        print(number)
        calculate(enter, number)
        return number

calculate(N, count)
