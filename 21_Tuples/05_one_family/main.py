BD = {'Сидоров Никита': 35,
      'Сидорова Алина': 34,
      'Сидоров Павел': 10,
      'Петров Саша': 23,
      'Петрова Анна': 23,
      'Петровский Ваня': 18}
enter = input('Введите фамилию: ')
age_family = 0
for name, age in BD.items():
      if enter.lower() == (name[0:len(enter)]).lower():
            age_family += age
if age_family == 0:
      print("Sorry, фамилия, " + str(enter) + " отсутствует в базе данных")
else:
      print("Сумарный возраст семьи составляет:", age_family)