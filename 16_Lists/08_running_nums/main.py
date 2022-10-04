K = int(input("Сдвиг: "))
string = ["1", "2", "3", "4", "5"]
new_string = []

for count in range(-K, len(string) - K):
    new_string += string[count]
print("Изначальный список:", string, "\nСдвинутый список:", new_string)