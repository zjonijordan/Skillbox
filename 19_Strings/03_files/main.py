no_way = '@ № $ % ^ & * ()'.split()
file = input("Ведите название файла: ")

for i in no_way:
    if file.startswith(i):
        print("название начинается на один из специальных символов!")
        break
    elif (not file.endswith('.txt')) and (not file.endswith('.docx')):
        print("неверное расширение файла. Ожидалось .txt или .docx")
        break
    else:
        print("Файл назван верно.")
        break