class Car(object):
    def __init__(self,name=None, color=None, price=None,power=None):

        self.name = name
        self.color = color
        self.price = price
        self.power = power

    def __str__(self):
        print( '{}:{},{}'.format(self.name,self.power,self.color))

    def move(self):
        print('一辆{}的{}正在以{}马力的速度飞驰'.format(self.color,self.name,self.power))

ferrari_f12 = Car('ferrari_f12','红色','100w','300')
audi_a9 = Car('audi_a9','黑色','100k','200')
ferrari_f12.move()
audi_a9.move()

#
# 作业题2：
# 任意定义一个动物类，添加name、age、color,food等属性，如“熊猫”，5,“黑白”，“竹子”
# 定义一个run方法，调用run方法时打印相关信息，如打印出“熊猫正在奔跑”
# 定义一个get_age方法，调用get_age方法时打印相关信息，如打印出“这只熊猫今年5岁了”
# 定义一个eat方法，调用eat方法时打印相关信息，如打印出“熊猫正在吃竹子”
class Animal(object):
    def __init__(self, name=None, age=None, color=None, food=None):
        self.name = name
        self.age = age
        self.color = color
        self.food = food
    def run(self):
        print(f'{self.name} run')
    def get_age(self):
        print(f' {self.name} {self.age} 岁了')

    def eat(self):
        print(f'{self.name} 吃 {self.food}')
    def drink(self):
        print(f'{self.name} 在喝水')

    def sleep(self):
        print(f'{self.name} 在睡觉')

panda = Animal('薛定谔的猫','4', '即黑又白','猫粮')
panda.get_age()
panda.eat()
panda.run()


# 作业题3：
# 定义动物类Animal,包含eat、drink、run、sleep方法分别打印吃、喝、跑、睡觉
# 定义狗类Dog继承自动物类Animal（bark方法输出汪汪叫）
# 定义哮天犬类XiaoTianDog继承自狗类Dog（bark方法输出嗷嗷叫、fly方法输出会飞上天）
class Dog(Animal):

    def bark(self):
        print(f'{self.name} 叫：wwwwww')


class GadDog(Dog):
    def bark(self):
        print(f'{self.name} 叫：oooooooooooo')

    def fly(self):
        print('fllllllllllllllllly')

# 通过Dog类创建wangcai对象，调用bark方法、eat方法
# 通过XiaoTianDog类创建xiaoTianDog对象，调用fly方法，bark方法，drink方法
norndog = Dog('中华田园犬','3','黄色','肉')
gaddog = GadDog('哮天犬','3','黑色','肉')

norndog.bark()
norndog.eat()
gaddog.fly()
gaddog.bark()
gaddog.drink()
