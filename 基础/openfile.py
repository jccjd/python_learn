class MeataClassDB(type):
    def __new__(mcs, name, base, dct):
        if name == 'Model':
            return super(MeataClassDB, mcs).__new__(mcs,name, base, dct)

        chiose = ((k, value) for k, value in dct.items() if not k.startswith('__'))
        mapping = dict((k,v) for k, v in chiose)

        for k in mapping.keys():
            dct.pop(k)
        dct['__mapping__'] = mapping
        return super(MeataClassDB, mcs).__new__(mcs, name, base, dct)

class Model(dict,metaclass=MeataClassDB):

    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(self, *args, **kwargs)

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] =  value


    # def save(self):
    #     for k,v in self.__mapping__.items():
    #         print(k,v)

    def save(self):
        args = []
        i = 0
        for k,v in self.__mapping__.items():
            args.append(getattr(self, k, None))

            with open('data.txt','a+') as f:
                f.write("{}: {} ".format(k,args[i]))
            i += 1
    def get(self):
        with open('data.txt','r') as f:
            a = f.read()
            print(a)

class student(Model):
    id = 12
    name = 12

student = student(id='dfd',name=121)
student.get()



