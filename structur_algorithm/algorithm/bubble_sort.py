# def Bubblesort(numbs):
#     for i in range(len(numbs)):
#         for j in range(len(numbs) - 1):
#             if numbs[j] > numbs[j + 1]:
#                 numbs[j], numbs[j + 1] = numbs[j + 1], numbs[j]
#
#     return numbs

def Bubblesort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1] :
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

nums = [5, 4, 3, 2, 1]
print(Bubblesort(nums))