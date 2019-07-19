#### 推导式(comprehensions)
推导式又称解析式，是Python的一种独特特性。推导式可以从一个数据序列构建另一个新的数据序列的结构体。共有三种推导式
1. list
2. dict
3. set
#### 列表推导式
使用[]生成list

基本格式：
    
    list = [i for i in range(30) if i%3 is 0]
    应该只允许一个变量 i,将 i 从 迭代器对象rang(30)中取出 
    然后对i进行判断 最后返回i   
    
    def squared(x):
        return x*x
    newlist = [squared(x) for x in range(20) if i%3 is 0]
    最后返回值可以进行函数处理

该方法返回的是一个数列，当要生成的数非常多的时候，占用空间将非常大
存在一定的问题，下面可以用生成器推导式可以解决这个问题
#### 生成器推导式(generator)
生成器推导式只需将[] 变为()
    
    generator = (i ** 2 for i in range(10) if i % 2 is 0)
    <generator object <genexpr> at 0x0000028A8FB35E58>
    
    
该generator 是一个生成器对象，生成器本质就是迭代器，那么该对象就可以取多少用多少，而不用一次生成全部数据。

#### 字典推导式
字典推导式将列表推导式的中括号改为大括号，下面将mydict字典的小写关键字提取出来
       
       mydict = {'a':10,'b':34,'c': 90,'A':10}
       mydict_frequency = {
            k.lower():mydict.get(k.lower()) for k in mydict.keys()
       }
#### 创建字典的方法
##### 直接创建
    
    dict = {'name':'name','port':100 }

##### 工厂方法
    
    items = [('name','earth'),('port','80)]
    dict = dict(items)
    
##### fromkeys()方法
    
    my_dict = {}.fromkeys(('x','y'),12))
#### 合并两个有序列表
      
    #合并两个有序列表
    def link_two_list(l1,l2,tmp):
        if len(l1) == 0 or len(l2) == 0:
            tmp.extend(l1)
            tmp.extend(l2)
            return tmp
        else:
            if l1[0] < l2[0]:
                tmp.append(l1[0])
                del l1[0]
            else:
                tmp.append(l2[0])
                del l2[0]
            return link_two_list(l1,l2,tmp)    
思路：对比两个列表的第一个元素，将小的加入到新列表中，然后删除该元素，然后递归比较，每次都是对比第一个元素
若果有个比较列表比较短，当L2还有元素时L1已经提前清空，那么直接将
l2的剩余元素直接加入到tmp中，直接返回tmp
