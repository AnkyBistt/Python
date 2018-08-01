class BaseClass:

   def __init__(self):
        print("this is base class 1")


class BaseClass2:

    def __init__(self):
        print("This is base class 2")


class DerivedClass(BaseClass, BaseClass2):

    def __init__(self):
        print("this is derived class")
        base1 = BaseClass2()
        base2 = BaseClass2()

obj = DerivedClass()