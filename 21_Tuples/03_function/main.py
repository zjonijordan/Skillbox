random_turple = tuple(('h e l l o w o r l d').split(' '))
elem = input("enter: ")
count = []
for index, name in enumerate(random_turple):
    if elem == name:
        count += [str(index)]
if len(count) == 0:
    print('Нету такого элемента!')
if len(count) == 1:
    print(random_turple[int(count[0]):])
if len(count) == 2:
    print(random_turple[int(count[0]): int(count[1]) + 1])
if len(count) > 2:
    print(random_turple[int(count[0]): int(count[-1]) + 1])

