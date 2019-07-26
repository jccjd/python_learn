list = [2,1,3,4,5]

def bubble(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
def InsertSort(list):
    for i in range(len(list)):
        for j in range(i - 1, -1, -1):
            if list[j] > list[j + 1]:
                list[j] ,list[j + 1] = list[j + 1], list[j]
    return list
def selectSort(list):
    for i in range(len(list)):
        min = list[i]
        for j in range(i + 1, len(list)):
            if list[j] < min:
                list[j], min = min, list[j]
        list[i] = min
    return list
def quickSort(list):
    if len(list) <= 1:
        return list
    pivot = len(list) // 2
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return quickSort(left) + middle + quickSort(right)
print(quickSort(list))
print(selectSort(list))
print(InsertSort(list))
print(bubble([2,1,3,4,5]))