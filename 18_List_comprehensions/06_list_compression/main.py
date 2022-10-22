N = list(input("Ведите список чисел: "))

N_with_zero = [i for i in N if int(i) != 0]
zero = [i for i in N if int(i) == 0]

print("Масив: ", N, "\nМасив без нулей:", N_with_zero, "\nМасив с нулями:", N_with_zero + zero)


