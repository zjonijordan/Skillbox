import random
original = []
modified = []
for _ in range(10):
    original += str(random.randrange(10))
print('Оригинальный список:', original)
for index in range(len(original)):
    if index % 2 == 0:
        modified.append(tuple(original[index]) + tuple(original[index + 1]))
print('Новый список:', modified)