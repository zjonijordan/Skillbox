import random
list_1 = [round(random.triangular(5, 10), 2) for i in range(20)]
list2 = [round(random.triangular(5, 10), 2) for t in range(20)]
list_3 = [list_1[u] if list_1[u] >= list2[u] else list2[u] for u in range(20)]

print("Первая команда: ", list_1, "\nВторая команда: ", list2, "\nПобедители тура: ", list_3)