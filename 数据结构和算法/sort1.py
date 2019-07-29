list = [2,1,3,4,5]
length = len(list)

def bubble(list):
    for i in range(length):
      for j in range(length - 1):
          if list[j] > list[j + 1]:
              list[j], list[j + 1] = list[j + 1], list[j]
    return list
def InsertSort(list):
    for i in range(1,length):
        for j in range(i -1, -1, -1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + j], list[j]
    return list

def selectSort(list):
    for i in range(length):
        min = list[i]
        for j in range(i + 1, length):
            if list[j] < min:
               list[j], min = min, list[j]
        list[i] = min
    return list
def quickSort(list):
    if len(list) <= 1:
        return list
    key = list[len(list) // 2]
    left = [i for i in list if i < key]
    middle = [i for i in list if i == key]
    right = [i for i in list if i > key]
    return quickSort(left) + middle + quickSort(right)

print(quickSort(list))
print(selectSort(list))
print(InsertSort(list))
print(bubble([2,1,3,4,5]))