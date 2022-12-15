a = [1, 2, 3]
b = '4567'
c = (7, 8, 9)
def zip(*args):
    sequences = [list(arg) for arg in args]
    min_length = len(min(args, key = len))
    return [tuple(seq[i] for seq in sequences) for i in range(min_length)]

print(zip(a, b, c))