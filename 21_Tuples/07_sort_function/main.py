strin = input("Ведите числа через пробел: ")

flag = True
for i in strin:
    if i == ".":
        print(tuple(strin.split()), '\nЕсть дробное число')
        flag = False
def sort(nums):
    nums = nums.split()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return tuple(nums)

if flag == True:
    print(sort(strin))