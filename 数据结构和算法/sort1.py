list = [2,1,3,4,5]
length = len(list)
def bubble(list):
    for i in range(length):
        for j in range(length - 1 ):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
def Instertsort(list):
    for i in range(length):
        for j in range(i - 1, -1, -1):
            if list[j] >list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

def selectsort(list):
    for i in range(length):
        min = list[i]
        for j in range(i+1,length):
            if list[j] < min:
                list[j], min = min,list[j]
        list[i] = min
    return list
def quicksort(list):
    if len(list) <=1:
        return list
    key = list[len(list) // 2]
    left = [i for i in list if i < key]
    middle = [i for i in list if i == key]
    rigth = [i for i in list if i > key]

    return quicksort(left) + middle + quicksort(rigth)
print(quicksort(list))
print(bubble(list))
print(Instertsort(list))
print(selectsort(list))

