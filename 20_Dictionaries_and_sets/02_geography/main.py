place = []

for i in range(int(input("Кол-во стран: "))):
    place += [[i for i in input(str(i + 1) + " страна: ").split()]]
def check(word):
    answer = ''
    Flag = False
    for i in range(len(place)):
        for u in place[i]:
            if u == word:
                answer = "Город " + str(u) + " расположен в стране " +  place[i][0]
                Flag = True
    if Flag == False:
        answer = "По городу " + word + " данных нет."
    return answer

for i in range(3):
    print(check(input(str(i + 1) + " город: ")))