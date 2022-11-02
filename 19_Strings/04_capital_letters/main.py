string = input("Введите строку: ").split()

new_string = [(i[0].upper() + i[1:]) for i in string]

print('Результат:'," ".join(new_string))