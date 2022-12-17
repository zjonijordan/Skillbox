enter = int(input('Введите позицию числа в ряде Фибоначчи: '))
data = {0: 0, 1: 1}
def calculate(n):
    if n in data:
        return data[n]
    data[n] = calculate(n - 1) + calculate(n - 2)
    return data[n]

print(calculate(enter))