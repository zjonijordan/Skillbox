strin = input("Ведите числа через пробел: ")
def sort(nums):
    flag = True
    for i in strin:
        if i == ".":
            flag = False
            print('Есть дробное число')
            return tuple(strin.split())
    if flag == True:
        nums = nums.split()
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
        return tuple(nums)

print(sort(strin))