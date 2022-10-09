arr = []
suffix = []
buf = []
last_i = len(arr)-1
HM = int(input("Кол-во чисел: "))


for t in range(HM):
    x = int(input("Число: "))
    arr.append(x)

for i in range(len(arr)):
    if arr[i] != arr[last_i]:
        if len(buf):
            suffix.extend(buf)
            buf = []
        suffix.insert(0, arr[i])
    elif last_i != i:
        buf.insert(0, arr[i])
        last_i -= 1
    if i == last_i:
        break

print("Последовательность:", arr, "\nНужно приписать чисел:",len(suffix),"\nСами числа:",suffix)