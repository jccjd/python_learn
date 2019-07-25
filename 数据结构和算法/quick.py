def quick(list, left, right):
    if left > right:
        return list
    key = list[left]
    start = left
    end = right
    while left < right:
        while left < right and list[right] > key:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] <= key:
            left += 1
        list[right] = list[left]

    list[left] = key
    quick(list, start, left - 1)
    quick(list, left + 1, end)
    return list
# 强化版
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))


list = [2,5,7,6,3,1]
l = quick(list,0,5)
print(l)


