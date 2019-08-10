
def Bubblesort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) -i - 1):
            if nums[j] > nums[j + 1] :
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums
def Bubble(nums):
    for i in range(len(nums)):
        flag = True
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = False
            if flag == True:
                break
    return nums

nums = [5, 4, 3, 2, 1]
print(Bubblesort(nums))