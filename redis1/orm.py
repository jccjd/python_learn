from redis1.Mysqlap import MySQLApp


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s, %s>' % (self.__class__.__name__, self.name)


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class MetaClassModel(type):

    def __new__(mcs, name, base, dct):
        if name == 'Model':
            return super(MetaClassModel, mcs).__new__(mcs, name, base, dct)

        attrs = ((name, value) for name, value in dct.items() if isinstance(value, Field))

        mapping = dict((name, value) for name, value in attrs)

        for k in mapping:
            dct.pop(k)

        dct['__mappings__'] = mapping
        dct['__table__'] = name.lower()

        return super(MetaClassModel, mcs).__new__(mcs, name, base, dct)


    # def __new__(mcs, name, base, dct):
    #     if name == 'Model':
    #         return super(MetaClassModel, mcs).__new__(mcs, name, base, dct)
    #
    #     attrs = ((name, value) for name, value in dct.items() if isinstance(value, Field))
    #     mapping = dict((name, value) for name, value in attrs)
    #     for k in mapping:
    #         dct.pop(k)
    # dct['__mapping__'] = mapping
    # dct['__table__'] = name.lower()
    #
    # return super(MetaClassModel, mcs).__new__(mcs, name, bases, dic)


class Model(dict, metaclass=MetaClassModel):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append('%s' % getattr(self, k))
        # sql = 'insert into %s (%s) value (%s)' % (self.__table__, ','.join(fields), ','.join(args))
        sql = "insert into goods (name, price) value ('name', 4)"
        print('SQL: %s' % sql)
        Instance = MySQLApp.getInstance()
        Instance.insert(sql)

    def getone(self, pk):

        sql = 'select *  from %s where id=\'%s\'' % (self.__table__,  pk)

        db = MySQLApp().getInstance()
        db.query(sql)
        result = db.fetchoneRow()
        db.close()
        return result

    def delete(self, pk):
        sql = 'delete from %s where id=\'%s\'' % (self.__table__, pk)
        db = MySQLApp().getInstance()
        result = db.update(sql)  ##删除操作也是更新 主要是游标 _cur
        db.close()
        print(result)
        return result


class Goods(Model):
    # 定义类的属性到列的映射：
    name = StringField('name')
    price = IntegerField('price')


# 创建一个实例：
u = Goods(name='Michael', price=10)
# 保存到数据库：
# u.save()
print(u.getone(pk=35))

