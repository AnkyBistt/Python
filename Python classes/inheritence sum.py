class BaseClass:
    num1 = 0
    num2 = 0
    result = 0


    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def sum(self):
        self.result = self.num1 + self.num2
        return self.result

class DerivedClass(BaseClass):

    def __init__(self, num1, num2):
        super(DerivedClass,self).__init__(num1, num2)
        result = super(DerivedClass, self).sum()
        print("The sum of two no. is: ", result)

try:

    num1 = int(input('Enter the first no.'))
    num2 = int(input('Enter the second no.'))
    obj = DerivedClass(num1 = num1, num2= num2)

except ValueError:

    print("enter only integer values")