words = input("Ведите слова: ").split()
long_word = []

for i in words:
    if len(long_word) < len(i):
        long_word = i

print("Слово: ", long_word, "\nДлинна слова: ", len(long_word))