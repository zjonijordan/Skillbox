import random
enter = set(i for i in range(1, int(input("Введите максимальное число: ")) + 1))
flag = True
while flag == True:
    temp = set()
    for i in range(len(enter) // 2):
        temp.add(random.choice([min(enter), max(enter)]))
    user = input('Нужное число есть среди вот этих чисел: ' + str(temp) + '\n')
    if user == "нет":
        enter -= temp
    if user == "да":
        enter = temp
    if user == "Помогите":
        enter -= temp
        print('Артём мог загадать следующие числа: ', enter)
        flag = False
    if len(enter) < 2:
        print("Загаданное число:", enter)
        flag = False


