students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
def calculate(data):
    interests = tuple()
    soname = 0
    for i, p in data.items():
        interests += tuple(p['interests'])
        soname += len(p['surname'])
    return interests, soname

print(calculate(students))
