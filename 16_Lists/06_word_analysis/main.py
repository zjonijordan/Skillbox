word = input("Введите слово: ")
number_word = len(word)
new_word = list(word)
count = 0

for number in range(number_word):
    for i in word:
        if i == new_word[number]:
            count += 1

answer = number_word - count
if answer < 0:
    answer = abs(answer)
elif answer == 0:
    answer = number_word
print("Кол-во уникальных букв:", answer)

