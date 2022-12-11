import random
def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True

data = {random.randrange(1, 100):random.choice(['win', 'lose', 'draw']) for i in range(10)}
print({index: name for index, name in data.items() if is_prime(index) == True})