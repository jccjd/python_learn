class Singleton(type):

    def __init__(cls, name, base, dct):

        super(Singleton, cls).__init__(name, base, dct)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instance

class Singletons(type):

    def __init__(cls, name, base, dct):
        super(Singletons, cls).__init__(name, base, dct)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singletons, cls).__call__(*args, **kwargs)

        return cls._instance

