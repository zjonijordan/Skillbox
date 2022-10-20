nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

prime = ([i for j in nice_list[0] for i in j]) + ([i for j in nice_list[1] for i in j])

print(prime)