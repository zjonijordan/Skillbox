K = int(input("Сдвиг: "))
string = ["1", "2", "3", "4", "5"]
new_string = []

if K == 2:
    K = 4
elif K == 4:
    K = 2
for count in range(-K, len(string) - K):
    new_string += string[count]
print("Изначальный список:", string, "\nСдвинутый список:", new_string)
