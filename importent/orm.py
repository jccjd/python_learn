# 一、首先来定义Field类，它负责保存数据库表的字段名和字段类型：


# 二、定义元类，控制Model对象的创建
class ModelMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        # 为什么要判定这个model，ModelMetaclass相当于被两个类继承了，那么，下面
        # model 和 student 在new的时候都需要在该类中找new方法，我们不需要对model进行操作
        # 我们要做的是对student的字段动态的创建mapping，由于我们可能有多张表，而且每张标的字段数量可能不同
        # 所有每次表对象不同的时候，创建的mapping段也不同

        if name == 'Model':
            return super(ModelMetaclass, mcs).__new__(mcs, name, bases, attrs)

        chiose = ((k, v) for k, v, in attrs.items() if not k.startswith('__'))

        mappings = dict((k, v ) for k, v in chiose)

        for k in mappings.keys():
            # 将类属性移除，使定义的类字段不污染User类属性，只在实例中可以访问这些key
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系，创建类时添加一个__mappings__类属性
        return super(ModelMetaclass, mcs).__new__(mcs, name, bases, attrs)


# 三、编写Model基类
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(self, *args, **kwargs)

    def save(self):
        for k, v in self.__mappings__.items():
            print(k,v)

# 最后，我们使用定义好的ORM接口，使用起来非常的简单。
class User(Model):
    # 定义类的属性到列的映射：

    id = 'id'
    name = ('username')
    email = 'email2'
    password = ('password')

class good(Model):
    id = 1
    good_name = 'hhh'
good = good()
good.save()
# 创建一个实例：
u = User(id=12345, name="Michael", email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
