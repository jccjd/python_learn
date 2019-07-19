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

    def __new__(cls,name,bases,dct):
        '''返回一个类，将属性都大写 version3.0'''
        attrs = ((name,value) for name,value in dct.items() if not name.startswith('__'))
        uppercase_attrs = dict((name.upper(),value) for name, value in attrs)

        return super(UpperAttrMetaClass,cls).__new__(cls,name,bases,uppercase_attrs)
class Foo(metaclass=UpperAttrMetaClass):
    bar = 'bip'
f = Foo()
print(f.BAR)

class MetaClassModel(type):
    def __new__(mcs, name, base, dct):
        if name == 'Model':
            return super(MetaClassModel, mcs).__new__(mcs, name, base, dct)
        mapping = dict()
        for k, v in dct.items():
            mapping[k] = v
        for k in mapping.keys():
            dct.pop(k)
        dct['mapping'] = mapping

        return super(MetaClassModel, mcs).__new__(mcs, name, base, dct)

class Model(dict, metaclass=MetaClassModel):
    def __init__(self,*args, **kwargs):
        super(Model,self).__init__(self,*args, **kwargs)

    def save(self):
        for k, v, in self.mapping.items():
            print(k,v)
class Student(Model):
    id = 'df'
    cd = 'df'
stu = Student(id='d',cd = 'fd')
stu.save()


