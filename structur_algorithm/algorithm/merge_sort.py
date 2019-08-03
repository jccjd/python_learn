def merge_sort(list):
    """归并排序"""
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left_list = merge_sort(list[:mid])
    rigth_list = merge_sort(list[mid:])

    left_prointer = 0
    rigth_prointer = 0
    result = []

    while left_prointer < len(left_list) and rigth_prointer < len(rigth_list):
        if left_list[left_prointer] < rigth_list[rigth_prointer]:
            result.append(left_list[left_prointer])
            left_prointer += 1
        else:
            result.append(rigth_list[rigth_prointer])
            rigth_prointer += 1

    result += left_list[left_prointer:]
    result += rigth_list[rigth_prointer:]

    return result


numbers = [5, 4, 3, 2, 1]
print(merge_sort(numbers))
