class Filed(object):
    def __init__(self, name, column):
        self.name = name
        self.column = column

class StringFiled(Filed):
    def __init__(self, name):
        super(StringFiled, self).__init__(name, 'varchar(100)')

class IntegerFiled(Filed):
    def __init__(self, name):
        super(IntegerFiled, self).__init__(name, 'bigint')

class ModelMetaClass(type):
    def __new__(mcs, name, base, dic):
        if name == 'Model':
            super(ModelMetaClass, mcs).__new__(mcs, name, base, dic)

        mapping = dict()
        for k, v in dic.items():
            if isinstance(v, Filed):
                print(f'find mapping{k,v.column}')
                mapping[k] = v

        for k in mapping.keys():
            dic.pop(k)

        dic['__table__'] = name.lower()
        dic['__mapping__'] = mapping
        return super(ModelMetaClass, mcs).__new__(mcs, name, base, dic)
class Model(dict,metaclass=ModelMetaClass):

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except:
            Exception('not found the %s'%key)

    def save(self):
        field = []
        args = []
        for k, v in self.__mapping__.items():
            field.append(k)
            args.append(getattr(self, k,  None))

        args = [str(i) for i in args]
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(field), ','.join(args))
        print(sql)

class User(Model):
    id = IntegerFiled('id')
    name = StringFiled('name')
    age = IntegerFiled('age')

u = User(id=1, name='li', age=10)
u.save()
