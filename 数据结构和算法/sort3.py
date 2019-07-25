def sort1(list):
    # 冒泡排序 时间复杂度为n方 不稳定排序
    for i in range(len(list)):
        for j in range(len(list) -1 ):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
def sort2(list):
    # 插入排序，时间复杂度为n方，稳定排序
    for i in range(1,len(list)):
        for j in range(i - 1, -1, -1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1],list[j]
    return list

def sort3(list):
    # 选择排序，时间复杂度为n方，不稳定排序
    for i in range(len(list)):
        min = list[i]
        for j in range(i,len(list)):
            if list[j] < min:
                list[j], min = min, list[j]
        list[i] = min
    return list

list = [4,3,2,1]
print(sort1(list))
print(sort2(list))
print(sort3(list))