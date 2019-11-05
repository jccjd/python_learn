class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s %s>' % self.__class__.__name__, self.name


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaClass(type):
    def __new__(mcs, name, base, dct):
        if name == 'Model':
            super(ModelMetaClass, mcs).__new__(mcs, name, base, dct)
        attr = ((key, value) for key, value in dct.items() if isinstance(value, Field))
        mapping = dict((key, value) for key, value in attr)

        for k in mapping.keys():
            dct.pop(k)

        dct['__table__'] = name.lower()
        dct['__mapping__'] = mapping
        return super(ModelMetaClass, mcs).__new__(mcs, name, base, dct)


class Model(dict, metaclass=ModelMetaClass):

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, item):
        return self[item]

    def save(self):
        field = []
        args = []
        for k, v in self.__mapping__.items():
            field.append(v.name)
            args.append(getattr(self, k))
        print(field, args)


class User(Model):
    id = IntegerField('id')
    name = StringField('name')


u = User(id=1, name='ll')
u.save()
