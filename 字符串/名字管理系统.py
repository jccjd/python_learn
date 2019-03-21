print("="*50)
print("     名字管理系统 v8.6     ")
print("1.添加一个新名字")
print("2.删除一个名字")
print("3.添加一个新名字")
print("="*50)
while True:

    num = int(input(" 亲输入功能序号："))

    names = []
    if num == 1:
        new_name = input("亲输入名字：")
        names.append(new_name)
        print(names)
    elif num == 2:
        pass
    elif num == 3:
        pass
    elif num == 4:
        find_name = input("输入要查询的名字：")
        if find_name in names:
            print("find it")
        else:
            print("not find")
    elif num == 5:
        break
    else:
        print("输入有误，重行输入")