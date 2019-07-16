def quick_sort(lists,left,right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right

    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
                left += 1
        lists[right] = lists[left]

    lists[right] = key
    quick_sort(lists,low,left - 1)
    quick_sort(lists,left + 1 ,high)
    return lists

list = [2,5,7,6,3,1]
l = quick_sort(list,0,5)
print(l)
def demo_quick_sorting(lists, left, right):
    if left > right:
        return lists
    key = lists[left]
    low = left
    height = right

    while left < right:
        if left < right and lists[right] > key:
            right -= 1
        lists[left] = lists[right]
        if left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key

    demo_quick_sorting(lists,low,left - 1)
    demo_quick_sorting(lists,left + 1,height)


