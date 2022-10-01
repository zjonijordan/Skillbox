N = int(input("Ведите число N: "))
N_new = []

for i in range(1, N + 1):
     if i % 2 == 0:
         N_new.append(i)

print(N_new)
