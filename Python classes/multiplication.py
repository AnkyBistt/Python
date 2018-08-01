class Numbers:
    num1 = 0
    num2 = 0


    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        result =self.mul()
        print(result)




    def mul(self):
        result = self.num1 * self.num2
        return result

       # print("multiplication of these two no. is :" , result)



num1 = int(input('Enter the first no.'))
num2 = int(input('Enter the second no.'))
obj = Numbers(num1,num2)
