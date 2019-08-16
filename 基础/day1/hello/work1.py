while True:
    strs = input('input: ')
    if strs == 'end':
        break

    mylist = [strs]
    for i in mylist:
        if len(i) >= 6:
            with open('context.txt','a+') as f:
                f.write(i+'\n')
        else:
            print('列表中没有符合条件的元素')