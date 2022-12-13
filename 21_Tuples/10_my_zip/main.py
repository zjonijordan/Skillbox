string = [i for i in 'abcd']
qsq = (10, 20, 30, 40)

new_zip = ((name, str(qsq[index])) for index, name in enumerate(string))

print(new_zip)
for i in new_zip:
    print(i)

