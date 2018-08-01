class BaseClass:
    firstNumber = 10

    def __init__(self):
        print("this is base class")




class DerivedClass(BaseClass):


    def __init__(self):
        print("this is derived class")
        print(super(DerivedClass, self).firstNumber)


#obj = DerivedClass()
#obj = BaseClass()

