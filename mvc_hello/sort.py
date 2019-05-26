def binary_search(arr,key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = ( start + end ) / 2
        if arr[mid] < key:
            start = mid
        elif arr[mid] > key:
            end = mid
        if arr[mid] == key:
            return mid
    return -1
# arr = [0,1,2,3,4,5]
# print binary_search(arr,3)




def bubble_sort(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(i + 1,count) :
            if lists[i] > lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
    return lists


def insert_sort(lists):
    for i in range(1, len(lists)):
        for j in range(i - 1,-1,-1):
            if lists[j] > lists[j+1]:
                lists[j],lists[j+1] = lists[j+1],lists[j]
    return lists


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

def quick(list,left,right):
    if (left > right):
        return
    key = list[left]
    start = left
    end = right
    while left < right:
        while left < right and list[right] >=key:
            right-=1
        list[right],list[left] = list[left],list[right]
        while left < right and list[left] <= key:
            left+=1
        list[left],list[right] = list[right],list[left]

    quick(list,start,left -1)
    quick(list,left+1,end)
    return list

lists = [21,32,43,98,54,45,23,4,66,86]
# print bubble_sort(lists)
# print insert_sort(lists)
print(quick(lists,0,len(lists)-1))