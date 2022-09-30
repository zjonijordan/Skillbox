number = int(input("Ведите число: "))

for i in range(2, number):
    if number / i == number // i:
        number = i
print("Наименьший делитель, отличный от единицы:", number)