
def upper_attr(future_class_name,future_class_parents,future_class_attr):
    '''返回一个类，将属性都大写 version1.0'''
    attrs = ((name,value) for name,value in future_class_attr.items() if not name.startswith('__'))

    uppercase_attrs = dict((name.upper(),value) for name,value in attrs)

    return type(future_class_name,future_class_parents,uppercase_attrs)#返回改写的类

class UpperAttrMetaClass(type):

    # def __new__(cls,name,bases,dct):
    #     '''返回一个类，将属性都大写 version2.0'''
    #     attrs = ((name,value) for name,value in dct.items() if not name.startswith('__'))
    #     uppercase_attrs = dict((name.upper(),value) for name, value in attrs)
    #     return type.__new__(cls,name,bases,uppercase_attrs)

    def __new__(mcs, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attrs = dict((name.upper(), value) for name, value in attrs)

        return super(UpperAttrMetaClass, mcs).__new__(mcs, name, bases, uppercase_attrs)


class MetaClassModel(type):
    def __new__(mcs, name, base, dct):

        if name == 'Model':
           return super(MetaClassModel, mcs).__new__(mcs, name, base, dct)

        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        mapping = dict((name, value) for name, value in attrs)

        for k in mapping:
            dct.pop(k)
        dct['__mapping__'] = mapping
        return super(MetaClassModel, mcs).__new__(mcs, name, base, dct)

class Model(metaclass=MetaClassModel):

    def save(self):
        for k, v in self.__mapping__.items():
            print(k, v)


class User(Model):
    id = 1
    name = 'll'
    sex = 'll'

class Singleton(type):
    def __init__(cls, name, base, dct):
        super(Singleton, cls).__init__(name, base, dct)
        cls._instance = None
    def __call__(self, *args, **kwargs):
        if self._instance == None:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance

if __name__ == '__main__':
    u = User()
    u.save()
