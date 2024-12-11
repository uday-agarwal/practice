""" Singleton design pattern.

This module presents a test class and its usage as a Singleton.
"""

class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None 

    def __call__(cls,*args,**kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance

class Logger(metaclass=Singleton):
    pass

if __name__ == "__main__":
    first_instance = Logger()
    second_instance = Logger()
    print(first_instance is second_instance)
