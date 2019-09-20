class Singleton(type):

    def __init__(cls, name, base, dct):

        super(Singleton, cls).__init__(name, base, dct)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instance

