from importent.mysingle import Singleton
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varcher(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'int')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print("Found mapping: %s==%s" % (k,v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name
        attrs['__mappings__'] = mappings
        return type.__new__(cls, name, bases, attrs)

class Model(metaclass=Singleton):
    def __init__(self, **kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute'%s'" % item)
    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args =[]
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self,k,None))

        sql = 'insert into %s (%s)' % (self.__table__,','.join(fields),','.join(params))
        print("Sql:%s" %sql)
        print("ARGS: %s" % str(args))

class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField("id")
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

user = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
user.save()


