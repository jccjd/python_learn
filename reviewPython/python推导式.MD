#### 推导式(comprehensions)
推导式又称解析式，是Python的一种独特特性。推导式可以从一个数据序列构建另一个新的数据序列的结构体。共有三种推导式
1. list
2. dict
3. set
#### 列表推导式
使用[]生成list

基本格式：
    
    list = [i for i in range(30) if i%3 is 0]
    i    