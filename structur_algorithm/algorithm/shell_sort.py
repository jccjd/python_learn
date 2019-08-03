def shell(list):
    """希尔排序"""
    n = len(list)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if list[i] < list[i - gap]:
                    list[i], list[i - gap] = list[i - gap], list[i]
                    i -= gap
                else:
                    break
        gap //= 2

    return listd
listd = [5,4,3,1,2]
print(shell(listd))